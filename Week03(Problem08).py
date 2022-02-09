# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:52:45 2022

@author: Admin
"""
import math

def pageTurnCount(n,p):
    if p%2==0:
        p=p+1
    return int(min(((p-1)/2),math.ceil((n-p)/2)))

if __name__=="__main__":
    n=int(input())
    p=int(input())
    print(pageTurnCount(n,p))