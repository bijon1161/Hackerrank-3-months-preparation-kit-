# -*- coding: utf-8 -*-
"""
Created on Thu Dec 23 21:35:58 2021

@author: Admin
"""

def matrix(n,mat):
    p=0
    q=0
    for i in range(n):
        p+=mat[i][i]
        q+=mat[i][n-i-1]
    print(abs(p-q))

if __name__ == '__main__':
    n=int(input().rstrip())
    mat=[]
    for i in range(n):
        mat.append(list(map(int,input().rstrip().split())))
    matrix(n,mat)
    