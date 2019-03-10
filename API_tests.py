from random import random, uniform, choice
import timeit
from structural_calculation import Database, StructuralUnit
from xml.etree.ElementTree import ElementTree, Element, XMLParser
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import API
from uuid import uuid4
    

class member:
    """
    Per-member functionns.
    """

    def __init__(self, debug_vars=False, M_y=337.5, M_z=337.5, N=-10000, V=450, T=200, material="C24", service_class="S2", 
                    load_duration_class="medium", section="45x220", start_point=[0,0,0], end_point=[3,0,0]):
        """
        Creates a structural member.
        """
        self.member = API.StructuralUnit(str(uuid4()))
        print(self.member)

    @staticmethod
    def add(name):
        """
        Add a new member, with name 'name', and set it as the current member.
        """
        pass

    @staticmethod
    def remove():
        """
        Remove the current member.
        """
        pass

    @staticmethod
    def set_current():
        """
        Set the current model to the model with name `name'. If several models have
        the same name, select the one that was added first.
        """


    @staticmethod
    def get_variables():
        variables = [var for var in vars(self.unit)]

        return variables


    class options:

        def __init__(self):
            pass

        

        @staticmethod
        def set_variables(self):
            """self.test_unit.M_y = M_y
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

            self.ULS = API.UltimateLimitStateoptions()
            self.ULS.set_unit(self.test_unit)
            
            
            #Space for additional tests
            
            if debug_vars == True:
                variables = [attr for attr in vars(self.test_unit)]

                with open("units.txt", "w") as f:
                    for attr in variables:
                        f.write(f"{attr}, \t, {getattr(self.test_unit, attr)}\n")"""
            pass
        
        @staticmethod
        def start_calculation(self):
            self.ULS.start_calculation()
            #print(self.test_unit.results)


class logger:
    """
    Message logger functions
    """
    
    @staticmethod
    def __init__():
        pass


if __name__ == "__main__":
    initialize()
    
    print(get_variables())