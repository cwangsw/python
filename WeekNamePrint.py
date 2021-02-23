# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 15:35:12 2021

@author: v-shawnwang
"""


weekStr = "SunMonTueWedThuFriSat"
weekId = eval(input("please type the number:"))
pos = (weekId - 1) * 3
print(weekStr[pos : pos + 3])