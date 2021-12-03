#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 22:41:34 2021

@author: walberto

Advent of code 2021, day 3
"""

from math import ceil

# unpaking data
# file = open('example.txt')
file = open('input.txt')
lines = file.readlines()
file.close()






def bit_fill (data):
    
    size = len(list(data[0].split()[0]))

    bit = []

    for i in range(size):
        bit.append(0)
    
    for num in data:
        sep = list(num.split()[0])
        i = 0
        for ele in sep:
            bit[i] += int(ele)
            i += 1
            
    sign_t = len(data)//2
    
    return(bit, sign_t)
    


def gamma_eps (bit_list):
    
    gamma_out = []
    eps_out = []
    
    zer = '0'
    one = '1'
    
    for ele in bit_list:
        if ele > sign: 
            gamma_out.append(one)
            eps_out.append(zer)
        else:
            gamma_out.append(zer)
            eps_out.append(one)
    
    return(gamma_out,eps_out)
    
    
def Bin_to_decimal(binary):
    
    number = 0
    
    top = len(binary)
    i = 0
    while i < top:
        part = binary.pop()
        
        if (part == '1') or (part == 1):
            number = number + 2**i
        
        i += 1
    return number

# Main (part 1)

bit, sign = bit_fill(lines)

g,e = gamma_eps(bit)

gamma = Bin_to_decimal(g)
eps = Bin_to_decimal(e)
print('part 1 = ', gamma*eps)


# Parte 2

def Oxi_fill (data_temp):
    
    data = data_temp[:]
    
    sign_t = len(data)//2
    
    size = len(list(data[0].split()[0]))

    bit = []

    for i in range(size):
        bit.append(0)
            
    for i in range(size):
        # Esta parte va llenando el bit
        for num in data:
            sep = list(num.split()[0])
            bit[i] += int(sep[i])
        
        
        # Esta parte transforma el bit en el que estamos
        if bit[i] >= sign_t:
            bit[i] = 1
        else:
            bit[i] = 0
        
        # Esta parte quita los elementos que son distintos
        
        dummy_list = []
        for num in data:
            sep = list(num.split()[0])
            if bit[i] == int(sep[i]):
                dummy_list.append(num)
    
        data = dummy_list[:]
        
        # Esta parte para si nos quedamos con un ultimo elemento
        if len(data) == 1: 
            sep = list(data[0].split()[0])
            while i < size:
                bit[i] = int(sep[i])
                i+=1
            
            break
        
        sign_t = ceil(len(data)/2)
        
    
    return(bit)


def Co2_fill (data_temp):
    
    data = data_temp[:]
    
    sign_t = len(data)//2
    
    size = len(list(data[0].split()[0]))

    bit = []

    for i in range(size):
        bit.append(0)
            
    for i in range(size):
        # Esta parte va llenando el bit
        for num in data:
            sep = list(num.split()[0])
            bit[i] += int(sep[i])
        
        # Esta parte transforma el bit en el que estamos
        if bit[i] >= sign_t:
            bit[i] = 0
        else:
            bit[i] = 1
        
        # Esta parte quita los elementos que son distintos
        
        dummy_list = []
        for num in data:
            sep = list(num.split()[0])
            if bit[i] == int(sep[i]):
                dummy_list.append(num)
        

        data = dummy_list[:]
        
        
        # Esta parte para si nos quedamos con un ultimo elemento
        if len(data) == 1: 
            sep = list(data[0].split()[0])
            while i < size:
                bit[i] = int(sep[i])
                i+=1
            
            break
        
        sign_t = ceil(len(data)/2)       
    
    return(bit)

# Main parte 2

O2_bit = Oxi_fill(lines)
Co2_bit = Co2_fill(lines)

ox = Bin_to_decimal(O2_bit)
co2 = Bin_to_decimal(Co2_bit)

print('part 2 = ',ox*co2)