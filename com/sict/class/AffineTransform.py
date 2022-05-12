import cv2
import numpy as np

img = cv2.imread("D:\\demo1\\opencvbook.jpg")
rows,columns,ch = img.shape
print(img.shape)
pts1=np.float32([[81,509],[125,90],[451,523]])
pts2=np.float32([[79,523],[79,65],[451,523]])
M=cv2.getAffineTransform(pts1,pts2)
dst=cv2.warpAffine(img,M,(columns,rows))
cv2.imshow("dst",dst)
cv2.waitKey(20000)
cv2.destroyAllWindows()