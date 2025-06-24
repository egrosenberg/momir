from . import printCard, randomByMv


def momir(cards, printer):
    print("Entering Momir Mode - Enter 'e' or 'escape' at any time to stop")
    while True:
        n = input("Enter a number between 0 and 16: ")
        if n == "e" or n == "exit":
            break
        try:
            card = randomByMv(cards, int(n))
            printCard(printer, card)
        except ValueError:
            print("Invalid input")
