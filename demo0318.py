#Canny边缘提取
import cv2
def edge(image):
    blurred = cv2.GaussianBlur(image,(3,3),0)
    gray = cv2.cvtColor(blurred,cv2.COLOR_BGR2GRAY)
    edge_output = cv2.Canny(gray,50,150)
    cv2.imshow("Canny Edge",edge_output)
    dst = cv2.bitwise_and(image,image,mask=edge_output)
    cv2.imshow("Color Edge",dst)
src = cv2.imread("D:\\demo1\\demo3.jpg")
cv2.imshow('input image',src)
edge(src)
cv2.waitKey(0)
cv2.destroyAllWindows()