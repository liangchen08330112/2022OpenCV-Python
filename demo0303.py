#读取图片，返回图片的b,g,r三通道的值
import cv2;
img=cv2.imread('D:/image/demo2.jpg')
print(img.shape)
px = img[201,127]
print(px)
blue = img[201,127,0]
print(blue)
green = img[201,127,1]
print(green)
red = img[201,127,2]
print(red)