from . import mprint


def momir():
    printer = mprint.getPrinter()
    cards = mprint.fetchJson(creaturesOnly=True)
    print("Entering Momir Mode - Enter 'e' or 'escape' at any time to stop")
    try:
        while True:
            n = input("Enter a number between 0 and 16: ")
            if n == "e" or n == "exit":
                break
            try:
                card = mprint.randomByMv(cards, int(n))
                mprint.printCard(printer, card)
            except ValueError:
                print("Invalid input. If you would like to exit, enter 'e'.")
    except KeyboardInterrupt:
        return mprint.closePrinter()
    mprint.closePrinter()
