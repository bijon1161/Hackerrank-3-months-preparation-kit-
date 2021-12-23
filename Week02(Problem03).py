# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 10:17:17 2021

@author: Admin
"""

# Python program to convert decimal to binary

# Function to convert Decimal number
# to Binary number
def decimalToBinary(lis):
    
    for i in range(len(lis)):
      n=bin(lis[i]).replace("0b", "")
      p=n.zfill(32)
      q=""
      
      for i in range(32):
          if p[i]=="0":
              q+="1"
          else:
              q+="0"
      print(int(q,2))
      
      

# Driver code

    
if __name__ == '__main__':
    n = int(input())
    lis=[]
    for _ in range(n):
        s=int(input().strip())
        lis.append(s)
    decimalToBinary(lis)
        
          
        
        
