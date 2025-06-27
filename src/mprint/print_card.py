from .get_image import getArt
import time


def printCard(printer, card, artOverride=None):
    if "card_faces" in card:
        for face in card["card_faces"]:
            printCard(printer, face, artOverride=artOverride)
    else:
        img = artOverride or getArt(card, 256)
        printer.set(bold=True, align="left")
        printer.textln(card["name"])
        printer.set(bold=False, align="right")
        printer.textln(card["mana_cost"])
        if img:
            printer.set(align="center")
            printer.image(img, fragment_height=50)
            printer.textln()
        printer.set(align="left", underline=True)
        printer.textln(card["type_line"])
        printer.set(underline=False)
        if "oracle_text" in card and len(card["oracle_text"]):
            printer.textln()
            printer.textln(card["oracle_text"])
        if "flavor_text" in card and len(card["flavor_text"]):
            printer.set(align="center")
            printer.textln("-------------------------")
            printer.set(align="left")
            printer.set(font="b")
            printer.textln(card["flavor_text"])
            printer.set(font="a")
        printer.set(bold=True, align="right")
        if "power" in card and "toughness" in card:
            printer.textln(f'{card["power"]}/{card["toughness"]}')
        printer.set(bold=False, align="left")
        time.sleep(0.5)
        printer.print_and_feed(2)
        time.sleep(0.5)
