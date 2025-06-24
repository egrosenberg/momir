from escpos.printer import Usb
from .constants import USB_ID_VENDOR, USB_ID_PRODUCT
from .get_image import getArt


def printCard(card):
    p = Usb(USB_ID_VENDOR, USB_ID_PRODUCT, 0, profile="TM-T88III")
    p.open()
    img = getArt(card, 256)
    p.set(bold=True, align="left")
    p.textln(card["name"])
    p.set(bold=False, align="right")
    p.textln(card["mana_cost"])
    p.set(align="center")
    p.image(img, fragment_height=50)
    p.textln()
    p.set(align="left", underline=True)
    p.textln(card["type_line"])
    p.textln()
    p.set(underline=False)
    p.textln(card["oracle_text"])
    if ("flavor_text" in card):
        p.set(align="center")
        p.textln("-------------------------")
        p.set(align="left")
        p.set(font="b")
        p.textln(card["flavor_text"])
        p.set(font="a")
