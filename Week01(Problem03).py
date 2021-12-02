# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 16:47:56 2021

@author: Admin
"""

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ap = s[8]+s[9]
    if ap=="AM" or ap=="am":
        if s[0]=="1" and s[1]=="2":
            print("00:"+s[3]+s[4]+s[5]+s[6]+s[7])
        else:
            p=""
            for i in range(0,len(s)-2):
                p+=s[i]
            print(p)
    else:
        if s[0]=="1" and s[1]=="2":
            p=""
            for i in range(0,len(s)-2):
                p+=s[i]
            print(p)
        else:
            c=s[0]+s[1]
            inc= int(c) + 12
            print(str(inc)+s[2]+s[3]+s[4]+s[5]+s[6]+s[7])
            
           
            

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

   # fptr.write(result + '\n')

   # fptr.close()