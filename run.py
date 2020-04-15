import functions
import getExif

filename = "./images/square.png"
filename1 = './images/newSquare.png'
filename2 = "./images/squareWithExif.png"
filenameWithPLTE = "./images/tygrys.png"
filenameWithTIME = "./images/jez.png"

print("Physical pixel dimensions:")
functions.pHYsRead(filename)
print()
print("IDAT data:")
functions.IDATread(filename)
print()
print("Last modification time:")
functions.tIMEread(filenameWithTIME)
print()
print("Palette:")
functions.PLTEread(filenameWithPLTE)
print()
print("Interpretacja IHDR:")
functions.IHDRinterpetation(filename)
functions.displayImage(filename) #wyswietla orginalny obraz

newFile = functions.findAndRemoveAncillaryChunk(filename) # usuwa ancillary chunks

functions.HexStringToPNG(filename1, newFile)

functions.displayImage(filename1) #wyswietla obraz po usunieciu metadanych

print()
functions.fourierTransform(filename)

getExif.getExif(filename2)

