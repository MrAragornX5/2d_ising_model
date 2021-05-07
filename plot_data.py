#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 18:42:10 2021

@author: chabane
"""

import DataSet, numpy
import matplotlib.pyplot as plt

def plot_mean(data_array, N):
    mean_array = numpy.zeros(N)
    
    data = DataSet.DataSet(data_array)
    for i in range(N):
        mean_array[i] = data.calc_mean(i)
    
    fig1 = plt.figure()
    plt.title(r"Markov-Chain for $N$ = " + str(N))
    plt.grid(b=True, which='major', color='#666666', linestyle='--')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)
    plt.xlabel(r'$N$')
    plt.ylabel(r"$\langle x\rangle$")


    plt.plot(mean_array, 
             #marker="1", 
             color= "navy", 
             label = r"Sample-Mean: $\frac{1}{N}\sum_i f(x_i)$")
    plt.legend(loc='best')
    #fig1.savefig('test.pdf', dpi=300, bbox_inches='tight')
    
def plot_naive_error(data_array, N):
    naive_error = numpy.zeros(N)
    
    data = DataSet.DataSet(data_array)
    for i in range(N):
        naive_error[i] = data.calc_NaiveError(i)
    
    fig1 = plt.figure()
    plt.title(r"Markov-Chain for $N$ = " + str(N))
    plt.grid(b=True, which='major', color='#666666', linestyle='--')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)
    plt.xlabel(r'$N$')
    plt.ylabel(r"$\langle x\rangle$")


    plt.loglog(naive_error, 
             #marker="1", 
             color= "darkred", 
             label = r"Sample-Mean: $\frac{1}{N}\sum_i f(x_i)$")
    plt.legend(loc='best')
    #fig1.savefig('test.pdf', dpi=300, bbox_inches='tight')

