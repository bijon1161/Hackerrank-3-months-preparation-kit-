# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:03:36 2021

@author: Admin
"""
def splitString(s1):
    if s1[2]=="M":
        met=""
        for i in range(4,len(s1)-6):
            if s1[i] >= 'A' and s1[i] <= 'Z':
                s1[i]=chr(ord(s1[i])+32)
                met=met+" "+s1[i]
                continue
            met+=s1[i]
        print(met)
    elif s1[2]=="C":
        met=s1[0]+32
        for i in range(5,len(s1)-5):
            if s1[i] >= 'A' and s1[i] <= 'Z':
                s1[i]=chr(ord(s1[i])+32)
                met=met+" "+s1[i]
                continue
            met+=s1[i]
        print(met)
    else:
        met=""
        for i in range(4,len(s1)-4):
            if s1[i] >= 'A' and s1[i] <= 'Z':
                s1[i]=s1[i]+32
                met=met+" "+s1[i]
                continue
            met+=s1[i]
        print(met)
                
def combString(c1):
    if c1[2]=="V":
        
        met=""
        for i in range(4,len(c1)-4):
            if c1[i]==" ":
                c1[i+1]=c1[i+1]-32
                continue
            met+=c1[i]
        print(met)
    elif c1[2]=="C":
        met=c1[0]-32
        for i in range(5,len(c1)-5):
            if c1[i]==" ":
                c1[i+1]=c1[i+1]-32
                continue
            met+=c1[i]
        print(met)
    else:
        met=""
        for i in range(4,len(c1)-4):
            if c1[i]==" ":
                c1[i+1]=c1[i+1]-32
                continue
            met+=c1[i]
        print(met+"()")
        
        
    
    
if __name__=="__main__":
    stri=input()
    if stri[0]=="S":
        splitString(stri)
    elif stri[0]=="C":
        combString(stri)
    