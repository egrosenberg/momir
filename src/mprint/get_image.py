import os
import io
import requests
from PIL import Image
from .constants import DEFAULT_CARD

IMAGES_DIR = 'img/'


# ------------------------------------------------------------
# Downloads the art crop of a card and return it as a PIL Image
# ------------------------------------------------------------
def downloadArt(card):
    uri = card["image_uris"]["art_crop"]
    request = requests.get(uri, stream=True)
    if (request.status_code != 200):
        print(f'ERROR: unable to fetch image for {card["name"]}')
        return False
    i = Image.open(io.BytesIO(request.content))
    i.save(os.path.join(IMAGES_DIR, f'{card["id"]}.jpg'), quality=85)
    return i


# ------------------------------------------------------------
# Returns the art crop of a given card as a PIL image
# ------------------------------------------------------------
def getArt(card, maxSize=256):
    # check for existing local image
    path = os.path.join(IMAGES_DIR, f'{card["id"]}.jpg')
    cached = os.path.isfile(path)
    if cached:
        img = Image.open(path)
    else:
        img = downloadArt(card)
        if not img:
            # attempt to use default card image
            dPath = os.path.join(IMAGES_DIR, f'{DEFAULT_CARD["id"]}.jpg')
            backupExists = os.path.isfile(dPath)
            if not backupExists:
                return False
            img = Image.open(dPath)
    # resize image
    width, height = img.size
    ratio = min(maxSize/width, maxSize/height)
    size = (width*ratio, height*ratio)
    img.thumbnail(size)
    return img
