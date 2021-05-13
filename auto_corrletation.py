#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 10 15:08:46 2021

@author: chabane
"""
import numpy
import matplotlib.pyplot as plt
import metropolis


def mean(data_array, start, end):
    mean = 0.0
    for i in range(start, end):
        mean += data_array[i]
    return mean

def auto_corrfunction(data_array, N, t):
    c_t = 0
    
    mean_0 = mean(data_array, 0, N-t)
    mean_t = mean(data_array, t, N)
    #print("m0, mt = ", mean_0, mean_t)
    
    for i in range(0, N-t):
        c_t += (data_array[i] - mean_0) * (data_array[i+t] - mean_t)
        #print("ct = ", c_t)
    
    c_t/=(N-t)
    return c_t

def integrated_autocorrfunction(data_array, t, N):
    c_0 = auto_corrfunction(data_array, N, 0)   
    
    c_tilde = 0
    for t in range(1, N):
        c_tilde += (1 + 2*auto_corrfunction(data_array, N, t)/c_0)
    
    print(c_tilde)
    
    return c_tilde # c(t) = C(t)/C(0)

def naive_error(data_array, N):
    return numpy.sqrt(auto_corrfunction(data_array, N, 0)/(N-1))

def true_error(data_array, N):
    sigma = (numpy.sqrt(2.*integrated_autocorrfunction(data_array, N)
            * naive_error(data_array, N)))
    return sigma




t=32
N = 1000



data = metropolis.metropolis(0, 3, N)
#c = numpy.correlate(data, data, mode='full')
#plt.plot(c)




tau_int = numpy.zeros(t)

for i in range(t):
    #data = metropolis.metropolis(0, 3, N)
    tau_int[i] = integrated_autocorrfunction(data, t, N)


print(tau_int)
plt.plot(tau_int)

