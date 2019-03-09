from random import random, uniform, choice
import timeit
from structural_calculation import Database, StructuralUnit
from xml.etree.ElementTree import ElementTree, Element, XMLParser
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import API
    

def define_unit(debug_vars=False, M_y=337.5, M_z=337.5, N=-10000, V=450, T=200, material="C24", service_class="S2", 
                load_duration_class="medium", section="45x220", start_point=[0,0,0], end_point=[3,0,0]):
    """Defines a member."""
    test_unit = API.StructuralUnit(000)

    test_unit.M_y = M_y
    test_unit.M_z = M_z
    test_unit.N = N
    test_unit.V = V
    test_unit.T = T
    test_unit.material = material
    test_unit.service_class = service_class
    test_unit.load_duration_class = load_duration_class
    test_unit.cross_section = section
    test_unit.start_point = start_point
    test_unit.end_point = end_point

    ULS = API.UltimateLimitStateTimber()
    ULS.set_unit(test_unit)
    test_unit.prepare_for_calculation()
    ULS.start_calculation()
    
    #Space for additional tests
    #data.ULS_timber.ekv_6_32()
    
    if debug_vars == True:
        variables = [attr for attr in vars(test_unit)]

        with open("units.txt", "w") as f:
            for attr in variables:
                f.write(f"{attr}, \t, {getattr(test_unit, attr)}\n")

    print(test_unit.results)
    

if __name__ == "__main__":
    define_unit()