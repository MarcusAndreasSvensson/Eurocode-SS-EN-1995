#from mpl_toolkits.mplot3d import axes3d
#import matplotlib.pyplot as plt
#import numpy as np
#from scipy.interpolate import interp1d
from structural_calculation import Database, UltimateLimitStateTimber
#import mainWindow
#import editUnitWindow
#import sys
#import PyQt5
from random import random

"""app = PyQt5.QtWidgets.QApplication(sys.argv)
MainWindow = PyQt5.QtWidgets.QMainWindow()
ui = editUnitWindow.Ui_editUnitWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

plt = enhet.plot()

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
"""

data = Database()

for _ in range(10):
    data.add_unit()
    data.members[data.id]["unit_instance"].N = random()*100000
    data.members[data.id]["unit_instance"].V = random()*30000
    #data.members[data.id]["unit_instance"].T = random()*30000
    data.save_result(data.id, data.members[data.id]["unit_instance"].beräkna())

for member in data.members:
    print(member, data.members[member], "\n")







