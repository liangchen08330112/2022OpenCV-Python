import cv2

#Sobel边缘检测
img = cv2.imread('D:\\demo1\\flower.jpeg')
cv2.imshow('original',img)
img2 = cv2.Laplacian(img,cv2.CV_8U,0,1)
cv2.imshow('Sobel',img2)
cv2.waitKey()
cv2.destroyAllWindows()