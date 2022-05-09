#自定义模糊
import cv2
import numpy as np
#filter2D
src = cv2.imread("D:\\demo1\\demo.jpg")
cv2.imshow('src',src)
kernel = np.array([[0,1/5,0],
                   [1/5,1/5,1/5],
                   [0,1/5,0]])
dst = cv2.filter2D(src,-1,kernel)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()