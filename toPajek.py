#-*.*-coding:utf-8-*.*-#
import matplotlib.pyplot as plt
import math
import numpy as np
import pandas as pd
import networkx as nx
'''读取有权网络的边。TXT文件分隔符为'\t',存入一个list中'''
fl = pd.read_csv('temp.txt', header=None, sep='\t')
mat = np.zeros((fl.shape[0], fl.shape[1]))
for row in range(fl.shape[0]):
    for col in range(fl.shape[1]):
        mat[row][col] = fl[row][col]
# print(mat)
FG = nx.from_numpy_matrix(mat)
nx.write_pajek(FG, '01.net')