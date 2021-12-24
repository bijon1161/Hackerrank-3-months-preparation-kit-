# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 10:49:16 2021

@author: Admin
"""
def count(p):
    lis=[0]*100
    for i in range(len(p)):
        lis[p[i]]+=1
    for i in lis: 
        
        print( i,end=" ")

if __name__ == '__main__':
    n=int(input())
    p=list(map(int,input().split()))
    count(p)