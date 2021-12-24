# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 18:40:01 2021

@author: Admin
"""
def check(s):
    p=0
    c=0
    q=0
    for i in s:
        if i=="D":
            p+=1
            if p==0:
                q+=1
        else:
            p-=1
        if p==0:
            c+=1
    print(c-q)


if __name__ == '__main__':
    n=int(input())
    s=input()
    check(s)