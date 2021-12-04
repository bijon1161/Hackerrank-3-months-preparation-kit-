# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 17:46:35 2021

@author: Admin
"""

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecordsMin(scores):
    s1=sorted(scores)
    s=list(dict.fromkeys(s1))
    
    if(s[0]==scores[0]):
        result=0
    
    else:
        p=len(scores)
        ct=0
        mini=scores[0]
        for i in range(1,p):
            
            if mini>scores[i]:
                ct+=1
                mini=scores[i]
                
            else:
                continue
        result=ct
    return result
        
def breakingRecordsMax(scores):   
    s1=sorted(scores)
    s1.reverse()
    s=list(dict.fromkeys(s1))
    
    if(s[0]==scores[0]):
        result=0
    
    else:
        
        p=len(scores)
        ct=0
        maxi=scores[0]
        for i in range(1,p):
            
            if maxi<scores[i]:
                ct+=1
                maxi=scores[i]
                
            else:
                continue
        result=ct
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    p=breakingRecordsMin(scores)
    q=breakingRecordsMax(scores)
    print(q,p)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()
