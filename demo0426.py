import cv2

origin = cv2.imread("D:\\demo2\\img\\demo.jpg")
print(origin.shape[:2])
cv2.imshow("origin", origin)

dst = cv2.pyrDown(origin)
print(dst.shape[:2])
cv2.imshow("dst",dst)

dst1 = cv2.pyrDown(dst)
print(dst1.shape[:2])
cv2.imshow("dst1",dst1)

dst2 = cv2.pyrUp(dst1)
print(dst2.shape[:2])
cv2.imshow("dst2",dst2)

dst3 = cv2.pyrUp(dst2)
print(dst2.shape[:2])
cv2.imshow("dst3",dst3)

cv2.waitKey()
cv2.destroyAllWindows()