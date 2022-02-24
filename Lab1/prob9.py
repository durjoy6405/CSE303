# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:42:21 2022

@author: anamm
"""
List= [17,35,57,81,123,5,62,28]
def largest_number_2018_2_60_107(List):
    max=List[0]
    for element in List:
        if element>max :
             max=element
    return max

def smallest_number_2018_2_60_107(List):
    min=List[0]
    for element in List:
        if element<min :
             min=element
    return min

print("Largest element in the list is:",largest_number_2018_2_60_107(List))
print("Smallest element in the list is:",smallest_number_2018_2_60_107(List))