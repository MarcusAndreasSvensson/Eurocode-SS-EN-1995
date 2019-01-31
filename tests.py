from random import random, uniform
import timeit

from structural_calculation import Database, StructuralUnit


def calc_func(i):
    """Creates i number of members and calculates."""
    data = Database()
    
    for _ in range(i):
        try:
            data.add_unit()
            data.members[data.id]["unit_instance"].M_y = uniform(-1, 1)*100000
            data.members[data.id]["unit_instance"].M_z = uniform(-1, 1)*100000
            data.members[data.id]["unit_instance"].N = uniform(-1, 1)*100000
            data.members[data.id]["unit_instance"].V = uniform(-1, 1)*100000
            data.members[data.id]["unit_instance"].T = uniform(-1, 1)*100000
            data.save_result(data.id, data.members[data.id]["unit_instance"].beräkna())
        except TypeError:
            assert (type(data.members[data.id]["unit_instance"].M_y) == int() or float()
                    and type(data.members[data.id]["unit_instance"].M_z) == int() or float()
                    and type(data.members[data.id]["unit_instance"].N) == int() or float()
                    and type(data.members[data.id]["unit_instance"].V) == int() or float()
                    and type(data.members[data.id]["unit_instance"].T) == int() or float()),\
                    "All values must be of type int() or float()"

    for member in data.members:
        print(data.members[member], "\n")


def test():
    pass







if __name__ == "__main__":
	calc_func(10)
