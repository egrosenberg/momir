import mprint
from mprint.constants import DEFAULT_CARD
from random import randint
import re
from mprint.cstyle import STYLE as STYLE

MODIFIERS = [
    "Creature",
    "Instant",
    "Sorcery",
    "Land",
    "Artifact",
    "Enchantment",
    "Planeswalker",
    "Battle",
    "Instant",
    "Sorcery",
    "Kindred",
    "Snow",
    "Legendary"
]
SE_SPLASH = 'assets/se.jpg'


def displaySplash():
    mprint.cstyle.clear()
    mprint.cstyle.logImage(SE_SPLASH)
    mprint.cstyle.logStyled('    YOU HAVE UNCOVERED ',
                            STYLE.YELLOW + STYLE.BOLD, end='')
    mprint.cstyle.logStyled('Sarpadian Empires, Vol. VII',
                            STYLE.YELLOW + STYLE.BOLD + STYLE.UNDERLINE)
    mprint.cstyle.logStyled(
        'Enter token details or press ctrl+c to exit', STYLE.YELLOW)


def splitTypes(types):
    modifiers = list(filter(lambda t: t in MODIFIERS, types))
    nonMod = list(filter(lambda t: t not in MODIFIERS, types))
    return nonMod, modifiers


def getTokenArt(cards, creatureTypes, modifiers=[]):
    # Create pool of all possible cards for creature types
    artPool = []
    for cType in creatureTypes:
        artPool += mprint.filterCards(cards, {"type_line": cType})
    # Remove duplicates
    uniqueCards = []
    [uniqueCards.append(val) for val in artPool if val not in uniqueCards]

    # Return default in case of no hits
    if len(uniqueCards) == 0:
        return mprint.getArt(DEFAULT_CARD)

    # Store backup cards list
    fallBackCards = uniqueCards.copy()

    # Filter list by modifier types
    for m in modifiers:
        uniqueCards = mprint.filterCards(uniqueCards, {"type_line": m})

    # Use backup in case of reducing hits to 0
    if len(uniqueCards) == 0:
        uniqueCards = fallBackCards

    # Get art for card
    return mprint.getArt(uniqueCards[randint(0, len(uniqueCards)-1)])


def createToken(cards, printer):
    card = {}
    # Get mana cost
    card["mana_cost"] = input("Mana cost (empty for none): ") or ""
    # Get token types
    types = re.split(r'\s+', input("Token types: ").strip())
    for i in range(0, len(types)):
        types[i] = types[i].lower().capitalize()
    nonMod, modifiers = splitTypes(types)

    # Set name and type line
    card["type_line"] = "Token "
    card["name"] = ""
    for m in modifiers:
        card["type_line"] += m + " "
    if len(modifiers):
        card["type_line"] += " — "
    for n in nonMod:
        card["type_line"] += n + " "
        card["name"] += n + " "
    card["type_line"] = card["type_line"].strip()
    card["name"] += "Token"
    # Get oracle text
    card["oracle_text"] = input("Input oracle text (one line): ") or ""

    # Get P/T if creature
    if "Creature" in types:
        try:
            card["power"] = int(input("Token power: "))
        except ValueError:
            card["power"] = 0
        try:
            card["toughness"] = int(input("Token toughness: "))
        except ValueError:
            card["toughness"] = 0

    count = False
    while not count:
        try:
            count = int(input("How many to print? (default 1): "))
        except ValueError:
            count = 1

    for i in range(0, count):
        # get art
        tokenArt = getTokenArt(cards, nonMod, modifiers)

        # print token
        mprint.printCard(printer, card, artOverride=tokenArt)
        if count != i:
            input("Tear token and press enter to continue...")


def tokenCreator(offline=False):
    try:
        printer = mprint.getPrinter()
        cards = mprint.fetchJson(creaturesOnly=False, offline=offline)
        displaySplash()
        while True:
            createToken(cards, printer)
    except KeyboardInterrupt:
        _ = 0
    finally:
        mprint.closePrinter()
        mprint.cstyle.clear()
        mprint.cstyle.logStyled('You abandon your reading...', STYLE.YELLOW)
