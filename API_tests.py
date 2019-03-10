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
    Per-member functions.
    """

    def __init__(self, debug_vars=False, ):
        """
        Creates a structural member.
        """
        self.member = API.StructuralUnit(str(uuid4()))
        self.solver = API.UltimateLimitStateTimber()

    @staticmethod
    def add(name):
        """
        Add a new member, with name 'name', and set it as the current member.
        """
        pass

    @staticmethod
    def remove(name):
        """
        Remove the current member.
        """
        pass

    @staticmethod
    def set_current(self, name):
        """
        Set the current model to the model with name 'name'. If several models have
        the same name, select the one that was added first.
        """
        self.member = name

    @staticmethod
    def get_variables(self):
        var_dict = {}
        for var in vars(self.member):
            val = getattr(self.member, var)
            var_dict[var] = val

        return var_dict

    @staticmethod
    def set_variables(self, **kwargs):
        if kwargs is not None:
            allowed_keyes = ["M_y", "M_z", "N", "V", "T", "material", "service_class", 
                "load_duration_class", "section", "start_point", "end_point"]
            for key, val in kwargs.items():
                if key in allowed_keyes:
                    setattr(self.member, key, val)

    @staticmethod
    def set_solver_or_something(self, solver):
        solver_list = []
        if solver in solver_list:
            self.solver = solver

    @staticmethod
    def start_calculation(self):
        self.member.
        #print(self.test_unit.results)


    class options:

        def __init__(self):
            pass

        @staticmethod
        def set_variables(self):
            """
            self.ULS = API.UltimateLimitStateoptions()
            self.ULS.set_unit(self.test_unit)
            
            
            #Space for additional tests
            
            if debug_vars == True:
                variables = [attr for attr in vars(self.test_unit)]

                with open("units.txt", "w") as f:
                    for attr in variables:
                        f.write(f"{attr}, \t, {getattr(self.test_unit, attr)}\n")"""
            pass
        
        


class logger:
    """
    Message logger functions
    """
    
    @staticmethod
    def __init__():
        pass


if __name__ == "__main__":
    current_member = member()
    current_member.set_variables(current_member, M_y=337.5, M_z=337.5, N=-10000, V=450, 
        T=200, material="C24", service_class="S2", load_duration_class="medium", 
        section="45x220", start_point=[0,0,0], end_point=[3,0,0])
    #print(current_member.get_variables(current_member))
    current_member.start_calculation(current_member)