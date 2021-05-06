# -*- coding: utf-8 -*-

def kuku_list():
    zero = []
    one = []
    two = []
    three = []
    four = []
    five = []
    six = []
    seven = []
    eight = []
    nine = []


    for i in range(10):
        for j in range(10):
            tmp = i*j %10
            data = [i, j] 
            if tmp == 0:
                zero.append(data)
            elif tmp == 1:
                one.append(data)
            elif tmp == 2:
                two.append(data)
            elif tmp == 3:
                three.append(data)
            elif tmp == 4:
                four.append(data)
            elif tmp == 5:
                five.append(data)
            elif tmp == 6:
                six.append(data)
            elif tmp == 7:
                seven.append(data)
            elif tmp == 8:
                eight.append(data)
            else:
                nine.append(data)

            kuku= {0: zero, 1: one, 2: two, 3: three, 4: four, 5: five,
                   6: six, 7:seven,8: eight, 9: nine}
            return kuku
kuku = kuku_list()