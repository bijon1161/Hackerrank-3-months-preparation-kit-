# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:03:36 2021

@author: Admin
"""
def splitString(s1):
    if s1[2]=="M":
        met=""
        for i in range(4,len(s1)-2):
            if s1[i] >= 'A' and s1[i] <= 'Z':
                met=met+" "+chr(ord(s1[i])+32)
                
                continue
            met+=s1[i]
        print(met.rstrip())
    elif s1[2]=="C":
        met=chr(ord(s1[4])+32)
        for i in range(5,len(s1)):
            if s1[i] >= 'A' and s1[i] <= 'Z':
                met=met+" "+chr(ord(s1[i])+32)
                
                continue
            met+=s1[i]
        print(met.rstrip())
    else:
        met=""
        for i in range(4,len(s1)):
            if s1[i] >= 'A' and s1[i] <= 'Z':
                met=met+" "+chr(ord(s1[i])+32)
                
                continue
            met+=s1[i]
        print(met.rstrip())
                
def combString(c1):
    c2=""
    if c1[2]=="V":
        
        
        for i in range(4,len(c1),1):
            if c1[i]==" ":
                c2+=""
                continue
            if c1[i-1]==" ":
                c2+=chr(ord(c1[i])-32)
                continue
            
            c2+=c1[i]
        print(c2.rstrip())
    elif c1[2]=="C":
        c2=chr(ord(c1[4])-32)
        for i in range(5,len(c1)):
            if c1[i]==" ":
                c2+=""
                continue
            if c1[i-1]==" ":
                c2+=chr(ord(c1[i])-32)
                continue
            
            c2+=c1[i]
        print(c2.rstrip())
    else:
        
        
        for i in range(4,len(c1),1):
            
            if c1[i]==" ":
                c2+=""
                continue
            if c1[i-1]==" ":
                c2+=chr(ord(c1[i])-32)
                continue
            
            c2+=c1[i]
            
        print(c2+"()".rstrip())
        
        
    
    
if __name__=="__main__":
    while True:
        try:
            st=input().rstrip()
            if st[0]=="S":
                splitString(st)
            elif st[0]=="C":
                combString(st)
            else:
                break
        except (EOFError):
            break
    