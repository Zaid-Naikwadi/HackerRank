#problem statement link: https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#This problem can be solve using Bubble sort, but will fail some Test cases saying timout for big numbers as Bubble sort is slow
#Therefore the solution is to use optimized version of Bubble sort

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    n = len(q)
    cnt=0
    arr = {i:0 for i in q}

    # Traverse through all array elements 
    for i in range(n): 
        swapped = False
  
        # Last i elements are already 
        #  in place 
        for j in range(0, n-i-1): 
   
            # traverse the array from 0 to 
            # n-i-1. Swap if the element  
            # found is greater than the 
            # next element 
            if q[j] > q[j+1] :
                cnt+=1 
                if(arr[q[j]]<2):
                    arr[q[j]]+=1
                else:
                    print("Too chaotic")
                    return
                q[j], q[j+1] = q[j+1], q[j] 
                swapped = True
  
        # IF no two elements were swapped 
        # by inner loop, then break 
        if swapped == False: 
            break

    print(cnt)


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
