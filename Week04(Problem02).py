# -*- coding: utf-8 -*-
"""
Created on Thu Sep  1 07:52:35 2022

@author: Admin
"""

def rotateLeft(d, arr):
     result = [0] * len(arr)
     for i in range(len(arr)):
        result[i - d] = arr[i]
     return result
 
    
if __name__ == '__main__':
     n,d = list(map(int,input().split()))
     a = list(map(int,input().split()))
     print(rotateLeft(d,a))