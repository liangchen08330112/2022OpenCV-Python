import cv2
import numpy as np
img = np.zeros((200,320,3),np.uint8)               #创建黑色图像
cv2.rectangle(img,(20,20),(300,180),(255,0,0),5)   #画绿色矩形
cv2.rectangle(img,(70,70),(250,130),(0,255,0),-1)  #画蓝色矩形边框
cv2.imshow('rectangle',img)
cv2.waitKey()
cv2.destroyAllWindows()