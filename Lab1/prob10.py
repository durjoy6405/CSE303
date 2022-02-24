# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 22:06:19 2022

@author: anamm
"""
List= [17,35,57,81,123,5,62,28]
def second_largest_number(List):
    max=List[0]
    max2=List[0]
    for element in List:
        if element>max :
            max=element
    
    for element in range(len(List)):
        if List[element]>max2 and List[element]!=max:
            max2=List[element]
    return max2
print("Second largest element in the list is:",second_largest_number(List))