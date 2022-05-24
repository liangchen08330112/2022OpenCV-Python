#使用NumPy函数计算直方图
import cv2
import numpy as np
import matplotlib.pyplot as plt
from numpy import ravel

img=cv2.imread("D:\\demo1\\flower.jpeg")
plt.figure('程序运行结果')
rgb=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.subplot(2,2,1)
plt.imshow(rgb)
plt.title('Original')
plt.axis('off')
histb,e1=np.histogram(img[0].ravel(),256,[0,256])
histg,e2=np.histogram(img[1].ravel(),256,[0,256])
histr,e3=np.histogram(img[2].ravel(),256,[0,256])
plt.subplot(2,2,2)
plt.plot(histb,color="b")
plt.plot(histg,color="g")
plt.plot(histr,color="r")
plt.title('hist')
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
H,S,V = cv2.split(img2)
hist,x,y = np.histogram2d(H.ravel(),S.ravel(),[180,256],[[0,100],[0,256]])
plt.subplot(2,1,2)
plt.title('2Dhist')
plt.imshow(hist)
plt.show()