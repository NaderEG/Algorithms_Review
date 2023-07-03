#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    newGrades = [0]*len(grades)
    for i in range(len(grades)):
        if math.ceil((grades[i]/5))*5 - grades[i] < 3 and grades[i] > 37:
            newGrades[i] = math.ceil((grades[i]/5))*5
        else:
            newGrades[i] = grades[i]
    return newGrades

if __name__ == '__main__':
    fptr = sys.stdout

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
