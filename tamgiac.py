# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 16:05:26 2024

@author: ADMIN
"""

a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))
if a + b>c and b + c>a and a + c>b:
    print("Đây là tam giác.")
    if   a == b and b == c:
        print("Đây là một tam giác đều.")
    elif a == b or b == c or a == c:
        print("Đây là một tam giác cân.")
    elif a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a: 
        print("Đây là tam giác vuông.") 
    elif a*a + b*b == c*c and a == b or a*a + c*c == b*b and a == c or b*b + c*c == a*a and b == c:
        print("Đây là tam g vuông cân.")
    else:
        print("Đây là một tam giác thường.")
else:
    print("Không phải là một tam giác.")
    