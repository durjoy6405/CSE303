# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:38:49 2022

@author: anamm
"""
list1=[2,58,64,89,78,9,52,60]
list2=[51,99,100,2,35,36,48,50]
newlist=[]
for i in list1:
    if (i%2!=0):
        newlist.append(i)
for i in list2:
    if (i%2==0):
        newlist.append(i)
print(newlist)
