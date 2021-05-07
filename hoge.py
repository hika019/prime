# -*- coding: utf-8 -*-
from kuku_list import get_kuku_list
import math, time

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

p = 2147483647
q = 20211109

n_ori = p*q

kuku_list = get_kuku_list()



list_index = []
flag = False
math.sqrt(n_ori)

a = 0
b = 0
n = n_ori
tmp_list_1 = kuku_list[get_last(n)]

sqrt= int(math.sqrt(n))

start = time.time()
for i in range(1, int(sqrt/10)):
    for j in range(len(tmp_list_1)):
        
        a= i*10 + tmp_list_1[j][0]
        b= i*10 + tmp_list_1[j][1]
        
        
        if n%a == 0:
            print(a)
            print(int(n/a))
            flag= True
            break
        
        if n%b == 0:
            print(int(n/b))
            print(b)
            flag = True
            break
    if flag:
        print(time.time()-start)
        break


print("")
start = time.time()
for i in range(3, int(math.sqrt(n_ori)), 2):
    if n_ori % i ==0:
        print(i)
        print(int(n_ori/i))
        print(time.time() - start)
        break
    
    
    

    
    

