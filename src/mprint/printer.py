from escpos.printer import Usb
from .constants import USB_ID_VENDOR, USB_ID_PRODUCT

printer = None


def getPrinter():
    global printer
    if (printer):
        return printer
    printer = Usb(USB_ID_VENDOR, USB_ID_PRODUCT, 0, profile="TM-T88III")
    printer.open()


def closePrinter():
    global printer
    if (printer):
        printer.close()
        printer = None
