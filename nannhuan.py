# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:15:37 2024

@author: ADMIN
"""

a = float(input("Nhập năm: "))
if a % 400 == 0 or a % 4 == 0 and a % 100 == 0 :
    print("Năm nhuận.")
else:
    print("Không phải năm nhận.")
