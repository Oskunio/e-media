import functions

filename = "square.png"
filename2 = 'newSquare.png'
functions.displayImage(filename)
functions.showImgInfo(filename)
functions.pritnFileInAnsi(filename)
functions.printFileInHex(filename)
print()

newFile = functions.findAndRemoveAncillaryChunk(filename)

functions.HexStrigToPNG(filename2, newFile)
functions.displayImage(filename2)
functions.pritnFileInAnsi(filename2)
functions.printFileInHex(filename2)




