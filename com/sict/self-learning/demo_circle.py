import numpy as np
import cv2
img = np.zeros((200,320,3),np.uint8)       #创建黑色图像
cv2.circle(img,(160,100),80,(255,0,0),5)   #画绿色圆形
cv2.circle(img,(160,100),40,(0,255,0),-1)  #画蓝色圆形边框
cv2.imshow('circle',img)
cv2.waitKey()
cv2.destroyAllWindows()