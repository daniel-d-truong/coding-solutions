#https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#failed attempt at a solution. WILL COME BACK
#!/bin/python

import math
import os
import random
import re
import sys
import collections

# Complete the isValid function below.
def isValid(s):
    dict_values = collections.Counter(s)
    ex = 1 #allows to check if one index can be removed
    list = dict_values.most_common()
    dict_counts = {0: [list[0][0]] }

    key = 0
    index = 1
    while index < len(list):
        if list[index][1] != list[index-1][1]:
            key+=1
            if (abs(list[index][1] - list[index-1][1]) > 1):
                return "NO"
            dict_counts[key] = [ ]
        dict_counts[key].append(list[index][0])
        index+=1

    print dict_counts
    if len(dict_counts[0]) < 2 or len(dict_counts[1])<2:
        return "YES"

    else:

        while key > 1:

        return "NO"


#     count=list[0][1]
#     count2=list[1][1]

#     print list
#     if (count==count2):
#         constant = count
#         for item in list:
#             temp_count = item[1]
#             if temp_count < constant:
#                 sub = constant-temp_count
#                 # count = temp_count
#                 ex-=sub
#                 print ("ex-1")

#             elif temp_count > constant:
#                 return "NO"

#             if ex<0:
#                 return "NO"
#         return "YES"

#     elif (abs(count-count2) == 1):
#         count3=list[2][1]
#         if count == count3:
#             constant = count
#         elif count2 == count3:
#             constant = count2
#         else:
#             return "NO"

#         ex-=1
#         index=2

#         while (index < len(list)):
#             print list[index]
#             if list[index][1] != constant:
#                 print "ITS THIS"
#                 return "NO"
#             index+=1
#         return "YES"

#     else:
#         return "NO"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
