import mprint
from rich.progress import Progress


def getArt(card):
    if "card_faces" in card:
        for face in card["card_faces"]:
            getArt(face)
    else:
        return mprint.getArt(card)
    return True


def downloadAllImages():
    cards = mprint.fetchJson(unfiltered=True)
    with Progress() as p:
        task = p.add_task("Downloading Card Images...", total=len(cards))
        for card in cards:
            getArt(card)
            p.update(task, advance=1)


if __name__ == '__main__':
    downloadAllImages()
