# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 20:06:21 2021

@author: Admin
"""

def sos(s):
    p=0
    for i in range(0,len(s),3):
        if s[i]!="S":
            p+=1
        if s[i+1]!="O":
            p+=1
        if s[i+2]!="S":
            p+=1
    print(p)


if __name__ == '__main__':
    s=input()
    sos(s)