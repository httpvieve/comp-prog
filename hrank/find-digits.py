import math
import os
import random
import re
import sys

def findDigits(n):
    div_ctr = 0
    for digit in str(n):
        if int(digit) > 0:
            if n % int(digit) == 0:
                div_ctr += 1
    return div_ctr

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        result = findDigits(n)
        fptr.write(str(result) + '\n')
    fptr.close()
