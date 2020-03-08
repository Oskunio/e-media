def findChunk2(text):
    x=text.find('sRGB')
    if x != 1:
        return text[x:(x+4)]

#szukanie chunksow i usuwanie ich
#nieskonczone !!!
#funkcja ma zwracac docelowo kod nowego pliku
def findChunk(filename):
    chunks=["bKGD","cHRM","dSIG"] #dodac reszte
    newTextFile = ''

    handler1 = open(filename, encoding='ANSI')
    textFile=handler1.read()

    handler2 = open(filename, 'rb')
    hexFile = handler2.read().hex()

    posInText=textFile.find('sRGB') #dodac petle w ktorej zmienia sie nazwe chunksa

    print('check position:',posInText)
    if posInText != 1:
        y=2*posInText+2 #y is posInHex
        chunkLengthHex=hexFile[(y-4):y]
        print("length:", chunkLengthHex)
        chunkLengthDec=int(chunkLengthHex,16)
        newTextFile=textFile[0:(posInText-4)]+textFile[((posInText-1)+chunkLengthDec):]
        return chunkLengthDec

