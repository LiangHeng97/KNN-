# -*- coding: utf-8 -*-
#pip install numpy
import os
import os.path
from numpy import *
import operator
import time
from os import listdir

"""
描述：
    KNN算法实现分类器
参数：
    inputPoint：测试集
    dataSet：训练集
    labels：类别标签
    k:K个邻居
返回值：
    该测试数据的类别
"""
def classify(inputPoint,dataSet,labels,k):
    dataSetSize = dataSet.shape[0]	 #已知分类的数据集（训练集）的行数
    #先tile函数将输入点拓展成与训练集相同维数的矩阵，再计算欧氏距离
    diffMat = tile(inputPoint,(dataSetSize,1))-dataSet  #样本与训练集的差值矩阵

    # print(inputPoint);
    sqDiffMat = diffMat ** 2	#sqDiffMat 的数据类型是nump提供的ndarray,这不是矩阵的平方，而是每个元素变成原来的平方。
    sqDistances = sqDiffMat.sum(axis=1)		 #计算每一行上元素的和
    # print(sqDistances);
    distances = sqDistances ** 0.5			  #开方得到欧拉距离矩阵
    # print(distances);
    sortedDistIndicies = distances.argsort()	#按distances中元素进行升序排序后得到的对应下标的列表,argsort函数返回的是数组值从小到大的索引值
    # print(sortedDistIndicies);

    # classCount数据类型是这样的{0: 2, 1: 2}，字典key：value
    classCount = {}
    # 选择距离最小的k个点
    for i in range(k):
        voteIlabel = labels[ sortedDistIndicies[i] ]
        # print(voteIlabel)
        # 类别数加1
        classCount[voteIlabel] = classCount.get(voteIlabel,0)+1
    print(classCount)# {1: 1, 7: 2}
    #按classCount字典的第2个元素（即类别出现的次数）从大到小排序
    sortedClassCount = sorted(classCount.items(), key = operator.itemgetter(1), reverse = True)
    print(sortedClassCount)# [(7, 2), (1, 1)]
    return sortedClassCount[0][0]

"""
描述：
    读取指定文件名的文本数据，构建一个矩阵
参数：
    文本文件名称
返回值：
    一个单行矩阵
"""
def img2vector(filename):
  returnVect = []
  fr = open(filename)
  for i in range(32):
    lineStr = fr.readline()
    for j in range(32):
      returnVect.append(int(lineStr[j]))
  return returnVect

"""
描述：
    从文件名中解析分类数字，比如由0_0.txt得知这个文本代表的数字分类是0
参数：
    文本文件名称
返回值：
    一个代表分类的数字
"""
def classnumCut(fileName):
    fileStr = fileName.split('.')[0]
    classNumStr = int(fileStr.split('_')[0])
    return classNumStr

"""
描述：
    构建训练集数据向量，及对应分类标签向量
参数：
    无
返回值：
    hwLabels：分类标签矩阵
    trainingMat：训练数据集矩阵
"""
def trainingDataSet():
    hwLabels = []
    trainingFileList = listdir('trainingDigits')		   #获取目录内容
    m = len(trainingFileList)
    # zeros返回全部是0的矩阵，
    trainingMat = zeros((m,1024))						  #m维向量的训练集
    for i in range(m):
        # print (i);
        fileNameStr = trainingFileList[i]
        hwLabels.append(classnumCut(fileNameStr))
        trainingMat[i,:] = img2vector('trainingDigits/%s' % fileNameStr)
    return hwLabels,trainingMat

"""
描述：
    主函数，最终打印识别了多少个数字以及识别的错误率
参数：
    无
返回值：
    无
"""
def handwritingTest():
    """
    hwLabels,trainingMat 是标签和训练数据，
    hwLabels 是一个一维矩阵，代表每个文本对应的标签（即文本所代表的数字类型）
    trainingMat是一个多维矩阵，每一行都代表一个文本的数据，每行有1024个数字（0或1）
    """
    hwLabels,trainingMat = trainingDataSet()	#构建训练集
    testFileList = listdir('testDigits')		#获取测试集
    errorCount = 0.0							#错误数
    mTest = len(testFileList)				   #测试集总样本数
    t1 = time.time()
    for i in range(mTest):
        fileNameStr = testFileList[i]
        classNumStr = classnumCut(fileNameStr)
        # img2vector返回一个文本对应的一维矩阵，1024个0或者1
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        #调用knn算法进行测试
        classifierResult = classify(vectorUnderTest, trainingMat, hwLabels, 3)
        # 打印测试出来的结果和真正的结果，看看是否匹配
        print ("the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr))
        # 如果测试出来的值和原值不相等，errorCount+1
        if (classifierResult != classNumStr):
            errorCount += 1.0
    print("\nthe total number of tests is: %d" % mTest)			   #输出测试总样本数
    print ("the total number of errors is: %d" % errorCount	)	   #输出测试错误样本数
    print ("the total error rate is: %f" % (errorCount/float(mTest)))  #输出错误率
    t2 = time.time()
    print ("Cost time: %.2fmin, %.4fs."%((t2-t1)//60,(t2-t1)%60)	)  #测试耗时

"""
描述：
    指定handwritingTest（）为主函数
"""
if __name__ == "__main__":
  handwritingTest()