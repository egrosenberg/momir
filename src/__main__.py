from __init__ import mirrorworks, tokenCreator, momir
from mprint import cstyle, closePrinter
from mprint.cstyle import STYLE

offline = False


def flipOffline():
    global offline
    offline = not offline
    print(f"Now {'offline' if offline else 'online'}")


ACTIVITES = {
    "1": momir,
    "2": mirrorworks,
    "3": tokenCreator,
    "o": flipOffline
}


def prompt():
    cstyle.logStyled("Select an application to run: ",
                     STYLE.BOLD + STYLE.UNDERLINE)
    cstyle.logStyled("1. Momir's Lab", STYLE.BOLD + STYLE.GREEN)
    cstyle.logStyled("2. The Mirrorworks", STYLE.BOLD + STYLE.YELLOW)
    cstyle.logStyled("3. Sarpadian Empires, Vol. VII",
                     STYLE.BOLD + STYLE.MAGENTA)
    print('\n Enter \'o\' to toggle offline mode')


if __name__ == '__main__':
    try:
        while True:
            t = 1
            while True:
                prompt()
                t = input()
                if t not in ACTIVITES:
                    cstyle.logStyled("Invalid selection, try again",
                                     STYLE.BOLD + STYLE.RED)
                else:
                    break
            ACTIVITES[t]()
    except KeyboardInterrupt:
        _ = 0
    finally:
        closePrinter()
