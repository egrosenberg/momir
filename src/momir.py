from . import mprint


def momir(offline=False):
    printer = mprint.getPrinter()
    cards = mprint.fetchJson(creaturesOnly=True, offline=offline)
    print("Entering Momir Mode - Enter 'e' or 'escape' at any time to stop")
    try:
        while True:
            n = input("Enter a number between 0 and 16: ")
            if n == "e" or n == "exit":
                break
            try:
                filter = {"cmc": int(n)}
                card = mprint.getRandomCard(cards, filter)
                card["type_line"] = "Token " + card["type_line"]
                mprint.printCard(printer, card)
            except ValueError:
                print("Invalid input. If you would like to exit, enter 'e'.")
    except KeyboardInterrupt:
        return mprint.closePrinter()
    mprint.closePrinter()
