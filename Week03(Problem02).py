# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 11:48:10 2022

@author: Admin
"""

def birthday(s, d, m):
    result=0
    for i in range(0,len(s)):
       if sum(s[i:m+i])==d:
         result+=1
    print(result) 

if __name__ == '__main__':
    s=list(map(int,input().split()))
    d=int(input())
    m=int(input())
    birthday(s,d,m)