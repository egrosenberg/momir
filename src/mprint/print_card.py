from .get_image import getArt
import time

CARD_FIELDS = ["name", "mana_cost", "type_line", "oracle_text", "flavor_text"]


def printCard(printer, card, artOverride=None, asToken=False):
    if "card_faces" in card:
        for face in card["card_faces"]:
            printCard(printer, face, artOverride=artOverride, asToken=asToken)
    else:
        img = artOverride or getArt(card, 256)
        for key in CARD_FIELDS:
            if key in card:
                card[key] = card[key].replace("—", "-")
        printer.set(bold=True, align="left")
        printer.textln(card["name"])
        printer.set(bold=False, align="right")
        printer.textln(card["mana_cost"])
        if img:
            printer.set(align="center")
            printer.image(img, fragment_height=50)
            printer.textln()
        printer.set(align="left", underline=True)
        if asToken:
            printer.text("Token ")
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
        if "life_modifier" in card and "hand_modifier" in card:
            printer.textln(f'Hand Size: {card["hand_modifier"]}')
            printer.textln(f'Starting Modifier: {card["hand_modifier"]}')
        printer.set(bold=False, align="left")
        time.sleep(0.5)
        printer.print_and_feed(2)
        time.sleep(0.5)
