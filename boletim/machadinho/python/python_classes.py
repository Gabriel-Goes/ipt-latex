# Creating a code to learn how python classes works
# Author: Gabriel Góes
# Date: 2019-12-05
# Version: 0.1
# =============================================================================
# Importing libraries
import csv
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import xarray as xr

# This code below is a grid nomeator, it will be used to create a grid
def nomeador_grid(left, right, top, bottom, escala=5):
    e1kk = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
            'H', 'I', 'J', 'K', 'L', 'M', 'N']
    e500k = [['V', 'Y'], ['X', 'Z']]
    e250k = [['A', 'C'], ['B', 'D']]
    e100k = [['I', 'IV'], ['II', 'V'], ['III', 'VI']]
    e50k = [['2', '3'], ['2', '4']]
    e25k = [['NW', 'SW'], ['NE', 'SE']]
    if left > right:
        print('Oeste deve ser menor que leste')
    if top < bottom:
        print('Norte deve ser maior que Sul')
    else:
        id_folha = ''
        if top <= 0:
            id_folha += 'S'
            index = math.floor(-top/4)
        else:
            id_folha += 'N'
            index = math.floor(bottom/4)
        numero = math.ceil((180+right)/6)
        print(numero)
        id_folha += e1kk[index]+str(numero)
        lat_gap = abs(top-bottom)
        # p500k-----------------------
        if (lat_gap <= 2) & (escala >= 1):
            LO = math.ceil(right/3) % 2 == 0
            NS = math.ceil(top/2) % 2 != 0
            id_folha += '_'+e500k[LO][NS]
        # p250k-----------------------
        if (lat_gap <= 1) & (escala >= 2):
            LO = math.ceil(right/1.5) % 2 == 0
            NS = math.ceil(top) % 2 != 0
            id_folha += e250k[LO][NS]
        # p100k-----------------------
        if (lat_gap <= 0.5) & (escala >= 3):
            LO = (math.ceil(right/0.5) % 3)-1
            NS = math.ceil(top/0.5) % 2 != 0
            id_folha += '_'+e100k[LO][NS]
        # p50k------------------------
        if (lat_gap <= 0.25) & (escala >= 4):
            LO = math.ceil(right/0.25) % 2 == 0
            NS = math.ceil(top/0.25) % 2 != 0
            id_folha += '_'+e50k[LO][NS]
        # p25k------------------------
        if (lat_gap <= 0.125) & (escala >= 5):
            LO = math.ceil(right/0.125) % 2 == 0
            NS = math.ceil(top/0.125) % 2 != 0
            id_folha += e25k[LO][NS]
        return id_folha


# =============================================================================
# Creating a class that is a database, as  dictionay, but the dictionary is inside of a dictionary
# this class will have some methods like add, remove, update, etc.
#    Hemisfério Sul e Norte = ['S', 'N']
#    1 : 1.000.000 = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
#                     'H', 'I', 'J', 'K', 'L', 'M', 'N']
#    1 : 500.000   = [['V', 'Y'], ['X', 'Z']]
#    1 : 250.000   = [['A', 'C'], ['B', 'D']]
#    1 : 100.000   = [['I', 'IV'], ['II', 'V'], ['III', 'VI']]
#    1 : 50.000    = [['1', '3'], ['2', '4']]
#    1 : 25.000    = [['NW', 'SW'], ['NE', 'SE']]

class Database:
    # Create a dictionary like {"S" : {"A" : {"V" : {"A" : {"I" : {"1" : {"NW" : {xarray.DataArray}}}}}}}}
