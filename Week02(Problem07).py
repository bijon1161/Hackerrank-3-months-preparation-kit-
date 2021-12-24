# -*- coding: utf-8 -*-
"""
Created on Fri Dec 24 19:42:03 2021

@author: Admin
"""

def pangram(s):
    p="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s=s.upper()
    q=0
    cou=0
    for i in range(len(p)):
        cou=s.count(p[i])
        if cou==0:
            print("not pangram")
            break
        else:
            q+=1
        cou=0
    if q==len(p):
        print("pangram")
    
    

if __name__ == '__main__':
    s=input()
    pangram(s)