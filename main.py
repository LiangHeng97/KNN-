#-*- coding: utf-8 -*-
from numpy import *
import operator
import os
from os import listdir
import operatepicture
import tonumber
import denoising



def f():
    def classify(inputPoint,dataSet,labels,k):
        dataSetSize = dataSet.shape[0]     #已知分类的数据集（训练集）的行数
        #先tile函数将输入点拓展成与训练集相同维数的矩阵，再计算欧氏距离
        diffMat = tile(inputPoint,(dataSetSize,1))-dataSet  #样本与训练集的差值矩阵
        sqDiffMat = diffMat ** 2                    #差值矩阵平方
        sqDistances = sqDiffMat.sum(axis=1)         #计算每一行上元素的和
        distances = sqDistances ** 0.5              #开方得到欧拉距离矩阵
        sortedDistIndicies = distances.argsort()    #按distances中元素进行升序排序后得到的对应下标的列表
        #选择距离最小的k个点
        classCount = {}
        for i in range(k):
            voteIlabel = labels[ sortedDistIndicies[i] ]
            classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
        #按classCount字典的第2个元素（即类别出现的次数）从大到小排序
        sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
        return sortedClassCount[0][0]


    #文本向量化 32x32 -> 1x1024
    def img2vector(filename):
        returnVect = []
        fr = open(filename)
        for i in range(32):
            lineStr = fr.readline()
            for j in range(32):
                returnVect.append(int(lineStr[j]))
        return returnVect

    #从文件名中解析分类数字
    def classnumCut(fileName):
        fileStr = fileName.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        return classNumStr

    def classnumCut1(fileName):
        fileStr = fileName.split('.')[0]
        classNumStr = int(fileStr.split('_')[1])
        return classNumStr


        #构建训练集数据向量，及对应分类标签向量
    def trainingDataSet():
            hwLabels = []
            trainingFileList = listdir('trainingDigits')           #获取目录内容
            m = len(trainingFileList)
            trainingMat = zeros((m,1024))                          #m维向量的训练集
            for i in range(m):
                fileNameStr = trainingFileList[i]
                hwLabels.append(classnumCut(fileNameStr))
                trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
            return hwLabels,trainingMat

    #测试函数
    def handwritingTest():
        each= [0]*20
        sum =0
        maxnum=1
        hwLabels,trainingMat = trainingDataSet()    #构建训练集
        testFileList = listdir('testDigits1')        #获取测试集
        errorCount = 0.0                            #错误数
        mTest = len(testFileList)                   #测试集总样本数
        for i in range(mTest):
            fileNameStr = testFileList[i]
            classNumStr = classnumCut(fileNameStr)
            vectorUnderTest = img2vector('testDigits1/%s' % fileNameStr)
            #调用knn算法进行测试
            classifierResult = classify(vectorUnderTest, trainingMat, hwLabels, 3)
            sum+=classifierResult*classNumStr
            # print "the classifier came back with: %d" % (classifierResult)
            each[classnumCut1(fileNameStr) ]=classifierResult*classNumStr+each[classnumCut1(fileNameStr) ]
            if(classnumCut1(fileNameStr) >maxnum):
                maxnum=classnumCut1(fileNameStr )
            if (classifierResult != classNumStr): errorCount += 1.0
        print "the total score is: %d" % sum
        for i in range(1, maxnum+1):
            # print ("第%d题的分数：%d\t" %(i ,each[i]))
            print "NO.%d: %d"%(i,each[i])
            if(i== maxnum): print'\n'



    if __name__ == "__main__":
        handwritingTest()

# t1= time.time()
# operatepicture.f()
# denoising.f()
# tonumber.f()
# f()
# t2 = time.time()
# print "Cost time: %.2fmin, %.4fs."%((t2-t1)//60,(t2-t1)%60)      #测试耗时

lis = os.listdir('picture/picture')
for i in range(0, len(lis)):
    path = os.path.join("picture/picture", lis[i])
    IMGNAME = path
    # print ("图片："+IMGNAME).decode("utf-8").encode("gb2312")
    print "picture: "+ IMGNAME
    operatepicture.f(IMGNAME)
    denoising.f()
    tonumber.f()
    f()

