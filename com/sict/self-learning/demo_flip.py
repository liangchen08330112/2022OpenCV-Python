import cv2
img=cv2.imread("D:\\demo1\\flower.jpeg")
cv2.imshow("original",img)
while True:
    key=cv2.waitKey()
    if key==48:               #按0显示原图
        img2=img
    elif key==49:
        img2=cv2.flip(img,0)  #按1垂直翻转
    elif key==50:
        img2-cv2.flip(img,1)  #按2水平翻转
    elif key==51:
        img2=cv2.flip(img,-1) #按3垂直、水平翻转
    cv2.imshow("img2",img2)
    if key ==27:              #按下Esc关闭所有窗口
        cv2.destroyAllWindows()
