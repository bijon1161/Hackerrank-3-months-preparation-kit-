# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:48:10 2022

@author: Admin
"""

def birthday(s, dm):
    d=dm[0]
    m=dm[1]
    result=0
    for i in range(0,len(s)):
       if sum(s[i:m+i])==d:
         result+=1
    print(result) 

if __name__ == '__main__':
    n=int(input())
    s=list(map(int,input().split()))
    dm=list(map(int,input().split()))
    
    birthday(s,dm)