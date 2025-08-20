# USER LSUSB to decide what usb device your printer is
USB_ID_VENDOR = 0x0485
USB_ID_PRODUCT = 0x5741

DEFAULT_CARD = {
    "id": "404",
    "name": "Forofor, Locus Unknown",
    "power": 40,
    "toughness": 4,
    "mana_cost": "4 0 4",
    "type_line": "Summon - Error",
    "image_uris": {
        "art_crop": ("https://cards.scryfall.io/art_crop/front/e/6/" +
                     "e6d7fba8-a157-4d81-9d6b-bd210a96b248.jpg?1623189417")
    },
    "oracle_text": "what exactly... did you expect to find here?",
    "flavor_text": "...i hope it was nothing"
}

MOMIR_AVATAR = {
    "object": "card",
    "id": "f5ed5ad3-b970-4720-b23b-308a25f42887",
    "oracle_id": "2057571e-3ee0-4100-8fd9-00dedb8a0b2f",
    "multiverse_ids": [
        182271
    ],
    "mtgo_id": 23965,
    "name": "Momir Vig, Simic Visionary Avatar",
    "layout": "vanguard",
    "image_status": "highres_scan",
    "image_uris": {
        "art_crop": ("https://cards.scryfall.io/art_crop/front/f/5/" +
                     "f5ed5ad3-b970-4720-b23b-308a25f42887.jpg?1562953277"),
    },
    "mana_cost": "",
    "cmc": 0,
    "type_line": "Vanguard",
    "oracle_text": ("{X}, Discard a card: Create a token that's a copy"
                    "of a creature card with mana value X chosen at random"
                    "Activate only as a sorcery and only once each turn."),
    "life_modifier": "+4",
    "hand_modifier": "+0",
    "colors": [],
    "color_identity": [],
    "games": [
        "mtgo"
    ], }

__all__ = ['USB_ID_VENDOR', 'USB_ID_PRODUCT', 'MOMIR_AVATAR']
