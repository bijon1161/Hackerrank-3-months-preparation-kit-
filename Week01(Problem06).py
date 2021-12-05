# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 00:31:31 2021

@author: Admin
"""

def divSumPairs(n,k,s):
    cou=0
    for i in range(0,len(s)):
        for j in range(i+1,len(s)):
            if (s[i]+s[j])%k==0:
                cou+=1
            else:
                continue
    print(cou)


if __name__ == '__main__':
    n,k, = list(map(int,input().split()))
    s =list(map(int,input().split()))
    divSumPairs(n,k,s)