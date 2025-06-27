import mprint
from mprint.cstyle import STYLE as STYLE

DISHARMONY_IMG_PATH = 'assets/maelstrom.jpg'


def prompt():
    mprint.cstyle.clear()
    mprint.cstyle.logImage(DISHARMONY_IMG_PATH)
    mprint.cstyle.logStyled(
        '    THE MAELSTROM RAGES ON', STYLE.RED + STYLE.BOLD)
    mprint.cstyle.logStyled(
        '(press enter to continue...)', STYLE.RED)


def discord(offline=False):
    printer = mprint.getPrinter()
    print("Entering the maelstrom....")
    cards = mprint.fetchJson(unfiltered=True, offline=offline)
    cards = mprint.filterCards(cards, {"type_line": "land"}, invertFilter=True)
    try:
        while True:
            prompt()
            input("")
            card = mprint.getRandomCard(cards)
            mprint.printCard(printer, card, asToken=True)
    finally:
        mprint.cstyle.clear()
        mprint.cstyle.logStyled(
            'YOU HAVE ESCAPED THE MAELSTROM...', STYLE.RED)
        return mprint.closePrinter()
