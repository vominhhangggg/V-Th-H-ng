# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 15:18:07 2024

@author: ADMIN
"""
import math
a = float(input("nhập a: "))
b = float(input("nhập b: "))
c = float(input("nhập c: "))
delta = b*b - 4*a*c
if delta < 0:
    print("phương trình vô nghiệm") 
elif delta == 0:
    print("phương trình có nghiệm kép x1 = x2 = ", -(b / 2*a))
else:
    x1 = ( - b + math.sprt(delta)) / 2*a
    x2 = ( - b - math.sprt(delta)) / 2*a
    print("phương trình có nghiệm x1: ", x1)
    print("phương trình có nghiệm x2: ", x2)