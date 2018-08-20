#https://www.hackerrank.com/challenges/save-the-prisoner/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the saveThePrisoner function below.
def saveThePrisoner(n, m, s):
    prisoner = (m + s - 1) % n
    if prisoner == 0:
        prisoner = n
    return prisoner


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        nms = raw_input().split()

        n = int(nms[0]) #num of prisoners

        m = int(nms[1]) #num of treats

        s = int(nms[2]) #prisoner start

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
