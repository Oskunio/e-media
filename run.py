import functions
import getExif

filename = "./images/square.png"
filename1 = './images/newSquare.png'
filename2 = "./images/squareWithExif.png"


functions.displayImage(filename) #wyswietla orginalny obraz

newFile = functions.findAndRemoveAncillaryChunk(filename) # usuwa ancillary chunks

functions.HexStringToPNG(filename1, newFile)

functions.displayImage(filename1) #wyswietla obraz po usunieciu metadanych
print("Interpretacja IHDR:")
functions.IHDRinterpetation(filename)
print()
functions.fourierTransform(filename)

getExif.getExif(filename2)

