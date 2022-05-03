import cv2

origin = cv2.imread("D:\\demo2\\img\\demo2.jpg")

gaosi0 = origin
gaosi1 = cv2.pyrDown(gaosi0)
print(gaosi1.shape[:2])
gaosi2 = cv2.pyrDown(gaosi1)
print(gaosi2.shape[:2])
lapu0 = gaosi0 - cv2.pyrUp(gaosi1)
lapu1 = gaosi1 - cv2.pyrUp(gaosi2)

rep = lapu0 + cv2.pyrUp(lapu1+cv2.pyrUp(gaosi2))
gaosi_rep = cv2.pyrUp(cv2.pyrUp(gaosi2))
cv2.imshow("origin",origin)
cv2.imshow("rep",rep)
cv2.imshow("gaosi_rep",gaosi_rep)
cv2.waitKey()
cv2.destroyAllWindows()