#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 17:10:02 2021

@author: chabane
"""

import matplotlib.pyplot as plt
import numpy

import functions, config



L = 10
max_sweep = 20000

sweep_arr = numpy.arange(0, max_sweep)

J = 1

lattice = config.Lattice(L)
l = lattice.init_lattice()

T, d1 = functions.Lsquared(l, max_sweep, J)



plt.plot(T, d1, color='darkred', marker='x')
#plt.imshow(c, cmap='Greys')
#plt.colorbar()
plt.legend()
plt.show()