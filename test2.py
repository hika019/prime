# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:12:07 2021

@author: hikar
"""

def kuku_create():
    
    for i in range(10):
        for j in range(10):
            ans = i * j
            kuku_list.append([i, j, ans - int(ans/10)*10])
     
kuku_list = []
kuku_create()

p = 1087
q = 1274
n = p*q

n_lis = []
x_lis=[]
y_lis = []

n_lis.append(n -int(n/10)*10)
#検索↓
#x = p
x_lis.append(7)
y_lis.append(4)

#x,yともに素数判定and 素因数分解できたかチェック
n=int(n/10)- int(x_lis[0] * y_lis[0]/10)


n_lis.append(n -int(n/10)*10)
x_lis.append(8)
y_lis.append(7)
#x1 * y0 + x0 * y1 = n1

n =int(n/10) - int((x_lis[1]*y_lis[0] + x_lis[0]*y_lis[1])/10)


n_lis.append(n -int(n/10)*10)
x_lis.append(0)
y_lis.append(2)

