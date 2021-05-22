#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:01:44 2021

@author: chabane
"""
import numpy, random, time
class Lattice:
    def __init__(self, L):
        self.L = L
    
    def init_lattice(self):
        return numpy.ones((self.L, self.L), dtype=(int))

def metropolis(mat, L):
    random.seed(time.time())
    pos_x = numpy.random.randint(0, L)
    pos_y = numpy.random.randint(0, L)
    mat[pos_x][pos_y] = 99
    return mat    

N = 10
l = Lattice(10)
l1 = metropolis(l.init_lattice(), 10)
print(l1)