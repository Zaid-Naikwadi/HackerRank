#problem statement link: https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    sum=0;
    arr1 = [[0 for x in range(4)] for y in range(4)]
    
    for i in range(0,4):
        for j in range(0,4):
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if (k-i)==1 and (l-j)!=1:
                        continue
                    sum = sum + arr[k][l]
            
            arr1[i][j] = sum
            sum=0

    maxNum = arr1[0][0]
    for i in range(0,4):
       if(maxNum < max(arr1[i])):
           maxNum = max(arr1[i])

    return maxNum
                       


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
