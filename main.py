from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
import enhet
import numpy
import GUI


### Initiates the list of units ###
unit_database = enhet.Database()




"""plt = enhet.plot()

plt.add_object([0,6,0], [0,0,0])
plt.add_object([5,0,0], [5,5,0])
plt.add_object([5,5,0], [5,5,5])
plt.add_object([5,0,5], [5,5,5])
plt.add_object([0,0,5], [0,5,5])
plt.add_object([1, 0, 2.5], [1, 5, 2.5])
plt.add_object([0,5,0], [0,5,5])
plt.add_object([2,0,2], [2,4,2])
plt.add_object([6,0,-1], [6,7,-1])

plt.add_square_face([0,5,0], [5,5,5])
plt.show()


calc = enhet.ULSTrä()

print(calc.beräkna())

"""
