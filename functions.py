#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:09:35 2021

@author: chabane
"""

import numpy, time, random
import config
    
def find_neigboorSpins(lattice, pos_x, pos_y):
    L = len(lattice)
#    
    nn1 = lattice[(pos_x+1)%L][(pos_y)%L]
    nn2 = lattice[(pos_x)%L][(pos_y-1)%L]
    nn3 = lattice[(pos_x)%L][(pos_y+1)%L]
    nn4 = lattice[(pos_x-1)%L][(pos_y)%L]
    
    nn_list = [nn1, nn2, nn3, nn4]
    return nn_list


def metropolis(lattice, J, beta):
    random.seed(time.time())
    L = len(lattice)
    N = numpy.power(L, 2)
    
    for i in range(N):
        pos_x, pos_y = numpy.random.randint(0, L), numpy.random.randint(0, L)
        nn_spins = sum(find_neigboorSpins(lattice, pos_x, pos_y))
        
        dE = 2*J*lattice[pos_x][pos_y]*nn_spins
        
        if dE <= 0:
            lattice[pos_x][pos_y] = -1*lattice[pos_x][pos_y]
        else:
            tprob = numpy.exp(-beta*dE)
            rprob = numpy.random.random()
            if rprob <= tprob:
                lattice[pos_x][pos_y] = -1*lattice[pos_x][pos_y]
        
        lattice[pos_x][pos_y] = lattice[pos_x][pos_y]
    return lattice

def Lsquared(init_lattice, sweep_max, J):
    
    #mag_per_sweep = numpy.zeros(sweep_max)
    mag_T = []
    beta_arr = numpy.linspace(0, 1, 8)
    
    for beta in beta_arr:
        for sweep in range(1, sweep_max):
            lattice = metropolis(init_lattice, J, beta)
        
            c = config.SpinConfiguration(lattice)
    
        #print(c.get_magnetization())
            
        #config_lattice = c.get_configuration()
        
        #mag_per_sweep[sweep] = c.get_magnetization()
        print("Sweep.. ", beta)
    
    
        
    return beta_arr, mag_T























#def metropolis(lattice, J, beta):
#    random.seed(time.time())
#    L = len(lattice)
#    #N = numpy.power(L, 2)
#    
#    pos_x, pos_y = numpy.random.randint(0, L), numpy.random.randint(0, L)
#    nn_spins = sum(find_neigboorSpins(lattice, pos_x, pos_y))
#    
#    dE = 2*J*lattice[pos_x][pos_y]*nn_spins
#        
#    if dE <= 0:
#        lattice[pos_x][pos_y] = -1*lattice[pos_x][pos_y]
#    else:
#        tprob = numpy.exp(-beta*dE)
#        rprob = numpy.random.random()
#        if rprob <= tprob:
#            lattice[pos_x][pos_y] = -1*lattice[pos_x][pos_y]
#    
#    lattice[pos_x][pos_y] = lattice[pos_x][pos_y]
#    return lattice