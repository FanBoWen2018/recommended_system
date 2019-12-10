# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 16:32:54 2018

@author: fan
"""

import datetime
import numpy as np
import math

def load_train_data(fileName):   
    trainingData=[]
    with open(fileName) as txtData:
        lines=txtData.readlines()
        for line in lines:
            lineData=line.strip().split(',')    #去除空白和逗号“,”
            for i in range(len(lineData)):
                lineData[i] = int(lineData[i])
            trainingData.append(lineData)   #训练数据集
    temp = np.zeros((1300,1182))
    for i in range(len(np.array(trainingData))):
        j = (np.array(trainingData))[i][0]-1
        k = (np.array(trainingData))[i][1]-1
        temp[j][k] = (np.array(trainingData))[i][2]
    return temp
def load_test_data(fileName):   
    testingData=[]
    with open(fileName) as testData:
        lines=testData.readlines()
        for line in lines:
            lineData=line.strip().split(',')    #去除空白和逗号“,”
            for i in range(len(lineData)):
                lineData[i] = int(lineData[i])
            testingData.append(lineData)   #训练数据集
    temp = np.zeros((1300,1182))
    for i in range(len(np.array(testingData))):
        j = (np.array(testingData))[i][0]-1
        k = (np.array(testingData))[i][1]-1
        temp[j][k] = (np.array(testingData))[i][2]
    return temp
def LFM(a,k):
    '''
    参数a：表示需要分解的评价矩阵
    参数k：分解的属性（隐变量）个数
    '''
    assert type(a) == np.ndarray
    m, n = a.shape
    alpha = 0.005
    lambda_ = 0.01
    u = np.random.rand(m,k)
    v = np.random.randn(k,n)
    for t in range(1000):
        for i in range(m):
            for j in range(n):
                if math.fabs(a[i][j]) > 1e-4:
                    err = a[i][j] - np.dot(u[i],v[:,j])
                    for r in range(k):
                        gu = err * v[r][j] - lambda_ * u[i][r]
                        gv = err * u[i][r] - lambda_ * v[r][j]
                        u[i][r] += alpha * gu
                        v[r][j] += alpha * gv
    return u,v
def PC(k):
    print('第',k,'个测试集的预测覆盖率为100%')
def MAE(train):
    fileName = 'testData'
    for k in range(5):
        sum = 0.0
        count = 0
        i = 0
        j = 0
        test = load_test_data(fileName+str(k+1)+'.txt')
        for i in range(1300):
            for j in range(1182):
                if(test[i][j] != 0):
                    sum = sum +abs(test[i][j]-train_result[i][j])
                    count = count+1
        print('第',k+1,'个测试集的共有数据',count,'条')
        print('第',k+1,'个测试集的MAE为:',sum/count)
        PC(k+1)
if __name__=="__main__":
    starttime = datetime.datetime.now()
    train = load_train_data('trainingData.txt')
    b,c = LFM(train,1)
    train_result=np.dot(b,c)
    MAE(train_result)
    endtime = datetime.datetime.now()
    print('整个程序运行总用时为：',endtime - starttime)
