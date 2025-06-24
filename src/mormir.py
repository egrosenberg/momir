from . import printCard, randomByMv


def mormir(cards, printer):
    while True:
        n = input("Enter a number between 0 and 16 (e to exit)")
        if n == "e" or n == "exit":
            break
        try:
            card = randomByMv(cards, int(n))
            printCard(printer, card)
        except ValueError:
            print("Invalid input")
