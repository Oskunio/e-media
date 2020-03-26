import png
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from PIL import Image
from PIL.ExifTags import TAGS


def getExif(filename):
    print("Getting EXIF data from your file:", filename)
    print("\n Using PyPNG \n")
    image = png.Reader(filename)
    for c in image.chunks():
        print(c[0], len(c[1]))

    print("\n Using hachoir \n")
    parser = createParser(filename)
    metadata = extractMetadata(parser)
    for line in metadata.exportPlaintext():
        print(line)

    print("\n Using Pillow \n")
    image = Image.open(filename)
    for tag, value in image.info.items():
        key = TAGS.get(tag, tag)
        print(key + " " + str(value))
