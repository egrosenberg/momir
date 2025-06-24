from escpos.printer import Usb
from .constants import USB_ID_VENDOR, USB_ID_PRODUCT
from .get_image import getArt


def printCard(printer, card):
    printer = Usb(USB_ID_VENDOR, USB_ID_PRODUCT, 0, profile="TM-T88III")
    printer.open()
    img = getArt(card, 256)
    printer.set(bold=True, align="left")
    printer.textln(card["name"])
    printer.set(bold=False, align="right")
    printer.textln(card["mana_cost"])
    printer.set(align="center")
    printer.image(img, fragment_height=50)
    printer.textln()
    printer.set(align="left", underline=True)
    printer.textln(card["type_line"])
    printer.textln()
    printer.set(underline=False)
    printer.textln(card["oracle_text"])
    if ("flavor_text" in card):
        printer.set(align="center")
        printer.textln("-------------------------")
        printer.set(align="left")
        printer.set(font="b")
        printer.textln(card["flavor_text"])
        printer.set(font="a")
