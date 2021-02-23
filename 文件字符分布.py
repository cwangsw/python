# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 16:11:19 2021

@author: v-shawnwang
"""


f = open("latex.log")
count = 0
d = dict()
for i in range(26):
    d[chr(ord('a') + i)] = 0
for line in f:
    for c in line:
        d[c] = d.get(c, 0) + 1
        count += 1
print("共{}字符".format(count), end="")
for i in range(26):
    if d[chr(ord('a') + i)] != 0:
        print(",{}:{}".format(chr(ord('a')+i), d[chr(ord('a')+i)]), end="")