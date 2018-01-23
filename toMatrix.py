'''邻接矩阵'''
import numpy as np
import xlrd
import networkx as nx

data = xlrd.open_workbook('step1.xlsx')
table = data.sheets()[0]
m, n = table.nrows, table.ncols
# i = j = 0
s = t = i = 0
flag = 0

# print(m,n)
def cell(x, y):
    return table.cell(x, y).value

ss = set()
for i in range(m):
    for j in range(n):
        if cell(i, j) != "":
            ss.add(cell(i, j))
lst = [i for i in range(len(ss))]
lst1 = list(ss)
print(lst1)
''''''
arr = np.zeros((len(ss), len(ss)))
np.set_printoptions(threshold=np.NaN)
while s < m:
    while t < n and cell(s, t) != "":
        while i < n and cell(s, i) != "":
            if i != t and cell(s, t) != cell(s, i):
                ii, jj = lst1.index(cell(s, t)), lst1.index(cell(s, i))
                # print(ii,jj)
                arr[ii][jj] += 1
                # arr[jj][ii] += 1
            i = i + 1
        i = 0
        t = t + 1
    t = 0
    s = s + 1
for ff in range(arr.shape[0]):
    for gg in range(arr.shape[0]):
        print(int(arr[ff][gg]), end='\t')
    print()
