# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 01:17:41 2021

@author: Admin
"""

def sparseArr(s,qq):
    
    
    for i in range(0,len(qq)):
        co=0
        for j in range(0,len(s)):
            if qq[i]==s[j]:
                co+=1
            else:
                continue
        print(co)
        


if __name__ == '__main__':
    n=int(input())
    s=[]
    for i in range(n):
        s.append(input())
    q=int(input())
    qq=[]
    for i in range(q):
        qq.append(input())
    sparseArr(s,qq)