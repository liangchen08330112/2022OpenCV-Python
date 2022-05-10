import cv2
import numpy as np
# 透视变换矫正照片
img = cv2.imread('D:\\demo1\\book.jpg')
rows,columns,ch = img.shape
print(img.shape)
pts1=np.float32([[44,32],[241,30],[6,316],[268,323]])
pts2=np.float32([[5,32],[268,32],[6,316],[287,323]])

M=cv2.getPerspectiveTransform(pts1,pts2)

dst=cv2.warpPerspective(img,M,(columns,rows))
cv2.imshow("dst",dst)
cv2.waitKey()
cv2.destroyAllWindows()