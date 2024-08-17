# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:37:41 2024

@author: pc
"""

# Bài tập tính tiền taxi
d=float(input("Nhap so km quang đuong đi đuoc: "))
if d >= 0:
    if d <= 1 : 
        tongtien = 20 
    elif d <= 3:
        tongtien = 20 + 13*(d-1) 
    elif d <= 8 :
        tongtien = 20 + 13*(d-1) + 12*(d-3) 
    else:
        tongtien = 20 + 13*(d-1) + 12*(d-3) + 10*(d-8) 
    if tongtien >= 100 :
        tongtien = tongtien*(1 - 8/100)
    print(f"Tong tien taxi la: {tongtien:.0f}k")
else:
    print("Khong xac dinh")
    
