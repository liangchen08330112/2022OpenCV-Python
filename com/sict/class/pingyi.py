import numpy as np
import cv2
img = cv2.imread("D:\\demo1\\demo.jpg")
rows, columns, channels = img.shape
# [1,0,100] 右移100；[0,1,50] 下移50。
M = np.float32([[1,0,100],
                [0,1,50]])
res = cv2.warpAffine(img, M, (columns, rows))
cv2.imshow("res",res)
cv2.imshow("img",img)
cv2.waitKey()
cv2.destroyAllWindows()