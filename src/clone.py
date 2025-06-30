from mprint.constants import DEFAULT_CARD
import mprint
from mprint.cstyle import STYLE as STYLE
import re

ILLEGAL_CHARS = r'[^a-zA-Z0-9]'
MAX_MATCHES = 10
MIRRORWORKS_SPLASH = 'assets/mirrorworks.jpg'


def displaySplash():
    mprint.cstyle.clear()
    mprint.cstyle.logImage(MIRRORWORKS_SPLASH)
    mprint.cstyle.logStyled(
        '    WELCOME TO THE MIRRORWORKS\n',  STYLE.YELLOW + STYLE.BOLD)
    mprint.cstyle.logStyled(
        'Enter a card name or Press ctrl+c to exit', STYLE.YELLOW)


def getExactlyNamed(cards, name):
    name = str(name).lower()

    def exactlyNamed(card):
        return name == card["name"].lower()

    filtered = list(filter(exactlyNamed, cards))
    if not len(filtered):
        return False
    return filtered[0]


def getSimilarlyNamed(cards, name):
    cleanName = str(name).lower()
    cleanName = re.sub(ILLEGAL_CHARS, '', cleanName)

    def similarlyNamed(card):
        cardName = re.sub(ILLEGAL_CHARS, '', card["name"]).lower()
        return cleanName in cardName

    return list(filter(similarlyNamed, cards))


def getNamedCard(cards, name):
    print(name)
    exactMatch = getExactlyNamed(cards, name)
    if exactMatch:
        return exactMatch
    partialMatches = getSimilarlyNamed(cards, name)
    if not len(partialMatches) or len(partialMatches) > MAX_MATCHES:
        return DEFAULT_CARD
    if len(partialMatches) > MAX_MATCHES:
        print(f'More than {MAX_MATCHES} matches, please try again.')
    if len(partialMatches) == 1:
        return partialMatches[0]
    # Narrow down result
    print(f'{len(partialMatches)} results found, enter a number to print it')
    # width is 2 chars if 10 or greater (we will never be counting to 100)
    width = 1 if len(partialMatches) < 10 else 2
    for i in range(len(partialMatches)):
        print(('{0: > '+str(width)+'}').format(i), end='')
        print(f': {partialMatches[i]["name"]}')
    index = -1
    while index < 0 or index >= len(partialMatches):
        try:
            index = int(input("Enter the number of the card you seek...\n"))
            if (index >= len(partialMatches) or index < 0):
                print("invalid number :(")
        except TypeError:
            print("Please enter a number next time :/")
    return partialMatches[index]


def promptCardToPrint(cards):
    cname = input("Card Name: ")
    if not cname:
        return False
    card = getNamedCard(cards, cname)
    if not card:
        promptCardToPrint(cards)
    return card


def mirrorworks(offline=False):
    try:
        cards = mprint.fetchJson(unfiltered=True, offline=offline)
        printer = mprint.getPrinter()
        displaySplash()
        while True:
            card = promptCardToPrint(cards)
            if not card:
                break
            mprint.printCard(printer, card)
    except KeyboardInterrupt:
        _ = 0
    finally:
        mprint.cstyle.clear()
        mprint.cstyle.logStyled('EXITING THE MIRRORWORKS....', STYLE.YELLOW)
        mprint.closePrinter()
