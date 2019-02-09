from random import random, uniform, choice
import timeit
from structural_calculation import Database, StructuralUnit
from xml.etree.ElementTree import ElementTree, Element, XMLParser
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import threading


def calc_func_test(i):
    """Creates i number of members and calculates."""
    table_2_1 = ["permanent", "long", "medium", "instant"]
    material = ["C14", "C16", "C18", "C20", "C22", "C24", "C27", "C30", "C35", "C40", "C45", "C50"]
    section = ["22x22","22x28","22x34","22x45","22x58","22x70","22x95","22x120","22x145","22x170","22x195","22x220",
                    "34x22","34x28","34x34","34x45","34x58","34x70","34x95","34x120","34x145","34x170","34x195","34x220",
                    "45x22","45x28","45x34","45x45","45x58","45x70","45x95","45x120","45x145","45x170","45x195","45x220",
                    "58x22","58x28","58x34","58x45","58x58","58x70","58x95","58x120","58x145","58x170","58x195","58x220",
                    "70x22","70x28","70x34","70x45","70x58","70x70","70x95","70x120","70x145","70x170","70x195","70x2220",
                    "95x22","95x28","95x34","95x45","95x58","95x70","95x95","95x120","95x145","95x170","95x195","95x220"]
    service_class = ["S1", "S2", "S3"]
    
    for _ in range(i):
        try:
            data.add_unit()
            data.members[data.id]["object_instance"].M_y = uniform(-1, 1)*800
            data.members[data.id]["object_instance"].M_z = uniform(-1, 1)*800
            data.members[data.id]["object_instance"].N = uniform(-1, 1)*10000
            data.members[data.id]["object_instance"].V = uniform(-1, 1)*10000
            data.members[data.id]["object_instance"].T = uniform(-1, 1)*200000
            data.members[data.id]["object_instance"].material = choice(material)
            data.members[data.id]["object_instance"].service_class = choice(service_class)
            data.members[data.id]["object_instance"].load_duration_class = choice(table_2_1)
            data.members[data.id]["object_instance"].section = data.members[data.id]["object_instance"].cross_section = choice(section)
            data.members[data.id]["object_instance"].start_point = [0,0,0]
            data.members[data.id]["object_instance"].end_point = [uniform(0.2, 15),0,0]

            #Prepares and calculates the instances equations
            data.members[data.id]["object_instance"].prepare_for_calculation()
            data.save_result(data.id, data.members[data.id]["object_instance"].start_calculation())

        except TypeError:
            assert (type(data.members[data.id]["object_instance"].M_y) == int() or float()
                    and type(data.members[data.id]["object_instance"].M_z) == int() or float()
                    and type(data.members[data.id]["object_instance"].N) == int() or float()
                    and type(data.members[data.id]["object_instance"].V) == int() or float()
                    and type(data.members[data.id]["object_instance"].T) == int() or float()),\
                    "All values must be of type int() or float()"

        

        
    for member in data.members:
        print(data.members[member])
        

def create_xml_test():
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

    calc_func_test(20)
    #print(bar_unit._prepare_for_xml())
    create_xml_test()
    #parser = parse_xml_test()


