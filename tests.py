from random import random, uniform
import timeit
from structural_calculation import Database, StructuralUnit
from xml.etree.ElementTree import ElementTree, Element, XMLParser
import xml.etree.ElementTree as ET
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString


def calc_func_test(i):
    """Creates i number of members and calculates."""
    
    for _ in range(i):
        try:
            data.add_unit()
            data.members[data.id]["object_instance"].M_y = uniform(-1, 1)*100000
            data.members[data.id]["object_instance"].M_z = uniform(-1, 1)*100000
            data.members[data.id]["object_instance"].N = uniform(-1, 1)*100000
            data.members[data.id]["object_instance"].V = uniform(-1, 1)*100000
            data.members[data.id]["object_instance"].T = uniform(-1, 1)*100000
            data.save_result(data.id, data.members[data.id]["object_instance"].start_calculation())
        except TypeError:
            assert (type(data.members[data.id]["object_instance"].M_y) == int() or float()
                    and type(data.members[data.id]["object_instance"].M_z) == int() or float()
                    and type(data.members[data.id]["object_instance"].N) == int() or float()
                    and type(data.members[data.id]["object_instance"].V) == int() or float()
                    and type(data.members[data.id]["object_instance"].T) == int() or float()),\
                    "All values must be of type int() or float()"

    for member in data.members:
        #print(data.members[member], "\n")
        pass

def generate_random_values():
    pass
        

def create_xml_test():
    #bar_unit._prepare_for_xml("large")
    data.create_xml()


def parse_xml_test():
    tree = ElementTree()
    tree.parse(r"C:\Users\Marcus Svensson\Documents\Eurocode-SS-EN-1995\Datasets\rst_basic_sample_project.struxml")

    return tree





if __name__ == "__main__":
    data = Database()
    bar_unit = StructuralUnit()

    #xml = dicttoxml(bar_unit._prepare_for_xml(), attr_type=False)
    #dom = parseString(xml)
    #print(dom.toprettyxml())
        
    calc_func_test(5)
    #print(bar_unit._prepare_for_xml())
    create_xml_test()
    #parser = parse_xml_test()


