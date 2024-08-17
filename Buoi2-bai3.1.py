# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:44:43 2024

@author: pc
"""

a=float(input("Nhap gia tri a:"))
b=float(input("Nhap gia tri b:"))
if a==0:
    print("Phuong trinh vo nghiem")
elif a>0:
    print("Phuong trinh co nghiem la ",-b/a)
else:
    print("Phuong trinh co nghiem la ",b/a)
    