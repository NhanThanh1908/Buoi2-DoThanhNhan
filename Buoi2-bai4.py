# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:19:57 2024

@author: pc
"""

a=float(input("Nhap canh a:"))
b=float(input("Nhap canh b:"))
c=float(input("Nhap canh c:"))
if a+b>c and b+c>a and a+c>b:
    print("3  abc tao thanh tam giac")
else:
    print("3 canh abc khong tao thanh tam giac")
if a==b==c:
    print("Tam giac abc la tam giac deu")
elif a==b or a==c or b==c:
    print("Tam giac abc la tam giac can")
elif a**2+b**2==c**2 or a**2+c**2==b**2 or b**2+c**2==a**2:
    print("Tam giac abc la tam giac vuong")
else:
    print("Tam giac abc la tam giac thuong ")
