#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:24:33 2021

@author: chabane
"""

# compositon = "has" relationship
# inhertance = "is" relationship

import numpy 

class Lattice:
    def __init__(self, L):
        self.L = L
        self.lattice = numpy.zeros((self.L, self.L), dtype=(int)) 
        # after init_lattice method -> it will always same value
        
    def init_lattice(self):
        # initalization for T = 0 or beta = inf
        lat_init = self.lattice
        for i in range(self.L):
            for j in range(self.L):
                lat_init[i][j] = -1
        return lat_init

# contains spinconfigurations of the system 
class SpinConfiguration:
    def __init__(self, config_mat):
        self.config_mat = config_mat
        self.N = len(config_mat)**2
    
    def get_configuration(self):
        return self.config_mat
    
    def get_magnetization(self):
        mag_abs = numpy.absolute(self.config_mat)
        return numpy.mean(mag_abs)

class Observables:
    def __init__(self, config_mat):
        self.config_mat = config_mat
    
    def get_magnetization(self):
        mag = 0
        for row in range(self.config_mat):
            for col in range(self.config_mat):
                mag += self.config_mat[row][col]
        return mag
                
    def get_energy(self):
        pass
    def get_specificHeat(self):
        pass
    def get_suscebility(self):
        pass
    
    
#print(numpy.arange(1,4.2, 0.2))