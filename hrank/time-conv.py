def timeConversion(s):
        hr = int(s[0])*10 + int(s[1])
        if hr > 12:
                s[0] = str(int((hr - 12) / 10))
                s[1] = str((hr - 12) % 10)
                s += 'PM'
        else : 
                s += 'AM'

s = input()
print(timeConversion(s))

import math
import os
import random
import re
import sys

def timeConversion(s):
    time = ""
    if s[8] == "P":
            hr = (int(s[0]) + 1)*10 + int(s[1]) + 2
            time += str(hr)
    for i in range (2, len(s) - 2):
        time += s[i]
    return time

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = timeConversion(s)
    fptr.write(result + '\n')
    fptr.close()
