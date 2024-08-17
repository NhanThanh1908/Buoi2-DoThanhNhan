# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 12:55:48 2024

@author: pc
"""

x=float(input("Nhap do dai doan duong den truong (m):"))
if x<300:
        print("Duong den truong qua gan. Thoi! Di bo")
elif x>1200:
        print("Duong den truong qua xa. Thoi! Di xe may")
elif x>=300 and x<=700:
        print("Duong den truong khong xa. Thoi! Di xe dap")
else:
        print("Khong xac dinh")
a=float(input("Nhap diem GPA:"))
if a<3.5:
        print("Hoc luc kem")
elif a>=3.5 and a<5:
        print("Hoc luc yeu")
elif a>=5 and a<7:
        print("Hoc luc trung binh")
elif a>=7 and a<8:
        print("Hoc luc kha")
elif a>=8 and a<9:
        print("Hoc luc gioi")
elif a>=9 and a<10:
        print("Hoc luc xuat sac")
else:
        print("Khong xac dinh")

        

        