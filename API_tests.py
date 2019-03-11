from random import random, uniform, choice
import timeit
from structural_calculation import Database, StructuralUnit
from xml.etree.ElementTree import ElementTree, Element, XMLParser
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import API
from uuid import uuid4


class options:

    def __init__(self):
        pass


class member:
    """
    Per-member functions.
    """

    def __init__(self, name):
        """
        Creates a structural member and sets it as current.
        """
        self.member = API.StructuralUnit(str(uuid4()), name)
        self.member.prepare_for_calculation()
        self.solver = API.UltimateLimitStateTimber()
        self.solver.set_unit(self.member)
        #TODO add member to list function

    @staticmethod
    def add(self, name):
        """
        Add a new member, with name 'name', and set it as the current member.
        """
        self.member = API.StructuralUnit(str(uuid4()), name)
        self.member.prepare_for_calculation()
        self.solver.set_unit(self.member)
        #TODO add member to list function

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
        #TODO fetch member from list function
        self.member = name
        self.solver.set_unit(self.member)

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
            allowed_keyes = ["M_y", "M_z", "N", "V", "T", "material", "name", "service_class", 
                "load_duration_class", "cross_section", "start_point", "end_point"]
            for key, val in kwargs.items():
                if key in allowed_keyes:
                    setattr(self.member, key, val)

        self.member.prepare_for_calculation()

    @staticmethod
    def set_solver(self, solver):
        solver_list = ["UltimateLimitStateTimber", "ULSTimber"]
        if solver in solver_list:
            if solver == "UltimateLimitStateTimber" or "ULSTimber":
                self.solver = API.UltimateLimitStateTimber()
                self.solver.set_unit(self.member)

    @staticmethod
    def start_calculation(self):
        self.member.prepare_for_calculation()
        self.solver.pre_calculations()
        self.solver.start_calculation()

        print("Calculation was successfully computed!")
    

class logger:
    """
    Message logger functions.
    """
    
    @staticmethod
    def __init__():
        pass


if __name__ == "__main__":
    current_member = member("HEJSAN")
    current_member.set_variables(current_member, M_y=337.5, M_z=337.5, N=-10000, V=450, 
        T=200, material="C24", service_class="S2", load_duration_class="medium", 
        cross_section="45x220", start_point=[0,0,0], end_point=[3,0,0])
    current_member.start_calculation(current_member)

    current_member.add(current_member, "NUMMER2")
    current_member.start_calculation(current_member)

    units = current_member.get_variables(current_member)
    with open("units.txt", "w") as f:
        for key, val in units.items():
            f.write(f"{key} : \t\t{val}\n")
