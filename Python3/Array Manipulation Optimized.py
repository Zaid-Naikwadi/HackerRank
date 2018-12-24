#problem statement link: https://www.hackerrank.com/challenges/crush/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for i in range(n+1)]
    maxNum = x = 0

    for opr in queries:
        arr[opr[0]-1]+=opr[2]
        if(opr[1]<=len(arr)): arr[opr[1]]-=opr[2]
    
    for i in arr:
        x=x+i;
        if(maxNum<x):
            maxNum=x
    
    return maxNum

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
