# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 09:58:57 2021

@author: Admin
"""

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    pos=0
    ct1=0
    neg=0
    ct2=0
    zer=0
    ct3=0
    lis=len(arr);
    for list in arr:
        if list>0:
            pos+=list
            ct1+=1
        elif list==0:
            zer+=list;
            ct3+=1
        else:
            neg+=list
            ct2+=1
    print(ct1,ct2,ct3)
    print("{0:.6f}".format(ct1/lis))
    print("{0:.6f}".format(ct2/lis))
    print("{0:.6f}".format(ct3/lis))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)