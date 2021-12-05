#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:36:52 2021

@author: walberto

Advent of code 2021, day 4
"""

# unpaking data
file = open('example.txt')
# file = open('input.txt')
lines = file.readlines()
file.close()

dummy_nums = list(lines.pop(0).split(','))
dummy_nums[-1] = dummy_nums[-1].split()[0]

nums_playd = []

for num in dummy_nums:
    nums_playd.append(int(num))
    


    














