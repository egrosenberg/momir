import math


def sliceImage(img, height=100.0):
    slices = []
    imgWidth, imgHeight = img.size
    sliceCount = math.ceil(imgHeight / height)
    for i in range(0, sliceCount):
        top = i * height
        bottom = min(imgHeight, top + height)
        hSlice = img.crop((0, top, imgWidth, bottom))
        slices.append(hSlice)
    return slices
