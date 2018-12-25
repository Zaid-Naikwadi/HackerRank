#problem statement link: https://www.hackerrank.com/challenges/ctci-ransom-note/forum?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#you can use hash tables instead

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    flag = 0

    for i in note:
        try:
            magazine.pop(magazine.index(i))
        except ValueError:
            flag=1
            break

    if(flag):
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
