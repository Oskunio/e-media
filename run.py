import cv2
import numpy as np
img = cv2.imread('dog.png')
cv2.namedWindow('dog.png', cv2.WINDOW_NORMAL) #umozliwia rozciaganie okna
cv2.imshow('dog.png',img)
cv2.waitKey(0) #zeby nie zamykalo okna
cv2.destroyAllWindows()



