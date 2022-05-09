import cv2
img=cv2.imread("D:\\demo1\demo.jpg")
#参数None本来是输出图像的尺寸，但后面我设置了缩放因子。
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
height,width=img.shape[:2]
#直接设置输出图像尺寸，无需设置缩放因子。
res2 = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
while(1):
    cv2.imshow('res', res)
    cv2.imshow('img', img)
    cv2.imshow('res2',res2)
    if cv2.waitKey(1) & 0xFF==27:
        break
cv2.destroyAllWindows()