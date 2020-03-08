import cv2
# szukanie chunksow i usuwanie ich
# funkcja przyjmuje nazwe pliku, a zwraca nowy plik tekstowy (obraz)
def findAndRemoveAncillaryChunk(filename):
    #ancillary chunks in hex code
    chunks = ["624b4744","6348524d","64534947","65584966","67414d41","68495354","69434350","69545874","70485973","73424954","73504c54","73524742","73544552","74455874","74494d45","74524e53","7a545874"]

    constChunkLengthInBytes = 12
    constChunkLength = 2*constChunkLengthInBytes

    #open and convert file to hex string
    handler = open(filename, 'rb')
    newTextFile = handler.read().hex()

    for element in chunks:
        posInText = newTextFile.find(element) #if not found returns -1
        if posInText != -1:
            length = newTextFile[(posInText-8):posInText]
            chunkLengthDec = int(length, 16)
            realLength = 2*chunkLengthDec
            firstpart = newTextFile[0:(posInText-8)]
            secondpart = newTextFile[((posInText-8)+realLength+constChunkLength):]
            newTextFile = firstpart+secondpart
    print("Ancillary chunks removed")
    return newTextFile

#wyswietla plik w czytelnym dla czlowieka formacie
def pritnFileInAnsi(filename):
    file = open(filename, encoding='ANSI')
    f2 = file.read()
    print(f2)
    file.close()

def printFileInHex(filename):
    handler = open(filename, 'rb')
    hexFile = handler.read().hex()
    print(hexFile)

def displayImage(filename):
    img = cv2.imread(filename)
    window = "Window"
    # Create a named window
    cv2.namedWindow(window)

    # Move window to certain place
    cv2.moveWindow(window, 600, 200)

    # Percent of original size
    scale_percent = 1000
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    # Resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    cv2.imshow(window, resized)
    cv2.waitKey()
    cv2.destroyAllWindows()

def showImgInfo(filename):
    img = cv2.imread(filename)
    shape = img.shape
    # dimensions of picture
    print("shape:(x,y,color format table size):",shape)
    # size
    size = img.size
    print("size:", size)

def HexStrigToPNG(filename, newFile):
    data = bytes.fromhex(newFile)
    with open(filename, 'wb') as file:
        file.write(data)
    file.close()

