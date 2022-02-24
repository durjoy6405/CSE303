# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 22:46:26 2022

@author: anamm
"""
N=int(input("Enter A number:"))
str1=input("Enter String:")

new_str=""
for i in range(len(str1)):
    if (i>N):
        new_str = new_str + str1[i]
print ("The string after removal",N," upto character(s) : ",new_str)