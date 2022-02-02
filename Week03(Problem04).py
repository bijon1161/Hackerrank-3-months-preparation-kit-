# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 12:15:10 2022

@author: Admin
"""
import math
def socksMerchant(n,arr):
    s=list(set(arr))
    
    res=0
    for i in range(len(s)):
        x=(arr.count(s[i]))
        res+=math.floor(x/2)
    return res

if __name__=="__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    print(socksMerchant(n,arr))
    