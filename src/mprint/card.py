from .constants import DEFAULT_CARD
from random import randint

PARTIAL_MATCH_KEYS = ["flavor_text", "oracle_text", "type_line", ]


def filterCards(cards, filter={}):
    def filterFn(card):
        for key, value in filter:
            if key not in card:
                return False
            cardVal = card[key]
            if isinstance(cardVal, str):
                cardVal = cardVal.lower()
                value = value.lower()
            if key in PARTIAL_MATCH_KEYS:
                if value not in cardVal:
                    return False
            if value != cardVal:
                return False
        return True
    return list(filter(filterFn, cards))


def getRandomCard(cards, filter={}):
    filtered = filterCards(cards, filter)
    count = len(filtered)
    if count == 0:
        print("NO CARD FOUND MATCHING FILTER")
        return DEFAULT_CARD
    return filtered[randint(0, count-1)]


def getCard(cards, filter={}):
    filtered = filterCards(cards, filter)
    if len(filtered) == 0:
        print("NO CARD FOUND MATCHING FILTER")
        return DEFAULT_CARD
    return filtered[0]
