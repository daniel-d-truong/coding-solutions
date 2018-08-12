#https://www.hackerrank.com/challenges/find-digits/problem

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the findDigits function below.
def findDigits(n):
    string = str(n) #makes n into a string
    count = 0 #counts how many digits are divisible with n
    for i in range(len(string)):
        temp_char = string[i] #one single digit
        if int(temp_char) == 0: #avoids n/0 which leads to error
            pass
        elif n % int(temp_char) == 0:
            count+=1
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(raw_input())

    for t_itr in xrange(t):
        n = int(raw_input())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
