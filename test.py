# -*- coding: utf-8 -*-


def kuku_create():
    
    for i in range(10):
        for j in range(10):
            ans = i * j
            kuku_list.append([i, j, ans - int(ans/10)*10])
     
kuku_list = []
kuku_create()
p = 37
q = 113
n_ori= p*q

n= n_ori

n0 = n -int(n/10)*10
"""
for i in kuku_list:
    if i[2] == n0:
        print(i)
"""
#とりあえず選択された↓
x0=7
y0=3
#x,yともに素数判定and 素因数分解できたかチェック
n=int(n/10)- int(x0 * y0/10)


n1 = n -int(n/10)*10
"""
for i in kuku_list:
    if i[2] == n1:
        print(i)
"""
#n1になる組み合わせげっと(x1, y1)とする
#x0 * x1 + y0 * y1 = n


x1=3
y1=1
#x,yともに素数判定and 素因数分解できたかチェック

#できなければ↓
n=int(n/10)- int((x1*y0 + x0*y1)/10)


n2 = n -int(n/10)*10
"""
for i in kuku_list:
    if i[2] == n1:
        print(i)
"""
#n1になる組み合わせげっと(x1, y1)とする
#x1 * x1 + y0 * y1 = n

        