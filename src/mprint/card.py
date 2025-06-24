from .constants import DEFAULT_CARD
from random import randint

PARTIAL_MATCH_KEYS = ["flavor_text", "oracle_text", "type_line", ]


def match(a, b, partialMatch=False):
    if isinstance(a, str):
        a = a.lower()
    if isinstance(b, str):
        b = b.lower()
    if partialMatch:
        return a in b or b in a
    return a == b


def filterCards(cards, filterDict={}):
    def filterFn(card):
        for key, value in filterDict.items():
            if key not in card:
                return False
            partialMatch = key in PARTIAL_MATCH_KEYS
            if not match(value, card[key], partialMatch):
                return False
        return True
    return list(filter(filterFn, cards))


def getRandomCard(cards, filterDict={}):
    filtered = filterCards(cards, filterDict)
    count = len(filtered)
    if count == 0:
        print("NO CARD FOUND MATCHING FILTER")
        return DEFAULT_CARD
    return filtered[randint(0, count-1)]


def getCard(cards, filterDict={}):
    filtered = filterCards(cards, filterDict)
    if len(filtered) == 0:
        print("NO CARD FOUND MATCHING FILTER")
        return DEFAULT_CARD
    return filtered[0]
