import binascii
import cv2
import numpy as np
import functions
import base64

filename = "square.png"
img = cv2.imread(filename)

window = "Window"
# Create a named window
cv2.namedWindow(window)

# Move window to sertain place
cv2.moveWindow(window, 600, 200)

# Percent of original size
scale_percent = 1000
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

# Resize image
resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

# Show image
#cv2.imshow(window, resized)
#print(img)
#cv2.waitKey()
#cv2.destroyAllWindows()

# for line in open(filename, "rb"):
#     if 'END' in line:
# break
#     if 'LINES' in line:
#         # remove trailing newline
#         line = line.rstrip('\n')
#         # extract integer value
#         print int(line.split('=')[1])  # 2240

#pixel checking
pix = img[0][0]
print("pixel:")
print(pix)

#dimensions of picture
shape = img.shape
print("shape:(x,y,color format table size):")
print(shape)

#size
size = img.size
print("size:")
print(size)
print()


#print file in ANSI
file = open(filename, encoding='ANSI')

f2 = file.read()
print(f2)
#result1 = functions.findChunk2(f2)
#print("Wynik findChunk2:",result1)
#result = functions.findChunk(filename)
#print("Wynik:",result)

print()

#print in hex
with open(filename, 'rb') as f:
    hexdata = f.read().hex()

print("hexdata length:",len(hexdata))
print(hexdata)
hexlist = map(''.join, zip(*[iter(hexdata)]*2)) #do a list of 2 char elements, moze sie przydac

newFile = functions.findChunk(filename)
print("zwrocilo !!!!!!!!!!!")



data = bytes.fromhex(hexdata)

with open('newSquare.png', 'wb') as file:
    file.write(data)

file.close()
img = cv2.imread(filename)



