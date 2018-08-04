#https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# Given two strings, determine if they share a common substring. A substring may be as small as one character.
#
# For example, the words "a", "and", "art" share the common substring . The words "be" and "cat" do not share a substring.
#
# Function Description
#
# Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.
#
# twoStrings has the following parameter(s):
#
# s1, s2: two strings to analyze .
# Input Format
#
# The first line contains a single integer , the number of test cases.
#
# The following  pairs of lines are as follows:
#
# The first line contains string .
# The second line contains string .
# Constraints
#
#  and  consist of characters in the range ascii[a-z].
# Output Format
#
# For each pair of strings, return YES or NO.
#
# Sample Input
#
# 2
# hello
# world
# hi
# world
# Sample Output
#
# YES
# NO

#!/bin/python

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the twoStrings function below.
def twoStrings(s1, s2):#Counter object create dictionary that tallies the keys

      char_dict1 = Counter(s1) #putting iterable in Counter object immediately does the tally
      char_dict2 = Counter(s2)

      for i in "abcdefghijklmnopqrstuvwxyz":
        if char_dict1[i] > 0 and char_dict2[i] > 0:
            return "YES"
      return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(raw_input())

    for q_itr in xrange(q):
        s1 = raw_input()

        s2 = raw_input()

        result = twoStrings(s1, s2)

        fptr.write(result + '\n')

    fptr.close()

#solution successful!
