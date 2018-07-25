#!/bin/python3

import math
import os
import random
import re
import sys

'''
[[1, 1, 1, 0, 0, 0],
 [0, 1, 0, 0, 0, 0],
 [1, 1, 1, 0, 0, 0],
 [0, 0, 2, 4, 4, 0],
 [0, 0, 0, 2, 0, 0],
 [0, 0, 1, 2, 4, 0]]

'''


if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0],
     [0, 1, 0, 0, 0, 0],
     [1, 1, 1, 0, 0, 0],
     [0, 0, 2, 4, 4, 0],
     [0, 0, 0, 2, 0, 0],
     [0, 0, 1, 2, 4, 0]]

    print(arr)
    print(arr[0][0],arr[0][1],arr[0][2],arr[0][3])# row
    print(arr[1][0],arr[1][1],arr[1][2],arr[1][3])# row

    print(arr[0][0],arr[1][0],arr[2][0],arr[3][0])#column

    sum_list =[]
    a = []
    b = [_ for _ in range(6)]
    print(b)

    for _ in range(6):
        #arr.append(list(map(int, input().rstrip().split())))
    print(arr)
    maximum = []
    type(arr[0][0:3])
    type(sum(arr[0][0:3]))

    sum(arr[0][0:3]) + sum(arr[1][1]) + sum(arr[2][0:3])


    for x in range(4):
        for y in range(4):
            arr_sum = sum(arr[x][y:y + 3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            maximum.append(str(arr_sum))


    print(maximum)
