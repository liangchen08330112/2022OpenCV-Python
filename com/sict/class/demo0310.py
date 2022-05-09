#高斯模糊
import cv2
src = cv2.imread("D:\\demo1\\hehua.jpeg")
dst = cv2.GaussianBlur(src,(9,9),1)
cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()