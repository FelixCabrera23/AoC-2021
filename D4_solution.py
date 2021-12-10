#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 22:36:52 2021

@author: walberto

Advent of code 2021, day 4
"""

import numpy as np

# unpaking data
# file = open('example.txt')
file = open('input.txt')
lines = file.readlines()
file.close()

dummy_nums = list(lines.pop(0).split(','))
dummy_nums[-1] = dummy_nums[-1].split()[0]

nums_playd = []

for num in dummy_nums:
    nums_playd.append(int(num))
    
    
def fill_mat (nums,boards):
    """
    Esta función llena genera los objetos Board y los mete 
    en una lista
    regresa: lista de objetos Board
    """
    Board_list = []
    
    top = len(boards)
    i = 0
    while i < top:
        i+=1 # hacemos el skip de la primera linea vacia
        Mat = [] #hacemos una matriz vacia
        for j in range(5):
            row = []
            for num in boards[i].split():
                row.append(int(num))
            Mat.append(row)
            i+=1 #Cambiamos de linea en la matriz
            
        
        Board_list.append(Board(Matrix=Mat,nums=nums))
        
    return Board_list
    
    
    
# Hacemos una clase para las boletas para el  juego

class Board(object):
    """
    Estas son las boletas, su parte principal es
    que son matrices de 5 x 5
    """
    
    def __init__(self,Matrix = [] ,win = False,nums = [],turn = 0 ,score = 0, marks = []):
        """
        Propiedades de las boletas
        A = matriz de 5 x 5
        win (bool), true = ganadora, false = no ha ganado
        nums = lista de numeros
        turn = turno en el que gana
        score = puntaje ganador
        """
        
        self.Matrix = Matrix
        self.win = win
        self.nums = nums
        self.turn = turn
        self.score = score
        self.marks = marks
        
    def winer(self):
        """
        Metodo que determina el turno y puntaje con la que
        gana el tablero
        
        Regresa: matriz de marcas, turno
        
        """
        dummy_Mat = np.zeros((5,5),dtype=bool).tolist()
        dummy_matT = np.zeros((5,5),dtype=bool).tolist()
        # tambien se puede usar copy.deepcopy()
        
        Matx = self.Matrix
        
        plays = self.nums
        
        for num in plays:
            # En cada turno marcamos casilla
            for i in range(5):
                for j in range(5):
                    if num == Matx[i][j]:
                        dummy_Mat[i][j] = True
                        dummy_matT[j][i] = True
            
            for line in dummy_Mat:
                if all(line):
                    self.win = True
                    self.turn = plays.index(num)
                    self.marks = dummy_Mat
                    return(dummy_Mat,plays.index(num))
            for row in dummy_matT:
                if all(row):
                    self.win = True
                    self.turn = plays.index(num)
                    self.marks = dummy_Mat
                    return(dummy_Mat,plays.index(num))
                
        return(dummy_Mat,0)
            
        
    def Set_score(self):
        Matx = self.Matrix
        dummy_Mat = self.marks
        nums_ = self.nums
        
        if len(dummy_Mat) < 1:
            return
        
        Score_ = 0
        for i in range(5):
            for j in range(5):
                if not(dummy_Mat[i][j]):
                    Score_ += Matx[i][j]
        
        Score_ = Score_*nums_[self.turn]
        
        return(Score_)
                    
    
# part 1 main

juego = fill_mat(nums_playd,lines)
                    
turns = []
for tab in juego:
    turns.append(tab.winer()[1])

result = juego[turns.index(min(turns))].Set_score()

print(result)
            
    














