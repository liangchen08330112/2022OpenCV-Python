import cv2
import numpy as np
img = np.zeros((200,320,3),np.uint8)       #创建黑色图像
cv2.line(img,(0,0),(320,200),(255,0,0),5)  #画第一条对角线，蓝色
cv2.line(img,(320,0),(0,200),(0,255,0),5)  #画第二条对角线，绿色
cv2.imshow('line',img)
cv2.waitKey()
cv2.destroyAllWindows()