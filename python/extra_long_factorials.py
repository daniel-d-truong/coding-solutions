#https://www.hackerrank.com/challenges/extra-long-factorials/problem
#!/bin/python

#solution works!
import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    if n != 1:
        return n*extraLongFactorials(n-1)
    else:
        return 1

if __name__ == '__main__':
    n = int(raw_input())

    x = extraLongFactorials(n)
    print x
