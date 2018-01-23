# -*.*-coding:utf-8-*.*- #
import pandas as pd

'''读取有权网络的边。TXT文件分隔符为'\t',存入一个list中'''
fl = pd.read_csv('temp.txt', header=None, sep='\t')

# print(fl)
for i in range(fl.shape[0]):
    for j in range(fl.shape[1]):
        if fl[i][j] and i < j:
            print(i, j, fl[i][j], "Undirected")