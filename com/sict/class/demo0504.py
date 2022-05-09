import cv2

img = cv2.imread("D:\\demo1\\demo.jpg")
rows,columns,channels = img.shape
# M矩阵中，第一个参数为旋转中心，第二个为旋转角度（45度），第三个为旋转后的缩放因子。
# 这三个参数以及窗口大小需要根据实际合理调整，以防旋转后超出边界。
M=cv2.getRotationMatrix2D((columns/2,rows/2),45,0.6)
dst = cv2.warpAffine(img,M,(2*columns,2*rows))
while(1):
    cv2.imshow('dst',dst)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()