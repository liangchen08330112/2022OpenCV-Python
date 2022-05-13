#自适应阈值处理
import cv2
img = cv2.imread("D:\\demo1\\flower.jpeg",cv2.IMREAD_GRAYSCALE)   #将读取到的图片转灰度图
cv2.imshow("Original",img)
img2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,5,10)   #自适应阈值处理
cv2.imshow("img2",img2)
cv2.waitKey()
cv2.destroyAllWindows()