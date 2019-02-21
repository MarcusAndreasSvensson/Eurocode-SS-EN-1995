from random import random, uniform, choice
import timeit
from structural_calculation import Database, StructuralUnit
from xml.etree.ElementTree import ElementTree, Element, XMLParser
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import threading


def define_unit(M_y=337.5, M_z=337.5, N=-10000, V=450, T=200, material="C24", service_class="S2", 
                load_duration_class="medium", section="45x220", start_point=[0,0,0], end_point=[3,0,0]):
    """Defines a member."""
    data.members[data.id]["object_instance"].M_y = M_y
    data.members[data.id]["object_instance"].M_z = M_z
    data.members[data.id]["object_instance"].N = N
    data.members[data.id]["object_instance"].V = V
    data.members[data.id]["object_instance"].T = T
    data.members[data.id]["object_instance"].material = material
    data.members[data.id]["object_instance"].service_class = service_class
    data.members[data.id]["object_instance"].load_duration_class = load_duration_class
    data.members[data.id]["object_instance"].cross_section = section
    data.members[data.id]["object_instance"].start_point = start_point
    data.members[data.id]["object_instance"].end_point = end_point

def calc_func_test(i, random=True, debug_vars=False):
    """Creates i number of members and calculates."""
    if random == True:
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
            data.add_unit()
            define_unit(M_y=uniform(-1, 1)*800, M_z=uniform(-1, 1)*800, N=uniform(-1, 1)*10000, V=uniform(-1, 1)*10000, T=uniform(-1, 1)*200000, 
                        material=choice(material), service_class=choice(service_class), load_duration_class=choice(table_2_1), 
                        section=choice(section), start_point=[0,0,0], end_point=[uniform(0.2, 15),0,0])
            #Prepares and calculates the instances equations
            data.members[data.id]["object_instance"].prepare_for_calculation()
            data.ULS_timber.set_unit(data.members[data.id]["object_instance"])
            data.save_result(data.id, data.ULS_timber.start_calculation())

    else:
        for _ in range(i):
            data.add_unit()
            define_unit()
            #Prepares and calculates the instances' equations
            data.members[data.id]["object_instance"].prepare_for_calculation()
            data.ULS_timber.set_unit(data.members[data.id]["object_instance"])
            data.save_result(data.id, data.ULS_timber.start_calculation())

            if debug_vars == True:
                variables = [attr for attr in vars(data.members[data.id]["object_instance"])]

                for attr in variables:
                    print(attr, "\t", getattr(data.members[data.id]["object_instance"], attr))

            # Space for additional tests
            #data.ULS_timber.ekv_6_11()
            # ==========
        
    for member in data.members:
        print(data.members[member])
        

def create_xml_test():
    data.create_xml()

def parse_xml_test():
    tree = ElementTree()
    tree.parse(r"C:\Users\Marcus Svensson\Documents\Eurocode-SS-EN-1995\Datasets\rst_basic_sample_project.struxml")

    return tree

def clear_database_test():
    data.remove_all_units()
    if data.members == {}:
        print("Database is empty") #TODO add assert statement


def test_chooser(random_memeber_calc=True, specific_member_calc=True, xml_test=True, clear_members=True):
    if random_memeber_calc == True:
        calc_func_test(1000, random=True)

    if specific_member_calc == True:
        calc_func_test(1, random=False, debug_vars=True)

    if xml_test == True:
        create_xml_test()

    if clear_members == True:
        clear_database_test()

if __name__ == "__main__":
    data = Database()
    test_chooser(False, True, True, False)
