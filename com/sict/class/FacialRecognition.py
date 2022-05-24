import cv2
import numpy as np
from PIL import Image

# 调用并开启电脑自带默认摄像头
# 如果想调用外接摄像头，则需要将0改成其他值。
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
def getFace(img):
    # 加载人脸识别模型。代码中提及的xml文件在项目的解释器环境中自带。解释器环境所处的位置请自查。
    # 初期我在GitHub上下载了xml文件，但运行时出现报错。
    face_cascade  = cv2.CascadeClassifier('D:\\2022OpenCV-Python\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    face_cascade.load('D:\\2022OpenCV-Python\\venv\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')
    # 图像二值化转灰度
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # 获取人脸识别数据，可一次识别多个人脸。
    # 1.3：人脸识别范围大小
    # 5：两个人脸之间需要有多大的距离才能都被识别到。
    face = face_cascade.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in face:
        # 绘制人脸识别数据
        # 调用矩形方法，(x,y)指矩形左上方的坐标，(x+w,y+h)指左上方的坐标加上宽度，加上高度，即可定义整个矩形的大小。
        # (255,0,0)指画刷的颜色，2指画刷的粗细
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    return img
# 为识别的人像加贴纸
# 生成视频
# 保存的视频格式为avi，编码格式为MJPG，帧率为15（可以改，帧率越大视频越流畅，反之越卡顿，但也会影响视频占用大小），(1000,563)指视频的宽高。
videoWriter = cv2.VideoWriter('D:\\demo1\\FacialRecognition.avi',cv2.VideoWriter_fourcc(*'MJPG'),15,(1000,563))
# 判断视频是否成功打开，如果成功打开则进入循环
while(cap.isOpened()):
    ret,frame = cap.read()
    if ret == True:
        # 重新定义图片大小
        img = cv2.resize(frame,(1000,563))
        # 实时识别人脸
        img = getFace(img)
        # 显示视频画面
        cv2.imshow('video',img)
        #保存视频
        videoWriter.write(img)
        # 循环每进行一次，就检测Q键是否被按下。
        if cv2.waitKey(10) & 0xFF == ord('q'):
            print("关闭视频")
            # 停止捕获和生成视频，跳出循环，执行下一步
            break
        # 摄像头如果未成功打开，跳出循环，执行下一步。
    else:
        break
# 释放摄像头，停止生成视频并关闭所有窗口。
cap.release()
videoWriter.release()
cv2.destroyAllWindows()