import cv2
import numpy as np
img = np.zeros((200,320,3),np.uint8)+255                 #创建白色图像
cv2.ellipse(img,(160,100),(120,50),0,0,360,(255,0,0),5)  #画椭圆形蓝色边框
cv2.ellipse(img,(160,100),(60,15),0,0,360,(0,255,0),51)  #画绿色椭圆
cv2.imshow('ellipse',img)
cv2.waitKey()
cv2.destroyAllWindows()