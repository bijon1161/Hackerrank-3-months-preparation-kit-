# -*- coding: utf-8 -*-
"""
Created on Sat Jan  1 10:02:29 2022

@author: Admin
"""

def permute(num,s1,s2):
    n=num[0]
    k=num[1]
    for i in range(n):
        p=k-s1[i]
        q=[]
        for j in range(0,n-i,1):
            
            if s2[j]>=p:
                q.append(s2[j])
                q.sort()
            
        if len(q)==0:
            print("NO")
            return 0
        s2.remove(q[0])
        q=[]
    print("YES")
        
        

if __name__=='__main__':
    q=int(input())
    for _ in range(q):
        
        num=list(map(int,input().split()))
        s1=list(map(int,input().split()))
        s2=list(map(int,input().split()))
        permute(num,s1,s2)
            