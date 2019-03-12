import cv2
import os

def f():
        lis = os.listdir('testpicture')
        for i in range(0,len(lis)):
                path = os.path.join("testpicture",lis[i])
                IMG= path
                img = cv2.imread(IMG)
                Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                ret, thresh = cv2.threshold(Grayimg, 100, 255, cv2.THRESH_BINARY)
                cv2.imwrite(IMG, thresh)

        lis = os.listdir('testpicture2')
        for i in range(0,len(lis)):
                path = os.path.join("testpicture2",lis[i])
                IMG= path
                img = cv2.imread(IMG)
                Grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                ret, thresh = cv2.threshold(Grayimg, 100, 255, cv2.THRESH_BINARY)
                cv2.imwrite(IMG, thresh)




# f()



