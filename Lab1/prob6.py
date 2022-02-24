# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 20:54:39 2022

@author: anamm
"""
N=int(input("Enter any Positive Number: "))
def Fibonacci(N):
    if N<= 0:
        print("Incorrect input")
    elif N== 1:
        return 0
    elif N== 2:
        return 1
    else:
        return Fibonacci(N-1)+Fibonacci(N-2)
 
print(Fibonacci(N))
