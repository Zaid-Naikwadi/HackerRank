#problem statement link: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# instead of calculating min element each time in loop, I optimized by taking already sorted array which made me pass some timeout test cases, but still 2 cases are giving timeout error.

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    n = len(arr)
    cnt=0
    sortedArr = arr.copy()
    sortedArr.sort()

    for i in range(n):
        minIndex = arr.index(sortedArr.pop(0))
        if(minIndex != 0):
            arr[0],arr[minIndex] = arr[minIndex],arr[0]
            cnt+=1
            
        arr.pop(0)
        n-=1   

    return cnt


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
