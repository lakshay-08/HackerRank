"""
Capitalize!
"""


import math
import os
import random
import re
import sys

def solve(s):
    l1=[]
    s=s.replace(" "," * ")
    l=s.split()
    for i in l:
        if i.isalpha():
          l1.append(i.capitalize())
        else:
          l1.append(i)
    return(("".join(l1).replace("*"," ")))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()