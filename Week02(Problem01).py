<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:12:19 2021

@author: Admin
"""

def checkElem(s):
    for i in range(0,len(s)):
        if s.count(s[i])!=2:
            print(s[i])
        else:
            continue

if __name__ == '__main__':
    n=int(input())
    s=list(map(int,input().split()))
=======
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 21:12:19 2021

@author: Admin
"""

def checkElem(s):
    for i in range(0,len(s)):
        if s.count(s[i])!=2:
            print(s[i])
        else:
            continue

if __name__ == '__main__':
    n=int(input())
    s=list(map(int,input().split()))
>>>>>>> c9bcb8b911bcd46cc5cace4c5a997be1df098a52
    checkElem(s)