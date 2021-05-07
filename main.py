#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 01:45:36 2021

@author: chabane
"""


import plot_data, metropolis

# Initialize Conditions
N = 10**3
x_start = 0
a = 3 # sowas wie ein suchradius


# Create Data
data_array = metropolis.metropolis(x_start, a, N)

plot_data.plot_mean(data_array, N)
plot_data.plot_naive_error(data_array, N)