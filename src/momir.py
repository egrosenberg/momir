import mprint
from mprint.cstyle import STYLE as STYLE
from mprint.constants import MOMIR_AVATAR

MOMIR_IMAGE_PATH = 'assets/momir.jpg'


def prompt():
    mprint.cstyle.clear()
    mprint.cstyle.logImage(MOMIR_IMAGE_PATH)
    mprint.cstyle.logStyled('    MOMIR ASKS: What is X?', STYLE.GREEN)


def momir(offline=False):
    printer = mprint.getPrinter()
    cards = mprint.fetchJson(creaturesOnly=True, offline=offline)
    print("Entering Momir Mode - Enter 'e' or 'escape' at any time to stop")
    print("Printing player 1 avatar...")
    mprint.printCard(printer, MOMIR_AVATAR)
    input("Press enter to print player 2 avatar...")
    mprint.printCard(printer, MOMIR_AVATAR)
    try:
        while True:
            prompt()
            n = input("")
            if n == "e" or n == "exit":
                break
            try:
                filter = {"cmc": int(n)}
                card = mprint.getRandomCard(cards, filter)
                mprint.printCard(printer, card, asToken=True)
            except ValueError:
                print("Invalid input. If you would like to exit, enter 'e'.")
    finally:
        mprint.cstyle.clear()
        mprint.cstyle.logStyled(
            'MOMIR IS CONTENTED ...for now...', STYLE.GREEN)
        return mprint.closePrinter()
