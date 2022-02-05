# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 21:45:10 2022

@author: Admin
"""

def maximumPerimeterTriangle(sticks):
    s = sorted(sticks,reverse=True)
    for i in range(len(sticks)-2):
        if(s[i] < s[i+1] + s[i+2]):
            print(s[i+2],end=" ")
            print(s[i+1],end=" ")
            print(s[i],end=" ")
            return 0
    print(-1)

if __name__=='__main__':
    s=int(input())
    sticks=list(map(int,input().split()))
    maximumPerimeterTriangle(sticks)