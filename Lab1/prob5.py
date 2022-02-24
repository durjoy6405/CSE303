# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:01:20 2022

@author: anamm
"""
import math
N=int(input("Please Enter any Positive Number: "))
def prime_find_2018_2_60_107(N):
    flag=False
    if(N==1):
        flag=True
    for i in range(2,math.ceil(N/2)):
        if(N%i==0):
            flag=True
            break
    if flag:
        print(N,"is not a prime number")
    else:
        print(N,"is a prime number")

prime_find_2018_2_60_107(N)
    
        
            
            
        