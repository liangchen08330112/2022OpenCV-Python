import cv2
import numpy as np
img = cv2.imread('D:\\demo1\\shapes.png')
cv2.imshow('original',img)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                        #转灰度
ret,img2=cv2.threshold(gray,125,255,cv2.THRESH_BINARY)             #二值化阈值
c,h = cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #查找轮廓
img3 = np.zeros(img.shape,np.uint8)+255                            #按原图大小创建一个白色图像
img3 = cv2.drawContours(img3,c,-1,(0,0,255),2)                     #绘制轮廓
cv2.imshow('Contours',img3)                                        #显示轮廓图像
for n in range(len(c)):
    m=cv2.moments(c[n])
    print('轮廓%s的矩：'%n,m)                                        #输出矩
    print('轮廓%s的面积：'%n,['m00'])                                #输出面积
cv2.waitKey()
cv2.destroyAllWindows()