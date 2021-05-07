#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 01:45:36 2021

@author: chabane
"""
import matplotlib.pyplot as plt
import numpy 
import MCMC_metro

N = 10**3
x_start = 0
a = 3 # sowas wie ein suchradius



data_array = MCMC_metro.metropolis(x_start, a, N)

data_mean = numpy.zeros(N)
naive_error = numpy.zeros(N)

for i in range(2, len(data_mean)):
    #data_mean[i]   = MCMC_metro.calc_mean(data_array, i)
    naive_error[i] = MCMC_metro.naive_error(data_array, i)


#print(naive_error)

fig1 = plt.figure()
plt.title(r"Markov-Chain for $N$ = " + str(N))
plt.grid(b=True, which='major', color='#666666', linestyle='--')
plt.minorticks_on()
plt.grid(b=True, which='minor', color='#999999', linestyle='--', alpha=0.1)

plt.xlabel(r'$N$')
plt.ylabel(r"$\langle x\rangle$")


#plt.plot(data_mean, 
#         #marker="1", 
#         color= "navy", 
#         label = r"Sample-Mean: $\frac{1}{N}\sum_i f(x_i)$")

plt.loglog(naive_error, 
         #marker="1", 
         color= "navy", 
         label = r"Naive-error:") #$\sigma^2 = \sqrt(\frac{1}{N} \sigma_f^2)$")

plt.legend(loc='best')
#fig1.savefig('test.pdf', dpi=300, bbox_inches='tight')