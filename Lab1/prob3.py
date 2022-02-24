# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 16:30:34 2022

@author: anamm
"""

P=int(input("Input Principal Amount : "))
R=float(input("Input Interest Rate : "))
T=float(input("Input Time(In Years) : "))
def compound_interest_2018_2_60_107(P, R, T):
    A=P*(pow((1+R/100),T))
    CI = A-P
    print("Compound interest is", CI)
compound_interest_2018_2_60_107(P,R,T)