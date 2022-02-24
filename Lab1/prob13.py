# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 23:37:17 2022

@author: anamm
"""

str=input("Plz Enter a string: ")
sub_str='CSE303'
result=0
sub_len=len(sub_str)
for i in range(len(str)):
    if str[i:i+sub_len]==sub_str:
        result+=1
print(result)