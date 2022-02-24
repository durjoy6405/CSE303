# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:22:51 2022

@author: anamm
"""
total_even_indexed_value=0
List= [17,35,57,81,123,5,62,28]
for element in range(1, len(List),2):
    
    total_even_indexed_value+=List[element]

print("Sum of the List: ", total_even_indexed_value)
