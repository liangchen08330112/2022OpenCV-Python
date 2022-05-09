import cv2
import numpy as np
img=np.zeros((200,320,3),np.uint8)                             #创建一幅黑色图像
pts=np.array([[160,20],[20,100],[160,180],[300,100]],np.int32) #创建顶点
cv2.polylines(img,[pts],True,(255,0,0),5)                      #画蓝色边框多边形
cv2.imshow('polylines',img)
cv2.waitKey()
cv2.destroyAllWindows()