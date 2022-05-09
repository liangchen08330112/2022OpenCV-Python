#中值模糊
import cv2
src = cv2.imread("D:\\demo1\\demo.jpg")
dst = cv2.medianBlur(src,3)
cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()