#matchTemplate多目标匹配

import cv2
import numpy as np

img_rgb = cv2.imread('D:\\demo1\\SuperMario.jpg')
img_gray = cv2.cvtColor(img_rgb,cv2.COLOR_BGR2GRAY)
template = cv2.imread('D:\\demo1\\MarioC.jpg',0)
#shape方法返回的是多位列表的行数、列数。对应图像的高度y、宽度x
print(template.shape)
w,h = template.shape[::-1]
print(w)
print(h)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where(res>=threshold)
#并行遍历
for pt in zip(*loc[::-1]):
    #图像坐标点(x,y)，正好就是元组
    cv2.rectangle(img_rgb,pt,(pt[0]+w,pt[1]+h),(0,0,255),1)
cv2.imshow('img_rgb',img_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()