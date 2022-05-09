import cv2
img = cv2.imread('D:\\demo1\\shapes.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,img2 = cv2.threshold(gray,125,255,cv2.THRESH_BINARY)
c,h = cv2.findContours(img2,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
for n in range(len(c)):
    m = cv2.contourArea(c[n])
    print('轮廓%s的面积：'%n,m)