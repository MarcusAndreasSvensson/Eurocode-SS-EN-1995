from random import random, uniform
import timeit

import structural_calculation


def calc_func():
    data = Database()
    
    for _ in range(100):
        data.add_unit()
        data.members[data.id]["unit_instance"].N = uniform(-1, 1)*100000
        data.members[data.id]["unit_instance"].V = uniform(-1, 1)*30000
        data.members[data.id]["unit_instance"].T = uniform(-1, 1)*30000
        data.save_result(data.id, data.members[data.id]["unit_instance"].beräkna())

    for member in data.members:
        print(data.members[member], "\n")




if __name__ == "__main__":
	calc_func()