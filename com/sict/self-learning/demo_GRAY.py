import cv2
img = cv2.imread("D:\\demo1\\flower.jpeg")
cv2.imshow("original",img)
img2= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)  #转灰度
cv2.imshow("GRAY",img2)
cv2.waitKey()
cv2.destroyAllWindows()