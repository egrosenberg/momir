import requests
import os
import json
import datetime

PREFERRED_JSON = 'oracle_cards'
JSON_PATH = 'json/cards.json'

loadedCards = None


def fetchBulkInfo():
    # Filter function to find preferred json from scryfall bulk
    def findPreferred(x):
        return x["type"] == PREFERRED_JSON
    # Get bulk info data
    bulkInfoRequest = requests.get('https://api.scryfall.com/bulk-data')
    if bulkInfoRequest.status_code != 200:
        return False
    bulkInfoData = bulkInfoRequest.json()["data"]
    # Extract info on scryfall bulk we will fetch
    bulkInfo = {}
    try:
        bulkInfo = next(filter(findPreferred, bulkInfoData))
    except StopIteration:
        print(f'Unable to find preferred JSON: "{PREFERRED_JSON}"')
        return False
    return bulkInfo


def fetchCards(bulkInfo):
    print(f'Fetching {bulkInfo["name"]}...')
    scryfallRequest = requests.get(bulkInfo["download_uri"])
    if scryfallRequest.status_code != 200:
        print(f'Error in fetching cards. CODE: {scryfallRequest.status_code}',
              f'Reason: {scryfallRequest.reason}')
        return []
    scryfallCards = scryfallRequest.json()
    print(f'Successfully fetched {len(scryfallCards)} cards')
    # Dump scryfall data to file
    print(f'Writing file "{JSON_PATH}"...')
    outFile = open(JSON_PATH, "w")
    json.dump(scryfallCards, outFile, indent=2)
    # updated metadata
    remoteLastUpdated = datetime.datetime.fromisoformat(
        bulkInfo["updated_at"]).timestamp()
    os.utime(JSON_PATH, (remoteLastUpdated, remoteLastUpdated))
    print(f'Successfully created file "{JSON_PATH}"')
    outFile.close()
    return scryfallCards


def latestCards(bulkInfo):
    print("Loading latest cards...")
    remoteLastUpdated = datetime.datetime.fromisoformat(bulkInfo["updated_at"])
    try:
        lastUpdated = os.path.getmtime(JSON_PATH)
        print(f'Found JSON data at "{JSON_PATH}"')
        if lastUpdated < remoteLastUpdated.timestamp():
            print("Local JSON is outdated")
            if bulkInfo:
                return fetchCards(bulkInfo)
            print('WARN - Unable to reach scryfall api, using outdated JSON')
        with open(JSON_PATH, 'r') as file:
            data = json.load(file)
            print(f'{len(data)} cards successfully loaded from "{JSON_PATH}"')
            file.close()
            return data
    except FileNotFoundError:
        if not bulkInfo:
            print('ERROR - no local JSON and unable to connect to API')
        print(f'{JSON_PATH} not found, creating new file...')
        return fetchCards(bulkInfo)


def fetchJson(creaturesOnly=True, unfiltered=False):
    global loadedCards
    if loadedCards:
        return loadedCards

    print("Loading card JSON...")
    # get bulk information
    bulkInfo = fetchBulkInfo()

    # Get cards json
    scryfallCards = latestCards(bulkInfo)

    if unfiltered:
        return scryfallCards

    # filter cards
    def inPaper(card):
        return "paper" in card["games"]

    def notMultiVersioned(card):
        def isComboPiece(c):
            return c["component"] == "combo_piece"
        if "all_parts" not in card:
            return True
        parts = list(filter(isComboPiece, card["all_parts"]))
        if len(parts) < 2:
            return True
        first = parts[0]["name"]
        for part in parts[1:]:
            if part["name"] != first:
                return True
        return False

    def finalFilter(card):
        if creaturesOnly and "Creature" not in card["type_line"]:
            return False
        # Filter out non-standard frame cards (these are too hard to print)
        if card["layout"] != "normal":
            return False
        return inPaper(card) and notMultiVersioned(card)

    cards = list(filter(finalFilter, scryfallCards))
    loadedCards = cards
    # Return json object
    return cards
