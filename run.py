import cv2
import numpy as np

img = cv2.imread('dog.png')

#robienie transformaty
f = np.fft.fft2(img)
magnitude_spectrum = 20*np.log(np.abs(f))
magnitude_spectrum = np.asarray(magnitude_spectrum, dtype=np.uint8)

cv2.namedWindow('magnitude_spectrum', cv2.WINDOW_NORMAL) #umozliwia rozciaganie okna
cv2.imshow('magnitude_spectrum',magnitude_spectrum) #wyswietla transformate
cv2.namedWindow('dog.png', cv2.WINDOW_NORMAL)
cv2.imshow('dog.png',img) #wyswietla obraz
cv2.waitKey(0) #zeby nie zamykalo okna
cv2.destroyAllWindows()



