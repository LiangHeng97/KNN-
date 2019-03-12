# encoding: utf-8
import cv2
from PIL import Image
import numpy as np
import os


def f(IMGNUM):
    ls = os.listdir("testpicture")
    for i in ls:
        c_path = os.path.join("testpicture", i)
        os.remove(c_path)
    ls = os.listdir("testpicture2")
    for i in ls:
        c_path = os.path.join("testpicture2", i)
        os.remove(c_path)

    for i in ls:
        c_path = os.path.join("picture/picture-cut", i)
        os.remove(c_path)

    i=1
    img = cv2.imread(IMGNUM)         #路径可以修改
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰度图像
    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # 将灰度图像转成二值图像

    contours, hierarchy = cv2.findContours(binary,  cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   # 查找轮廓
    cv2.drawContours(img, contours, -1, (0, 0, 255), 3)         #绘图，将图片描边

    cv2.waitKey(0)
    cv2.imwrite("picture/picture-cut/test2.jpg",img)
    img2=Image.open(IMGNUM)      #路径可以修改
    s = img2.size[0] * img2.size[1]         #计算图片总面积

    for i in range(1,len(contours),1):
        if contours[i] is None:
            break
        else:
            leftmin=0
            leftmax=0
            rightmin=0
            rightmax=0
            for i1 in range(len(contours[i])):
                w1=contours[i][i1]
                if leftmin==0:
                    leftmin=w1[0][0]
                if rightmin==0:
                    rightmin=w1[0][1]
                if leftmin>w1[0][0]:
                    leftmin=w1[0][0]
                if leftmax<w1[0][0]:
                    leftmax=w1[0][0]
                if rightmin>w1[0][1]:
                    rightmin=w1[0][1]
                if rightmax<w1[0][1]:
                    rightmax=w1[0][1]
        if abs(leftmax-leftmin)*abs(rightmax-rightmin)>(s/10) and (4*s/5) > abs(leftmax-leftmin)*abs(rightmax-rightmin):
            break
                                                #找到表格部分的对角坐标

    # print(leftmin,rightmin,leftmax,rightmax)

    box=(leftmin,rightmin,leftmax,rightmax)
    newimg=img2.crop(box)
    newimg.save("picture/picture-cut/test3.jpg")

    #处理完表格的第一步切割



    img = cv2.imread('picture/picture-cut/test3.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰度图像
    ret, binary = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)  # 将灰度图像转成二值图像

    contours, hierarchy = cv2.findContours(binary,  cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)   # 查找轮廓

    cv2.waitKey(0)
    cv2.imwrite("picture/picture-cut/test3.jpg",img)
    img2=Image.open('picture/picture-cut/test3.jpg')
    s = img2.size[0] * img2.size[1]         #计算图片总面积
    memory = []
    cm2=1
    mark=0
    sum=0
    for i in range(1,len(contours),1):
        if contours[i] is None:
            break
        else:
            leftmin=0
            leftmax=0
            rightmin=0
            rightmax=0
            for i1 in range(len(contours[i])):
                w1=contours[i][i1]
                if leftmin==0:
                    leftmin=w1[0][0]
                if rightmin==0:
                    rightmin=w1[0][1]
                if leftmin>w1[0][0]:
                    leftmin=w1[0][0]
                if leftmax<w1[0][0]:
                    leftmax=w1[0][0]
                if rightmin>w1[0][1]:
                    rightmin=w1[0][1]
                if rightmax<w1[0][1]:
                    rightmax=w1[0][1]

        if (rightmin > (img2.size[1]/3)) and abs(leftmax-leftmin)*abs(rightmax-rightmin)>(s/20) and (s/6) > abs(leftmax-leftmin)*abs(rightmax-rightmin)  and (leftmax-leftmin)<(img2.size[0]/4):
            memory.append([leftmin, rightmin, leftmax, rightmax])
            mark=mark+1
    def by_leftmin(memory):
        return memory[0]
    memory=sorted(memory,key=by_leftmin)

    for i in range(0,mark):
            leftmin=memory[i][0]
            rightmin=memory[i][1]
            leftmax=memory[i][2]
            rightmax=memory[i][3]
            box = (leftmin, rightmin, leftmax, rightmax)
            sum=sum+1
            newimg = img2.crop(box)
            cm1='picture/picture-cut/'
            cm3='.jpg'
            cm=cm1+str(cm2)+cm3
            newimg.save(cm)
            cm2=cm2+1
    #第二次处理，分割出小图片




    cm2=1
    i4 = 1
    for i3 in range(sum):
        n = 0
        L = []
        M = 0
        cm=cm1+str(i3+1)+cm3
        img = cv2.imread(cm)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 转成灰度图像
        ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # 将灰度图像转成二值图像
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # 查找轮廓

        cv2.waitKey(0)
        cv2.imwrite(cm, img)
        img2 = Image.open(cm)
        s = img2.size[0] * img2.size[1]  # 计算图片总面积

        for i in range(1, len(contours), 1):
            if contours[i] is None:
                break
            else:
                leftmin = 0
                leftmax = 0
                rightmin = 0
                rightmax = 0
                for i1 in range(len(contours[i])):
                    w1 = contours[i][i1]
                    if leftmin == 0:
                        leftmin = w1[0][0]
                    if rightmin == 0:
                        rightmin = w1[0][1]
                    if leftmin > w1[0][0]:
                        leftmin = w1[0][0]
                    if leftmax < w1[0][0]:
                        leftmax = w1[0][0]
                    if rightmin > w1[0][1]:
                        rightmin = w1[0][1]
                    if rightmax < w1[0][1]:
                        rightmax = w1[0][1]
            if abs(leftmax - leftmin) * abs(rightmax - rightmin) > (s / 120) and (2 * s / 3) > abs(leftmax - leftmin) * abs(
                            rightmax - rightmin) and leftmin>0 and rightmax<img2.size[0]:
                L.append([leftmin, rightmin, leftmax, rightmax])
                # print([leftmin, rightmin, leftmax, rightmax])
                n=n+1

        def by_leftmin(t):
             return t[0]

        L = sorted(L, key=by_leftmin)

        ml = []
        mm = 0
        if n>1:
            for c in range(n - 1):
                m = L[c]
                for c2 in range(c+1,n,1):
                    if (m[0]<L[c2][0] and m[2] > L[c2][2]):
                        ml.append(L[c2])
                        mm = mm + 1

            for i in range(mm):
                if ml[i] in L:
                    L.remove(ml[i])
                    n = n - 1

        if n==1:
            box = (L[0])
            newimg = img2.crop(box)
            cm5 = 'testpicture/' + str(i3+1) + cm3
            newimg.save(cm5)
        if n>1:

            box = (L[0])
            newimg = img2.crop(box)
            cm5 = 'testpicture2/' + str(i3+1) + cm3
            newimg.save(cm5)

            box = (L[1])
            newimg = img2.crop(box)
            cm5 = 'testpicture/' + str(i3+1) + cm3
            newimg.save(cm5)



                # 找到表格部分的对角坐标




# f(IMGNUM)