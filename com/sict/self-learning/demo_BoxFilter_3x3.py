import cv2
img = cv2.imread("D:\\demo1\\lady.jpg")
cv2.imshow("Original",img)
img2 = cv2.boxFilter(img,-1,(3,3),normalize=False)  #卷积大小3×3
cv2.imshow("BoxFilter",img2)
cv2.waitKey()
cv2.destroyAllWindows()