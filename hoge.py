# -*- coding: utf-8 -*-
from kuku_list import get_kuku_list
import math

def r_shift(n, i):
    tmp = 10**i
    return int((n-n%tmp)/tmp)

def get_last(n):
    return int(str(n)[-1])

def list_to_int(array):
    ans = 0
    for i in range(len(array)):
        ans += array[i] * 10**i    
    return ans

p = 701
q = 941

n_ori = p*q

kuku_list = get_kuku_list()



list_index = []
flag = False
math.sqrt(n_ori)

a = 0
b = 0


n = r_shift(n_ori - a*b, 0)
##1桁目
tmp_list_1 = kuku_list[get_last(n)]
for i in range(len(tmp_list_1)):
    a = tmp_list_1[i][0]
    b = tmp_list_1[i][1]
    
    if a*b == n:
        flag = True
        
        
    for j in range(1, int(math.sqrt(n_ori/10))):
        if n % (a + j*10) == 0 :
            a += j*10
            print(a)
            print(int(n/a))
            flag = True
            break
            
        if n % (b + j*10) == 0:
            b += j*10
            flag = True
            print(int(n/b))
            print(b)
            break
    
    if flag:
        break

        
        
    
    
    

    
    

