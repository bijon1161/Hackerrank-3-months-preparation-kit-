# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:25:02 2021

@author: Admin
"""

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    lis=sorted(arr)
    sum=0
   
    for i in lis:
        sum+=i
    print(sum-lis[4],end=" ")
    print(sum-lis[0],end=" ")
        

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)