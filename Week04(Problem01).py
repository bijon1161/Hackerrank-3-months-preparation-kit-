# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 05:25:55 2022

@author: Bijon
"""

def pickingNumbers(a):
    
    st = set(a)
    m = 0
    for i in st:
        if (a.count(i) + a.count(i-1)> m):
            m = a.count(i) + a.count(i-1)
        elif (a.count(i) + a.count(i+1) > m):
            m = a.count(i) + a.count(i+1)
    print(m)

if __name__ =="__main__":
    n = int(input())
    a = list(map(int,input().split()))
    pickingNumbers(a)