# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 17:17:45 2024

@author: ADMIN
"""

import random

print("Chào mừng bạn đến với trò chơi kéo - búa - bao!")
nguoi_chon=input("Nhập lựa chọn của bạn:")
if nguoi_chon not in ["kéo", "búa", "bao"]:
    print("Lỗi. Mời nhập lại")
else:
    print("Người chơi chọn:", nguoi_chon)
may_chon=random.choice(["kéo", "búa", "bao"])
print("Máy chọn:", may_chon)
if nguoi_chon==may_chon: 
    print("Hòa")
elif (nguoi_chon=='kéo' and may_chon=='bao') or (nguoi_chon=='búa' and may_chon=='kéo') or (nguoi_chon=='bao' and may_chon=='búa'):
    print("Bạn thắng")
elif (may_chon=='kéo' and nguoi_chon=='bao') or (may_chon=='búa' and nguoi_chon=='kéo') or (may_chon=='bao' and nguoi_chon=='búa'):
    print("Máy thắng")
else:
    print("Người chọn nhập sai, không có kết quả")