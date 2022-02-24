# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 22:15:38 2022

@author: anamm
"""
str=input("Enter String:\n")
print("\nCharacters are present in even index:\n")
for index in range(1,len(str),2):
    print(str[index] )
