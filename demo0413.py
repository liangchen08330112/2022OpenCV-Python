import cv2
img = cv2.imread("D:\\Downloads\\test.png")
imgray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,240,55,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
img = cv2.drawContours(img,contours,4,(0,255,0),3)
print(len(contours))
for i in range(len(contours)):
    epsilon = 0.01*cv2.arcLength(contours[i],True)
    approx = cv2.approxPolyDP(contours[i],epsilon,True)
    print(len(approx))
    if(len(approx)==3):
        print("第",i,"条轮廓是三角形")
    if(len(approx)==4):
        print("第",i,"条轮廓是矩形")
    if(len(approx)==10):
        print("第",i,"条轮廓是五角星")
    if(len(approx)==16):
        print("第",i,"条轮廓是圆形")

cv2.imshow('thresh',thresh)
cv2.imshow('imgray',imgray)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()