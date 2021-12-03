#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 22:42:05 2021

@author: walberto

Advent of code 2021, day 2
"""

# unpaking data
file = open('input.txt')
lines = file.readlines()
file.close()

# Original position
x,y = 0,0

# part 2
qAim, qx, qy = 0,0,0

for data in lines:
    data_1 = data.split()
    text = data_1[0]
    num = int(data_1[1])
    
    if text == 'forward':
        x += num
        qx += num
        qy += qAim*num
    
    elif text == 'down':
        y += num
        qAim += num
    
    elif text == 'up':
        y -= num
        qAim -= num
        
print('part 1 = ',x*y)
print('part 2 = ',qx*qy)