# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:17:49 2022

@author: anamm
"""
str=input("Please enter a string:\n")
def palindrome_cheker_2018_2_60_107(str):
    for i in range(int(len(str))):
        if str[i] != str[len(str)-i-1]:
            print("This string is not a palindrome")
    print("This string is a palindrome")
palindrome_cheker_2018_2_60_107(str)
