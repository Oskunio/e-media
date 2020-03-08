
#szukanie chunksow i usuwanie ich
#funkcja przyjmuje nazwe pliku, a zwraca nowy plik tekstowy (obraz)
def findChunk(filename):
    chunks = ["624b4744","6348524d","64534947","65584966","67414d41","68495354","69434350","69545874","70485973","73424954","73504c54","73524742","73544552","74455874","74494d45","74524e53","7a545874"]
    #chunks = ["73524742"]

    constChunkLengthInBytes=12;
    constChunkLength=2*constChunkLengthInBytes
    handler = open(filename, 'rb')
    hexFile = handler.read().hex()
    newTextFile = hexFile
    for element in chunks:
        posInText=hexFile.find(element) #dodac petle w ktorej zmienia sie nazwe chunksa
        print('check position:',posInText)
        if posInText != -1:

            length=newTextFile[(posInText-8):posInText]
            print("length:", length)
            chunkLengthDec=int(length,16)
            realLength=2*chunkLengthDec
            firstpart=newTextFile[0:(posInText-8)]
            secondpart=newTextFile[((posInText-8)+realLength+constChunkLength):]
            newTextFile=firstpart+secondpart
            print('new lenght:',len(newTextFile))
            print(newTextFile)
    return newTextFile

