import cv2
img = cv2.imread("D:\\demo1\\flower.jpeg")
cv2.imshow("Original",img)
img2 = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)  #转换为HSV
cv2.imshow("HSV",img2)
cv2.waitKey()
cv2.destroyAllWindows()