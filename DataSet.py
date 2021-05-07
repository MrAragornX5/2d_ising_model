#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  7 17:25:19 2021

@author: chabane
"""
import numpy 

# generate markov chain array and then insert it to dataset object

class DataSet:
    def __init__(self, data_array):
        self.data_array = data_array
        
        
    def print_data(self):
        print(self.data_array)
    
    def calc_mean(self, N):
        mean = 0
        for i in range(N):
            mean += self.data_array[i]/N
        return mean

    def calc_NaiveError(self, N):
        sigma_0, sigma_naive = 0.0, 0.0
        mean = self.calc_mean(N)
        
        for i in range(N):
            sigma_0 += numpy.power(abs(self.data_array[i]-mean), 2)
            sigma_0 /= (N-1)
            sigma_naive = numpy.sqrt(sigma_0/N)
 
        return sigma_naive