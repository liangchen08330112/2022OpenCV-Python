import cv2
img=cv2.imread("D:\\demo1\\flower.jpeg")
cv2.imshow("BGR",img)
img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)   #转换为RGB
cv2.imshow("RGB",img2)
cv2.waitKey()
cv2.destroyAllWindows()