#均值模糊
import cv2
src = cv2.imread("D:\\demo1\\hehua.jpeg")
dst = cv2.blur(src,(3,3)),
cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()