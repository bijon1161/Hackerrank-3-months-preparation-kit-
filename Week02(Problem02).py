# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 12:52:38 2021

@author: Admin
"""

def grade(lis):
    
    
    for i in range(len(lis)):
        if lis[i]<38:
            print(lis[i])
        else:
            
                if lis[i]%5==1 or lis[i]%5==2 or lis[i]%5==0:
                    print(lis[i])
                else:
                    if lis[i]%5==3:
                        print(lis[i]+2)
                    elif lis[i]%5==4:
                        print(lis[i]+1)
       
    
                
            
if __name__ == '__main__':
    n = int(input())
    grades=[]
    for _ in range(n):
        grades_item = int(input().strip())
        grades.append(grades_item)
        
    grade(grades)
                