import cv2
import numpy as np
img = cv2.imread("D:\\demo1\\flower.jpeg")
cv2.imshow('Original',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
kernel = np.ones((3,3),np.uint8)
open = cv2.morphologyEx(thresh,cv2.MORPH_OPEN,kernel,iterations=2)
dist = cv2.distanceTransform(open,cv2.DIST_L2,5)
cv2.imshow('distance',dist)
cv2.waitKey()
cv2.destroyAllWindows()