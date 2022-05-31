import cv2
import numpy as np
origin = cv2.imread("D:\\demo1\\zhong.png")
cv2.imshow("Original",origin)
kernel = np.ones((5,5),np.uint8)    #定义大小为5×5的内核
img2 = cv2.dilate(origin,kernel,iterations=3)   #膨胀，迭代3次
cv2.imshow('img2',img2)
cv2.waitKey()
cv2.destroyAllWindows()