import cv2
import numpy as np
from matplotlib import pyplot as plt



def fourierTransform(filename):
    img = cv2.imread(filename, 0)
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)
    magnitude_spectrum = 20*np.log(np.abs(fshift))
    phase_spectrum = np.angle(fshift)
    plt.subplot(131), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(132), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.subplot(133), plt.imshow(phase_spectrum, cmap='gray')
    plt.title('Phase Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

# szukanie chunksow i usuwanie ich
# funkcja przyjmuje nazwe pliku, a zwraca nowy plik tekstowy (obraz)
def findAndRemoveAncillaryChunk(filename):
    # ancillary chunks in hex code
    chunks = ["624b4744", "6348524d", "64534947", "65584966", "67414d41",
              "68495354", "69434350", "69545874", "70485973", "73424954",
              "73504c54", "73524742", "73544552", "74455874", "74494d45",
              "74524e53", "7a545874"]

    constChunkLengthInBytes = 12
    constChunkLength = 2*constChunkLengthInBytes

    # open and convert file to hex string
    handler = open(filename, 'rb')
    newTextFile = handler.read().hex()

    for element in chunks:
        posInText = newTextFile.find(element)  # if not found returns -1
        if posInText != -1:
            length = newTextFile[(posInText-8):posInText]
            chunkLengthDec = int(length, 16)
            realLength = 2*chunkLengthDec
            firstpart = newTextFile[0:(posInText-8)]
            secondpart = newTextFile[(
                (posInText-8)+realLength+constChunkLength):]
            newTextFile = firstpart+secondpart
    print("Ancillary chunks removed")
    handler.close()
    return newTextFile


# wyswietla plik w czytelnym dla czlowieka formacie
def pritnFileInAnsi(filename):
    file = open(filename, encoding='ANSI')
    f2 = file.read()
    print(f2)
    file.close()

# wyswietla plik w kodzie szesnastkowym
def printFileInHex(filename):
    handler = open(filename, 'rb')
    hexFile = handler.read().hex()
    print(hexFile)
    handler.close()

#wyswietla obraz
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
    print("shape:(x,y,color format table size):", shape)
    # size
    size = img.size
    print("size:", size)


def HexStringToPNG(filename, newFile):
    data = bytes.fromhex(newFile)
    with open(filename, 'wb') as file:
        file.write(data)
    file.close()


# IHDR data: it contains (in this order) the image's width (4 bytes),
# height (4 bytes),
# bit depth (1 byte),
# color type (1 byte),
# compression method (1 byte),
# filter method (1 byte),
# interlace method (1 byte)
# (13 data bytes total)
def IHDRinterpetation(filename):
    # open and convert file to hex string
    handler = open(filename, 'rb')
    hexFile = handler.read().hex()
    posInText = hexFile.find("49484452")

    if posInText != -1:
        width = hexFile[(posInText+8):(posInText+16)]
        widthDec = int(width, 16)
        print("Width: ", widthDec)

        height = hexFile[(posInText + 16):(posInText + 24)]
        heightDec = int(height, 16)
        print("Height: ", heightDec)

        # Bit depth is a single-byte integer giving the number of bits
        # per sample or per palette index (not per pixel)
        bitDepth = hexFile[(posInText + 24):(posInText + 26)]
        bitDepthDec = int(bitDepth, 16)
        print("Bit depth: ", bitDepthDec)

        # color type-img type: 0-grayscale, 2-truecolor, 3-indexed-colour,
        # 4-grayscale with alpha, 6-truecolor with aplha
        color = hexFile[(posInText + 26):(posInText + 28)]
        colorDec = int(color, 16)
        print("Color type: ",
              {0: "Grayscale",
               2: "Truecolor",
               3: "Indexed-colour",
               4: "Grayscale with alpha",
               6: "Truecolor with aplha"}.get(colorDec, colorDec))

        # PNG compression method 0 is deflate/inflate compression
        compression = hexFile[(posInText + 28):(posInText + 30)]
        compressionDec = int(compression, 16)
        print("Compression method: ", {
              0: "Deflate/inflate"}.get(compressionDec, compressionDec))

        filter = hexFile[(posInText + 30):(posInText + 32)]
        filterDec = int(filter, 16)
        print("Filter method: ", {
            0: "None",
            1: "Sub",
            2: "Up",
            3: "Average",
            4: "Path"}.get(filterDec, filterDec))

        # 0-the null method, Interlace method 1, known as Adam7
        inter = hexFile[(posInText + 32):(posInText + 34)]
        interDec = int(inter, 16)
        print("Interlace method: ", {
              0: "Null method",
              1: "Interlace method - Adam7"}.get(interDec, interDec))

    else:
        print("IHDR not found")

def PLTEread(filename):
    handler = open(filename, 'rb')
    hexFile = handler.read().hex()
    posInText = hexFile.find("504c5445")

    if posInText != -1:
        length = hexFile[(posInText - 8):posInText]
        chunkLengthDec = int(length, 16)
        realLength = 2 * chunkLengthDec
        posInText += 8
        i = 0
        while i < realLength / 3:
            red = hexFile[posInText:(posInText+2)]
            redDec = int(red, 16)
            posInText += 2
            green = hexFile[posInText:(posInText + 2)]
            greenDec = int(green, 16)
            posInText += 2
            blue = hexFile[posInText:(posInText + 2)]
            blueDec = int(blue, 16)
            posInText += 2
            print("Entry:" + str(i) + " Red:" + str(redDec) + " Green:" + str(greenDec) + " Blue:" + str(blueDec))
            i += 1
    else:
        print("PLTE not found")

# The tIME chunk gives the time of the last image modification (not the time of initial image creation)
def tIMEread(filename):
    handler = open(filename, 'rb')
    hexFile = handler.read().hex()
    posInText = hexFile.find("74494d45")

    if posInText != -1:
        posInText += 8  # skip chunk name
        year = hexFile[posInText:(posInText+4)]
        yearDec = int(year, 16)

        posInText += 4
        month = hexFile[posInText:(posInText + 2)]
        monthDec = int(month, 16)

        posInText += 2
        day = hexFile[posInText:(posInText + 2)]
        dayDec = int(day, 16)

        posInText += 2
        hour = hexFile[posInText:(posInText + 2)]
        hourDec = int(hour, 16)

        posInText += 2
        minutes = hexFile[posInText:(posInText + 2)]
        minutesDec = int(minutes, 16)

        posInText += 2
        seconds = hexFile[posInText:(posInText + 2)]
        secondsDec = int(seconds, 16)

        print(str(yearDec) + "-" + str(monthDec) + "-" + str(dayDec))
        print(str(hourDec) + ":" + str(minutesDec) + ":" + str(secondsDec))

    else:
        print("tIME not found")

# The pHYs chunk specifies the intended pixel size or aspect ratio for display of the image
def pHYsRead(filename):
    handler = open(filename, 'rb')
    hexFile = handler.read().hex()
    posInText = hexFile.find("70485973")

    if posInText != -1:
        posInText += 8  # skip chunk name
        Xaxis = hexFile[posInText:(posInText + 8)]
        XaxisDec = int(Xaxis, 16)
        print("Pixels per unit, X axis:", XaxisDec)

        posInText += 8 #skip X axis
        Yaxis = hexFile[posInText:(posInText + 8)]
        YaxisDec = int(Yaxis, 16)
        print("Pixels per unit, Y axis:", YaxisDec)

        posInText += 8  # skip Yaxis
        unit = hexFile[posInText:(posInText + 2)]
        unitDec = int(unit, 16)
        print("Unit specifier:", unitDec)

        if unitDec == 1:
            print("unit is the meter")
        else:
            print("unit is unknown")
    else:
        print("pHYs not found")


def IDATread(filename):
    handler = open(filename, 'rb')
    hexFile = handler.read().hex()
    posInText = hexFile.find("49444154")

    if posInText != -1:
        length = hexFile[(posInText - 8):posInText]
        chunkLengthDec = int(length, 16)
        realLength = 2 * chunkLengthDec
        posInText += 8  # skip name
        print(hexFile[posInText:(posInText + realLength)])
