#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt
#import numpy as np
#from scipy.interpolate import interp1d
from structural_calculation import Database, StructuralUnit
#import mainWindow
#import editUnitWindow
#import sys
#import PyQt5
from random import random, uniform
import timeit


def calc_func():
    data = Database()
    
    for _ in range(10):
        data.add_unit()
        data.members[data.id]["unit_instance"].N = uniform(-1, 1)*100000
        data.members[data.id]["unit_instance"].V = uniform(-1, 1)*30000
        #data.members[data.id]["unit_instance"].T = random()*30000
        data.save_result(data.id, data.members[data.id]["unit_instance"].beräkna())

    for member in data.members:
        print(data.members[member], "\n")






