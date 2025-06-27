import os
import io
import requests
from PIL import Image, ImageEnhance
from .constants import DEFAULT_CARD

IMAGES_DIR = 'img/'


def raiseBlackPoint(img, level):
    blackpoint = level*255

    def mod(c):
        point = c * (255-blackpoint)/255
        return point + blackpoint
    return img.point(mod)

# ------------------------------------------------------------
# Downloads the art crop of a card and return it as a PIL Image
# ------------------------------------------------------------


def downloadArt(card):
    id = ""
    if "id" in card:
        id = card["id"]
    elif "illustration_id" in card:
        id = card["illustration_id"]

    uri = card.get("image_uris", {}).get("art_crop", False)
    if not uri:
        return False
    request = requests.get(uri, stream=True)
    if (request.status_code != 200):
        print(f'ERROR: unable to fetch image for {card["name"]}')
        return False
    i = Image.open(io.BytesIO(request.content))
    i.save(os.path.join(IMAGES_DIR, f'{id}.jpg'), quality=85)
    return i


# ------------------------------------------------------------
# Returns the art crop of a given card as a PIL image
# ------------------------------------------------------------
def getArt(card, maxSize=256):
    # check for existing local image
    id = ""
    if "id" in card:
        id = card["id"]
    elif "illustration_id" in card:
        id = card["illustration_id"]
    path = os.path.join(IMAGES_DIR, f'{id}.jpg')
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
    img = raiseBlackPoint(img, 0.3)
    img = ImageEnhance.Brightness(img).enhance(1.1)
    img = ImageEnhance.Contrast(img).enhance(1.5)
    return img
