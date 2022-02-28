import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos_counter = 0
    neg_counter = 0
    zero_counter = 0
    result = [0,0,0]
    for i in range (0, len(arr)):
        if arr[i] < 0:
            neg_counter += 1
        elif arr[i] > 0:
            pos_counter += 1
        else:
            zero_counter += 1
    result[0] = float(pos_counter/len(arr))
    result[1] = float(neg_counter/len(arr))
    result[2] = float(zero_counter/len(arr))
    
    for k in range(0, 3):
        print(result[k])
    

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    plusMinus(arr)
