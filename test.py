# 项目 ： Python学习
# 姓名 ： 武浩东
# 开发时间 ： 2021/8/20  18:42
import os

import cv2
import numpy as np

# img = cv2.imread("F:\projects\PythonProjects\DL\ThreeHours_openCV\lambo.png")
# cv2.imwrite("qt\img\sys.png",img)
# img1 = cv2.resize(img,(400,600))
# cv2.imshow("img",img1)
# cv2.waitKey(0)
# print(img.shape[0])
# F:\projects\PythonProjects\DL\ThreeHours_openCV\ruiwen.jpg
try:
    img = cv2.imread(r"D:\dailyFiles\picProcess\e4front.png")
    print(img.shape)

    # img1 = img[0:int(img.shape[0]/2),0:int(img.shape[1]/2)]
    # img2 = img[int(img.shape[0]/2):img.shape[0],0:int(img.shape[1]/2)]
    # img3 = img[0:int(img.shape[0]/2),int(img.shape[1]/2):img.shape[1]]
    # img4 = img[int(img.shape[0]/2):img.shape[0],int(img.shape[1]/2):img.shape[1]]

    h = img.shape[0]
    w = img.shape[1]
    img1 = img[0:int(h/3),0:int(w/2)]
    img2 = img[int(h/3):int((h/3)*2),0:int(w/2)]
    img3 = img[int((h/3)*2):h,0:int(w/2)]
    img4 = img[0:int(h/3),int(w/2):w]
    img5 = img[int(h/3):int((h/3)*2),int(w/2):w]
    img6 = img[int((h/3)*2):h,int(w/2):w]

    # imgCanny = cv2.Canny(img, 100, 200)
    # cv2.imshow("img", img)
    # cv2.imshow("Canny", imgCanny)
    # cv2.imwrite("F:\projects\PyCharmProjects\img_process\qt\img\original\imgCanny.png", imgCanny)
    # kernel = np.ones((3, 3), np.uint8)  # 统一类型 np.uint8
    # imgDialation = cv2.dilate(imgCanny, kernel, iterations=1)
    # imgErode = cv2.erode(imgDialation, kernel, iterations=1)
    cv2.imshow("img1", img1)
    cv2.imwrite("D:\dailyFiles\picProcess\img1.png", img1)
    cv2.imwrite("D:\dailyFiles\picProcess\img2.png", img2)
    cv2.imwrite("D:\dailyFiles\picProcess\img3.png", img3)
    cv2.imwrite("D:\dailyFiles\picProcess\img4.png", img4)
    cv2.imwrite("D:\dailyFiles\picProcess\img5.png", img5)
    cv2.imwrite("D:\dailyFiles\picProcess\img6.png", img6)
    cv2.waitKey(0)
except Exception as e:
    print(e)
