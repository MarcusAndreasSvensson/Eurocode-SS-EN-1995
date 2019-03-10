from random import random, uniform, choice
import timeit
from structural_calculation import Database, StructuralUnit
from xml.etree.ElementTree import ElementTree, Element, XMLParser
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import API
    

class Timber:

    def __init__(self):
        pass

    @staticmethod
    def init_unit(self, debug_vars=False, M_y=337.5, M_z=337.5, N=-10000, V=450, T=200, material="C24", service_class="S2", 
                    load_duration_class="medium", section="45x220", start_point=[0,0,0], end_point=[3,0,0]):
        """Defines a member."""
        self.test_unit = API.StructuralUnit(000)

        self.test_unit.M_y = M_y
        self.test_unit.M_z = M_z
        self.test_unit.N = N
        self.test_unit.V = V
        self.test_unit.T = T
        self.test_unit.material = material
        self.test_unit.service_class = service_class
        self.test_unit.load_duration_class = load_duration_class
        self.test_unit.cross_section = section
        self.test_unit.start_point = start_point
        self.test_unit.end_point = end_point

        self.ULS = API.UltimateLimitStateTimber()
        self.ULS.set_unit(self.test_unit)
        
        
        #Space for additional tests
        
        if debug_vars == True:
            variables = [attr for attr in vars(self.test_unit)]

            with open("units.txt", "w") as f:
                for attr in variables:
                    f.write(f"{attr}, \t, {getattr(self.test_unit, attr)}\n")

        
    
    @staticmethod
    def start_calculation(self):
        self.ULS.start_calculation()
        print(self.test_unit.results)

if __name__ == "__main__":
    test = Timber()
    Timber.init_unit(test)
    Timber.start_calculation(test)