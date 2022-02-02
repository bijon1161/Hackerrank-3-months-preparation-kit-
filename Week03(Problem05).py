# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 21:23:32 2022

@author: Admin
"""
def migratoryBirds(arr):
    p=list(set(sorted(arr)))
    m=[]
    ma=0
    for i in range(len(p)):
        m.append(arr.count(p[i]))
        ma=max(m[i],ma)
    q=m.index(ma)
    return p[q]

if __name__ == '__main__':
    n=int(input())
    arr=list(map(int,input().split()))
    print(migratoryBirds(arr))