def findChunk2(text):
    chunks = ["sRGB", "bKGD", "cHRM", "dSIG", "IHDR"]  # dodac reszte
    newTextFile = ''
    constChunkLength = 12;
    handler1 = open(filename, encoding='ANSI')
    textFile = handler1.read()
    print('textFileLength:', len(textFile))

    handler2 = open(filename, 'rb')
    hexFile = handler2.read().hex()

    for element in chunks:
        posInText = textFile.find(element)  # dodac petle w ktorej zmienia sie nazwe chunksa
        print('check position:', posInText)
        if posInText != 1:
            y = 2 * posInText + 2  # y is posInHex
            chunkLengthHex = hexFile[(y - 8):y]
            print("length:", chunkLengthHex)
            chunkLengthDec = int(chunkLengthHex, 16)
            firstpart = textFile[0:(posInText - 2)]
            secondpart = textFile[((posInText - 2) + chunkLengthDec + constChunkLength):]
            newTextFile = firstpart + secondpart
            print('new lenght:', len(newTextFile))
            print(newTextFile)
            return newTextFile

#szukanie chunksow i usuwanie ich
#nieskonczone !!!
#funkcja ma zwracac docelowo kod nowego pliku
def findChunk(filename):
    chunks=["sRGB","bKGD","cHRM","dSIG", "IHDR"] #dodac reszte
    newTextFile = ''
    constChunkLength=12;
    handler1 = open(filename, encoding='ANSI')
    textFile=handler1.read()
    print('textFileLength:',len(textFile))

    handler2 = open(filename, 'rb')
    hexFile = handler2.read().hex()

    for element in chunks:
        posInText=textFile.find(element) #dodac petle w ktorej zmienia sie nazwe chunksa
        print('check position:',posInText)
        if posInText != 1:
            y=2*posInText+2 #y is posInHex
            chunkLengthHex=hexFile[(y-8):y]
            print("length:", chunkLengthHex)
            chunkLengthDec=int(chunkLengthHex,16)
            firstpart=textFile[0:(posInText-2)]
            secondpart=textFile[((posInText-2)+chunkLengthDec+constChunkLength):]
            newTextFile=firstpart+secondpart
            print('new lenght:',len(newTextFile))
            print(newTextFile)
            return newTextFile

