#三角阈值算法处理
import cv2
img = cv2.imread("D:\\demo1\\flower.jpeg",cv2.IMREAD_GRAYSCALE)   #将读取到的图片转灰度图
cv2.imshow("Original",img)
ret,img2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)   #只二值化
cv2.imshow("img2",img2)
ret,img3 = cv2.threshold(img,127,255,cv2.THRESH_BINARY+cv2.THRESH_TRIANGLE)   #二值化+三角阈值
cv2.imshow("img3",img3)
ret,img4 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV+cv2.THRESH_TRIANGLE)   #反二值化+三角阈值
cv2.imshow("img4",img4)
cv2.waitKey()
cv2.destroyAllWindows()