import math
import os
import random
import re
import sys

def gradingStudents(grades):
    final = []
    for i in range (0, len(grades) ):
        n = int(grades[i]/5)*5 + 5
        if (n - grades[i] < 3) and (grades[i] > 37):
            final.append(n)
        elif grades[i] < 38:
            final.append(grades[i])
        else:
            final.append(grades[i])
    return final

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    grades_count = int(input().strip())
    grades = []
    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)
    result = gradingStudents(grades)
    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
