# -*- coding: utf-8 -*-

'''
  Copyright(c) 2018, YangLiu.
  All rights reserved.
  2018/2/24
'''
import matplotlib.pyplot as plt
import numpy as np
import csv

filepath = r'I:\liuyang\program\2018\cifar10-tensorflow-resnet\resnet-in-tensorflow-master\resnet-in-tensorflow-master\logs_test_110\test_110_error.csv'
#filepath = r'I:\liuyang\program\2018\cifar10-tensorflow-vgg\logs_vgg\vgg_error.csv'
x_data =[]
train_error = []
vali_error = []
with open(filepath, 'r') as f:
    index = 0
    for line in f.readlines():
        index +=1
        if index>6:
            temp = [ele for ele in line.strip().split(',')]
            x_data.append(int(temp[1]))
            train_error.append(float(temp[2]))
            vali_error.append(float(temp[3]))


plt.plot(x_data, train_error, 'r--',label='train_error')
plt.plot(x_data, vali_error, 'r-', label='vali_error')
plt.grid(True)
plt.legend(loc='upper right')
plt.title('train_error and vali_error of cifar10 in ResNet_32 network')
#plt.title('train_error and vali_error of cifar10 in vgg_19 network')
plt.show()