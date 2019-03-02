import math
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from numpy import array
from mpl_toolkits.mplot3d import Axes3D
from collections import namedtuple
from uuid import uuid4
from xml.etree.ElementTree import ElementTree, Element, tostring
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
from sympy.physics.mechanics import ReferenceFrame, inertia


class TableValues:
	def __init__(self):
		pass

	def tabell_2_1(self, duration):
		tabell = {"permanent" : "more than 10 years",
					"long term" : "6 months - 10 years",
					"medium term" : "1 week - 6 months",
					"instantaneous" : "0"}

	def tabell_2_3(self, type):
		#TODO add upper- or lowercase independency
		tabell = {"solid timber" : 1.3,
					"glued laminated timber" : 1.25,
					"LVL" : 1.2,
					"plywood" : 1.2,
					"OSB" : 1.2,
					"particleboard" : 1.3,
					"hard fibreboard" : 1.3,
					"medium fibreboard" : 1.3,
					"MDF fibreboard" : 1.3,
					"soft fibreboard" : 1.3,
					"connection" : 1.3,
					"punched metal plate fastener" : 1.25,
					"accidental" : 1}

		gamma_M = tabell.get(type)

		return gamma_M

	def tabell_3_1(self, type, service_class, load_duration_class):
		#TODO finish the last + logic for the instances that contain more than 3 service classes

		tabell = {"solid timber" : {"S1" : {"permanent" : 0.6, "long" : 0.7, "medium" : 0.8, "short" : 0.9, "instant" : 1.1},
									"S2" : {"permanent" : 0.6, "long" : 0.7, "medium" : 0.8, "short" : 0.9, "instant" : 1.1},
									"S3" : {"permanent" : 0.5, "long" : 0.55, "medium" : 0.65, "short" : 0.7, "instant" : 0.9}},
					"glued laminated timber" : {"S1" : {"permanent" : 0.6, "long" : 0.7, "medium" : 0.8, "short" : 0.9, "instant" : 1.1},
												"S2" : {"permanent" : 0.6, "long" : 0.7, "medium" : 0.8, "short" : 0.9, "instant" : 1.1},
												"S3" : {"permanent" : 0.5, "long" : 0.55, "medium" : 0.65, "short" : 0.7, "instant" : 0.9}},
					"LVL" : {"S1" : {"permanent" : 0.6, "long" : 0.7, "medium" : 0.8, "short" : 0.9, "instant" : 1.1},
							"S2" : {"permanent" : 0.6, "long" : 0.7, "medium" : 0.8, "short" : 0.9, "instant" : 1.1},
							"S3" : {"permanent" : 0.5, "long" : 0.55, "medium" : 0.65, "short" : 0.7, "instant" : 0.9}},
					"plywood" : {"S1" : {"permanent" : 0.6, "long" : 0.7, "medium" : 0.8, "short" : 0.9, "instant" : 1.1},
								"S2" : {"permanent" : 0.6, "long" : 0.7, "medium" : 0.8, "short" : 0.9, "instant" : 1.1},
								"S3" : {"permanent" : 0.5, "long" : 0.55, "medium" : 0.65, "short" : 0.7, "instant" : 0.9}},
					"OSB" : {"S1" : {"permanent" : 0.3, "long" : 0.45, "medium" : 0.65, "short" : 0.85, "instant" : 1.1},
							"S2" : {"permanent" : 0.4, "long" : 0.5, "medium" : 0.7, "short" : 0.9, "instant" : 1.1},
							"S3" : {"permanent" : 0.3, "long" : 0.4, "medium" : 0.55, "short" : 0.7, "instant" : 0.9}},
					"particleboard" : {"S1" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
										"S2" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
										"S3" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666}},
					"hard fibreboard" : {"S1" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
										"S2" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
										"S3" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666}},
					"medium fibreboard" : {"S1" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
											"S2" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
											"S3" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666}},
					"MDF fibreboard" : {"S1" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
										"S2" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
										"S3" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666}},
					"soft fibreboard" : {"S1" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
										"S2" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
										"S3" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666}},
					"connection" : {"S1" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
									"S2" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
									"S3" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666}},
					"punched metal plate fastener" : {"S1" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
													"S2" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
													"S3" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666}},
					"accidental" : {"S1" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
									"S2" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666},
									"S3" : {"permanent" : 666, "long" : 666, "medium" : 666, "short" : 666, "instant" : 666}}}
		
		k_mod = tabell.get(type).get(service_class).get(load_duration_class)
		return k_mod
	
	def tabell_3_2(self, type, service_class):
		#TODO Finish table + logic, e.g. type if type == true
		tabell = {"solid timber": {"S1": 0.6, "S2": 0.8, "S3": 2},
				  "glued laminated timber": {"S1": 0.6, "S2": 0.8, "S3": 2},
                  "LVL": {"S1": 0.6, "S2": 0.8, "S3": 2}, #TODO finished to here, finish the rest
                  "plywood": {"S1": 6, "S2": 6, "S3": 6},
                  "OSB": {"S1": 6, "S2": 6, "S3": 6},
                  "particleboard": {"S1": 6, "S2": 6, "S3": 6},
                  "hard fibreboard": {"S1": 6, "S2": 6, "S3": 6},
                  "medium fibreboard": {"S1": 6, "S2": 6, "S3": 6},
                  "MDF fibreboard": {"S1": 6, "S2": 6, "S3": 6}}
		
		k_def = tabell.get(type).get(service_class)
		return k_def

	def tabell_6_1(self, l, stödtyp, lasttyp, torsionally_restrained, center, load_side, h):
		#TODO add supported logic somehow...
		tabell = {"Simply supported": {"Constant moment": 1,
										"Uniformly distributed load": 0.9,
										"Concentrated force at the middle of the span": 0.8},
					"Cantilever": {"Uniformly distributed load": 0.5,
									"Concentrated force at the free end": 0.8}}

		if torsionally_restrained == True and center == True:
			l_ef = tabell.get(stödtyp).get(lasttyp)

			if load_side == "compression":
				l_ef = l_ef*l + 2*h*1e-3
			elif load_side == "tension":
				l_ef = l_ef*l - 0.5*h*1e-3
		else:
			l_ef = 1 * l

		return l_ef

	# TODO Make material values table for D-classes and Glulam
	def material_values_timber(self, material, konst):
		tabell = {#                N/mm2                                                                            N/mm2                                                           kg/m3
			"C14": {"f_m_k": 14, "f_t_0_k": 8, "f_t_90_k": 0.4, "f_c_0_k": 16, "f_c_90_k": 2.0, "f_v_k": 1.7, "E_0_mean": 7000, "E_0_05": 4700, "E_90_mean": 230, "G_mean": 440, "rho_k": 290, "rho_mean": 350},
			"C16": {"f_m_k": 16, "f_t_0_k": 10, "f_t_90_k": 0.5, "f_c_0_k": 17, "f_c_90_k": 2.2, "f_v_k": 1.8, "E_0_mean": 8000, "E_0_05": 5400, "E_90_mean": 270, "G_mean": 500, "rho_k": 310, "rho_mean": 370},
			"C18": {"f_m_k": 18, "f_t_0_k": 11, "f_t_90_k": 0.5, "f_c_0_k": 18, "f_c_90_k": 2.2, "f_v_k": 2.0, "E_0_mean": 9000, "E_0_05": 6000, "E_90_mean": 300, "G_mean": 560, "rho_k": 320, "rho_mean": 380},
			"C20": {"f_m_k": 20, "f_t_0_k": 12, "f_t_90_k": 0.5, "f_c_0_k": 19, "f_c_90_k": 2.3, "f_v_k": 2.2, "E_0_mean": 9500, "E_0_05": 6400, "E_90_mean": 320, "G_mean": 590, "rho_k": 330, "rho_mean": 390},
			"C22": {"f_m_k": 22, "f_t_0_k": 13, "f_t_90_k": 0.5, "f_c_0_k": 20, "f_c_90_k": 2.4, "f_v_k": 2.4, "E_0_mean": 10000, "E_0_05": 6700, "E_90_mean": 330, "G_mean": 630, "rho_k": 340, "rho_mean": 410},
			"C24": {"f_m_k": 24, "f_t_0_k": 14, "f_t_90_k": 0.5, "f_c_0_k": 21, "f_c_90_k": 2.5, "f_v_k": 2.5, "E_0_mean": 11000, "E_0_05": 7400, "E_90_mean": 370, "G_mean": 690, "rho_k": 350, "rho_mean": 420},
			"C27": {"f_m_k": 27, "f_t_0_k": 16, "f_t_90_k": 0.6, "f_c_0_k": 22, "f_c_90_k": 2.6, "f_v_k": 2.8, "E_0_mean": 11500, "E_0_05": 7700, "E_90_mean": 380, "G_mean": 720, "rho_k": 370, "rho_mean": 450},
			"C30": {"f_m_k": 30, "f_t_0_k": 18, "f_t_90_k": 0.6, "f_c_0_k": 23, "f_c_90_k": 2.7, "f_v_k": 3.0, "E_0_mean": 12000, "E_0_05": 8000, "E_90_mean": 400, "G_mean": 750, "rho_k": 380, "rho_mean": 460},
			"C35": {"f_m_k": 35, "f_t_0_k": 21, "f_t_90_k": 0.6, "f_c_0_k": 25, "f_c_90_k": 2.8, "f_v_k": 3.4, "E_0_mean": 13000, "E_0_05": 8700, "E_90_mean": 430, "G_mean": 810, "rho_k": 400, "rho_mean": 480},
			"C40": {"f_m_k": 40, "f_t_0_k": 24, "f_t_90_k": 0.6, "f_c_0_k": 26, "f_c_90_k": 2.9, "f_v_k": 3.8, "E_0_mean": 14000, "E_0_05": 9400, "E_90_mean": 470, "G_mean": 880, "rho_k": 420, "rho_mean": 500},
			"C45": {"f_m_k": 45, "f_t_0_k": 27, "f_t_90_k": 0.6, "f_c_0_k": 27, "f_c_90_k": 3.1, "f_v_k": 3.8, "E_0_mean": 15000, "E_0_05": 10000, "E_90_mean": 500, "G_mean": 940, "rho_k": 440, "rho_mean": 520},
			"C50": {"f_m_k": 50, "f_t_0_k": 30, "f_t_90_k": 0.6, "f_c_0_k": 29, "f_c_90_k": 3.2, "f_v_k": 3.8, "E_0_mean": 16000, "E_0_05": 10700, "E_90_mean": 530, "G_mean": 1000, "rho_k": 460, "rho_mean": 550}}

		konstant = tabell.get(material).get(konst)

		return konstant

	def avsnitt_6_1_6_2(self, cross_section, type):
		if type == "solid timber" or type == "glued laminated timber" or type == "LVL":
			if cross_section == "rectangular":
				k_m = 0.7
			else:
				k_m = 1
		else:
			k_m = 1

		return k_m

	def avsnitt_6_1_5(self, support, type):
		tabell = {"continuous support": {"Solid softwood": 1.25,
											"Glued laminated softwood": 1.5},
					"discrete support": {"Solid softwood": 1.5,
										"Glued laminated softwood": 1.75}}

		k_c_90 = tabell.get(support).get(type)

		return k_c_90

	def effektiv_längd_placeholder(self, typ, längd):
		# TODO There are two of these values, but I don't know why
		tabell = {"ledadx2": 1,
					"ledadx1": 2,
					"fast+ledad": 0.7,
					"fastx2": 0.5}

		value = tabell.get(typ) * längd

		return value


class Sections:

	def __init__(self):
		pass

	def get_dimensions(self, polygon):
		h = [0,0]
		b = [0,0]

		i = 0
		for _ in polygon:
			if polygon[i][0] < b[0]:
				b[0] = polygon[i][0]
			if polygon[i][0] > b[1]:
				b[1] = polygon[i][0]

			if polygon[i][1] < h[0]:
				h[0] = polygon[i][1]
			if polygon[i][1] > h[1]:
				h[1] = polygon[i][1]

			i += 1

		return b[1]-b[0], h[1]-h[0]

	def set_section(self, type, tvärsnitt):
		sections = {"Dressed Lumber": {"22x22": ([22,22], [[0,0],[0,22],[22,22],[22,0]]),
										"22x28": ([22,28], [[0,0],[0,28],[22,28],[22,0]]),
										"22x34": ([22,34], [[0,0],[0,34],[22,34],[22,0]]),
										"22x45": ([22,45], [[0,0],[0,45],[22,45],[22,0]]),
										"22x58": ([22,58], [[0,0],[0,58],[22,58],[22,0]]),
										"22x70": ([22,70], [[0,0],[0,70],[22,70],[22,0]]),
										"22x95": ([22,95], [[0,0],[0,95],[22,95],[22,0]]),
										"22x120": ([22,120], [[0,0],[0,120],[22,120],[22,0]]),
										"22x145": ([22,145], [[0,0],[0,145],[22,145],[22,0]]),
										"22x170": ([22,170], [[0,0],[0,170],[22,170],[22,0]]),
										"22x195": ([22,195], [[0,0],[0,195],[22,195],[22,0]]),
										"22x220": ([22,220], [[0,0],[0,220],[22,220],[22,0]]),
										"34x22": ([34,22], [[0,0],[0,22],[34,22],[34,0]]),
										"34x28": ([34,28], [[0,0],[0,28],[34,28],[34,0]]),
										"34x34": ([34,34], [[0,0],[0,34],[34,34],[34,0]]),
										"34x45": ([34,45], [[0,0],[0,45],[34,45],[34,0]]),
										"34x58": ([34,58], [[0,0],[0,58],[34,58],[34,0]]),
										"34x70": ([34,70], [[0,0],[0,70],[34,70],[34,0]]),
										"34x95": ([34,95], [[0,0],[0,95],[34,95],[34,0]]),
										"34x120": ([34,120], [[0,0],[0,120],[34,120],[34,0]]),
										"34x145": ([34,145], [[0,0],[0,145],[34,145],[34,0]]),
										"34x170": ([34,170], [[0,0],[0,170],[34,170],[34,0]]),
										"34x195": ([34,195], [[0,0],[0,195],[34,195],[34,0]]),
										"34x220": ([34,220], [[0,0],[0,220],[34,220],[34,0]]),
										"45x22": ([45,22], [[0,0],[0,22],[45,22],[45,0]]),
										"45x28": ([45,28], [[0,0],[0,28],[45,28],[45,0]]),
										"45x34": ([45,34], [[0,0],[0,34],[45,34],[45,0]]),
										"45x45": ([45,45], [[0,0],[0,45],[45,45],[45,0]]),
										"45x58": ([45,58], [[0,0],[0,58],[45,58],[45,0]]),
										"45x70": ([45,70], [[0,0],[0,70],[45,70],[45,0]]),
										"45x95": ([45,95], [[0,0],[0,95],[45,95],[45,0]]),
										"45x120": ([45,120], [[0,0],[0,120],[45,120],[45,0]]),
										"45x145": ([45,145], [[0,0],[0,145],[45,145],[45,0]]),
										"45x170": ([45,170], [[0,0],[0,170],[45,170],[45,0]]),
										"45x195": ([45,195], [[0,0],[0,195],[45,195],[45,0]]),
										"45x220": ([45,220], [[0,0],[0,220],[45,220],[45,0]]),
										"58x22": ([58,22], [[0,0],[0,22],[58,22],[58,0]]),
										"58x28": ([58,28], [[0,0],[0,28],[58,28],[58,0]]),
										"58x34": ([58,34], [[0,0],[0,34],[58,34],[58,0]]),
										"58x45": ([58,45], [[0,0],[0,45],[58,45],[58,0]]),
										"58x58": ([58,58], [[0,0],[0,58],[58,58],[58,0]]),
										"58x70": ([58,70], [[0,0],[0,70],[58,70],[58,0]]),
										"58x95": ([58,95], [[0,0],[0,95],[58,95],[58,0]]),
										"58x120": ([58,120], [[0,0],[0,120],[58,120],[58,0]]),
										"58x145": ([58,145], [[0,0],[0,145],[58,145],[58,0]]),
										"58x170": ([58,170], [[0,0],[0,170],[58,170],[58,0]]),
										"58x195": ([58,195], [[0,0],[0,195],[58,195],[58,0]]),
										"58x220": ([58,220], [[0,0],[0,220],[58,220],[58,0]]),
										"70x22": ([70,22], [[0,0],[0,22],[70,22],[70,0]]),
										"70x28": ([70,28], [[0,0],[0,28],[70,28],[70,0]]),
										"70x34": ([70,34], [[0,0],[0,34],[70,34],[70,0]]),
										"70x45": ([70,45], [[0,0],[0,45],[70,45],[70,0]]),
										"70x58": ([70,58], [[0,0],[0,58],[70,58],[70,0]]),
										"70x70": ([70,70], [[0,0],[0,70],[70,70],[70,0]]),
										"70x95": ([70,95], [[0,0],[0,95],[70,95],[70,0]]),
										"70x120": ([70,120], [[0,0],[0,120],[70,120],[70,0]]),
										"70x145": ([70,145], [[0,0],[0,145],[70,145],[70,0]]),
										"70x170": ([70,170], [[0,0],[0,170],[70,170],[70,0]]),
										"70x195": ([70,195], [[0,0],[0,195],[70,195],[70,0]]),
										"70x2220": ([70,220], [[0,0],[0,220],[70,220],[70,0]]),
										"95x22": ([95,22], [[0,0],[0,22],[95,22],[95,0]]),
										"95x28": ([95,28], [[0,0],[0,28],[95,28],[95,0]]),
										"95x34": ([95,34], [[0,0],[0,34],[95,34],[95,0]]),
										"95x45": ([95,45], [[0,0],[0,45],[95,45],[95,0]]),
										"95x58": ([95,58], [[0,0],[0,58],[95,58],[95,0]]),
										"95x70": ([95,70], [[0,0],[0,70],[95,70],[95,0]]),
										"95x95": ([95,95], [[0,0],[0,95],[95,95],[95,0]]),
										"95x120": ([95,120], [[0,0],[0,120],[95,120],[95,0]]),
										"95x145": ([95,145], [[0,0],[0,145],[95,145],[95,0]]),
										"95x170": ([95,170], [[0,0],[0,170],[95,170],[95,0]]),
										"95x195": ([95,195], [[0,0],[0,195],[95,195],[95,0]]),
										"95x220": ([95,220], [[0,0],[0,220],[95,220],[95,0]]),},
					"Glued Laminated Timber": {"42x90": [42,90],
												"42x135": [42,135],
												"42x180": [42,180],
												"42x225": [42,225],
												"42x270": [42,270],
												"42x315": [42,315],
												"42x360": [42,360],
												"42x405": [42,405],
												"42x450": [42,450],
												"42x495": [42,495],
												"42x540": [42,540],
												"42x585": [42,585],
												"42x630": [42,630],
												"42x675": [42,675],
												"66x90": [66,90],
												"66x135": [66,135],
												"66x180": [66,180],
												"66x225": [66,225],
												"66x270": [66,270],
												"66x315": [66,315],
												"66x360": [66,360],
												"66x405": [66,405],
												"66x450": [66,450],
												"66x495": [66,495],
												"66x540": [66,540],
												"66x585": [66,585],
												"66x630": [66,630],
												"66x675": [66,675],
												"78x90": [78,90],
												"78x135": [78,135],
												"78x180": [78,180],
												"78x225": [78,225],
												"78x270": [78,270],
												"78x315": [78,315],
												"78x360": [78,360],
												"78x405": [78,405],
												"78x450": [78,450],
												"78x495": [78,495],
												"78x540": [78,540],
												"78x585": [78,585],
												"78x630": [78,630],
												"78x675": [78,675],
												"90x90": [90,90],
												"90x135": [90,135],
												"90x180": [90,180],
												"90x225": [90,225],
												"90x270": [90,270],
												"90x315": [90,315],
												"90x360": [90,360],
												"90x405": [90,405],
												"90x450": [90,450],
												"90x495": [90,495],
												"90x540": [90,540],
												"90x585": [90,585],
												"90x630": [90,630],
												"90x675": [90,675],
												"90x720": [90,720],
												"90x765": [90,765],
												"90x810": [90,810],
												"90x855": [90,855],
												"90x900": [90,900],
												"90x945": [90,945],
												"90x990": [90,990],
												"90x1035": [90,1035],
												"90x1080": [90,1080],
												"90x1125": [90,1125],
												"90x1170": [90,1170],
												"90x1215": [90,1215],
												"115x90": [115,90],
												"115x115": [115,115],
												"115x135": [115,135],
												"115x180": [115,180],
												"115x225": [115,225],
												"115x270": [115,270],
												"115x315": [115,315],
												"115x360": [115,360],
												"115x405": [115,405],
												"115x450": [115,450],
												"115x495": [115,495],
												"115x540": [115,540],
												"115x585": [115,585],
												"115x630": [115,630],
												"115x675": [115,675],
												"115x720": [115,720],
												"115x765": [115,765],
												"115x810": [115,810],
												"115x855": [115,855],
												"115x900": [115,900],
												"115x945": [115,945],
												"115x990": [115,990],
												"115x1035": [115,1035],
												"115x1080": [115,1080],
												"115x1125": [115,1125],
												"115x1260": [115,1260],
												"115x1305": [115,1305],
												"115x1350": [115,1350],
												"140x90": [140,90],
												"140x135": [140,135],
												"140x140": [140,140],
												"140x225": [140,225],
												"140x270": [140,270],
												"140x315": [140,315],
												"140x360": [140,360],
												"140x405": [140,405],
												"140x495": [140,495],
												"140x540": [140,540],
												"140x585": [140,585],
												"140x630": [140,630],
												"140x675": [140,675],
												"140x720": [140,720],
												"140x765": [140,765],
												"140x810": [140,810],
												"140x855": [140,855],
												"140x900": [140,900],
												"140x945": [140,945],
												"140x990": [140,990],
												"140x1035": [140,1035],
												"140x1080": [140,1080],
												"140x1125": [140,1125],
												"140x1170": [140,1170],
												"140x1215": [140,1215],
												"140x1260": [140,1260],
												"140x1305": [140,1305],
												"140x1350": [140,1350],
												"140x1395": [140,1395],
												"140x1440": [140,1440],
												"140x1485": [140,1485],
												"140x1530": [140,1530],
												"140x1575": [140,1575],
												"140x1620": [140,1620],
												"165x90": [165,90],
												"165x135": [165,135],
												"165x165": [165,165],
												"165x180": [165,180],
												"165x225": [165,225],
												"165x270": [165,270],
												"165x315": [165,315],
												"165x360": [165,360],
												"165x405": [165,405],
												"165x450": [165,450],
												"165x495": [165,495],
												"165x540": [165,540],
												"165x585": [165,585],
												"165x630": [165,630],
												"165x675": [165,675],
												"165x720": [165,720],
												"165x765": [165,765],
												"165x810": [165,810],
												"165x855": [165,855],
												"165x900": [165,900],
												"165x945": [165,945],
												"165x1035": [165,1035],
												"165x1080": [165,1080],
												"165x1125": [165,1125],
												"165x1170": [165,1170],
												"165x1215": [165,1215],
												"165x1260": [165,1260],
												"165x1305": [165,1305],
												"165x1350": [165,1350],
												"165x1395": [165,1395],
												"165x1440": [165,1440],
												"165x1485": [165,1485],
												"165x1530": [165,1530],
												"165x1575": [165,1575],
												"165x1620": [165,1620],
												"190x90": [190,90],
												"190x135": [190,135],
												"190x165": [190,165],
												"190x180": [190,180],
												"190x220": [190,225],
												"190x270": [190,270],
												"190x315": [190,315],
												"190x360": [190,360],
												"190x405": [190,405],
												"190x450": [190,450],
												"190x495": [190,495],
												"190x540": [190,540],
												"190x585": [190,585],
												"190x630": [190,630],
												"190x675": [190,675],
												"190x720": [190,720],
												"190x765": [190,765],
												"190x810": [190,810],
												"190x855": [190,855],
												"190x900": [190,900],
												"190x945": [190,945],
												"190x1035": [190,1035],
												"190x1080": [190,1080],
												"190x1125": [190,1125],
												"190x1170": [190,1170],
												"190x1215": [190,1215],
												"190x1260": [190,1260],
												"190x1305": [190,1305],
												"190x1350": [190,1350],
												"190x1395": [190,1395],
												"190x1440": [190,1440],
												"190x1485": [190,1485],
												"190x1530": [190,1530],
												"190x1575": [190,1575],
												"190x1620": [190,1620],
												"215x90": [215,90],
												"215x135": [215,135],
												"215x165": [215,165],
												"215x180": [215,180],
												"215x225": [215,225],
												"215x270": [215,270],
												"215x315": [215,315],
												"215x360": [215,360],
												"215x405": [215,405],
												"215x450": [215,450],
												"215x495": [215,495],
												"215x540": [215,540],
												"215x585": [215,585],
												"215x630": [215,630],
												"215x675": [215,675],
												"215x720": [215,720],
												"215x765": [215,765],
												"215x810": [215,810],
												"215x855": [215,855],
												"215x900": [215,900],
												"215x945": [215,945],
												"215x1035": [215,1035],
												"215x1080": [215,1080],
												"215x1125": [215,1125],
												"215x1170": [215,1170],
												"215x1215": [215,1215],
												"215x1260": [215,1260],
												"215x1305": [215,1305],
												"215x1350": [215,1350],
												"215x1395": [215,1395],
												"215x1440": [215,1440],
												"215x1485": [215,1485],
												"215x1530": [215,1530],
												"215x1575": [215,1575],
												"215x1620": [215,1620]}}

		section = sections.get(type).get(tvärsnitt)

		return section

	def get_area(self, polygon):
		#TODO I think it's industry standard to go counterclockwise, change that (alot of work)
		area = 0

		i = 0
		for _ in polygon:
			try:
				area += (polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1])
				i += 1
			except IndexError:
				area += (polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1])
				break

		area = abs(area) / 2
		return area

	def get_centroid(self, polygon):
		#TODO I think it's industry standard to go counterclockwise, change that (alot of work)
		centroid_x = 0
		centroid_y = 0

		i = 0
		for _ in polygon:
			try:
				centroid_x += ((polygon[i][0] + polygon[i+1][0]) * (polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1]))
				centroid_y += ((polygon[i][1] + polygon[i+1][1]) * (polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1]))
				i += 1
			except IndexError:
				centroid_x += ((polygon[i][0] + polygon[0][0]) * (polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1]))
				centroid_y += ((polygon[i][1] + polygon[0][1]) * (polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1]))
				break

		area = self.get_area(polygon)
		centroid_x = abs(centroid_x) * 1/(6*area)
		centroid_y = abs(centroid_y) * 1/(6*area)

		centroids = [centroid_x, centroid_y]
		return centroids

	def get_moment_of_inertia(self, polygon):
		#TODO I think it's industry standard to go counterclockwise, change that (alot of work)
		I_x = 0
		I_y = 0
		I_xy = 0
		centroid = self.get_centroid(polygon)

		for i, _ in enumerate(polygon):
			try:
				area = polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1]

				x = (pow((polygon[i][1] - centroid[1]), 2) + 
						(polygon[i][1] - centroid[1]) * (polygon[i+1][1] - centroid[1]) + 
						pow((polygon[i+1][1] - centroid[1]), 2))
						
				y = (pow((polygon[i][0] - centroid[0]), 2) + 
						(polygon[i][0] - centroid[0]) * (polygon[i+1][0] - centroid[0]) + 
						pow((polygon[i+1][0] - centroid[0]), 2))
				
				xy = (((polygon[i][1]-centroid[1])*(polygon[i+1][0]-centroid[0])) + 
					(2*(polygon[i][1]-centroid[1])*(polygon[i][0]-centroid[0])) + 
					(2*(polygon[i+1][1]-centroid[1])*(polygon[i+1][0]-centroid[0])) + 
					((polygon[i+1][1]-centroid[1])*(polygon[i][0]-centroid[0])))
					
				I_x += x * area
				I_y += y * area
				I_xy += xy * area

				#(a^4)/(192)ncot(pi/n)[3cos^2(pi/n)+1]
				#Ix2 += 

			except IndexError:
				area = polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1]

				x = (pow((polygon[i][1] - centroid[1]), 2) + 
					(polygon[i][1] - centroid[1]) * (polygon[0][1] - centroid[1]) + 
					pow((polygon[0][1] - centroid[1]), 2))

				y = (pow((polygon[i][0] - centroid[0]), 2) + 
					(polygon[i][0] - centroid[0]) * (polygon[0][0] - centroid[0]) + 
					pow((polygon[0][0] - centroid[0]), 2))

				xy = (((polygon[i][1]-centroid[1])*(polygon[0][0]-centroid[0])) + 
					(2*(polygon[i][1]-centroid[1])*(polygon[i][0]-centroid[0])) + 
					(2*(polygon[0][1]-centroid[1])*(polygon[0][0]-centroid[0])) + 
					((polygon[0][1]-centroid[1])*(polygon[i][0]-centroid[0])))

				I_x += x * area
				I_y += y * area
				I_xy += xy * area

				break

		I_x = abs(I_x) / 12
		I_y = abs(I_y) / 12
		I_xy = abs(I_xy) / 24

		#TODO fix torsional intertia

		#TODO torsional centrum is not always the same as the centroid, correct
		#TODO add a full stiffness matrix
		K = ReferenceFrame("K")
		N = inertia(K, 0, I_y, I_x, iyz=I_xy)
		#print(N)
		

		return I_x, I_y
	
	def get_polar_moment_of_inertia(self, b, h, polygon):
		"""Calculates the polar moment of inertia for a given polygon"""
		#TODO needs FEM implementation

		#Rectangular quick fix
		hb = h / b
		if hb <= 1:
			c = 0.22
		elif hb <= 2:
			c = 0.24
		elif hb <= 3:
			c = 0.26
		elif hb <= 4:
			c = 0.28
		elif hb <= 5:
			c = 0.29
		else:
			c = 0.31

		I_tor = (b**3 * h) * c
		return I_tor


class CoverUnit:

    def __init__(self):
        self.id = int()
        self.contact_points = [] # [id, unit type (e.g. beam), coordinates]


class StructuralUnit(Sections):

	def __init__(self, uuid):
		self.table_values = TableValues()
		self._init_vars()

		#TODO the UUID should be generated when the instance is created, not assigned from database
		self.id = uuid
		self.tvärsnitt = "rectangular"
		self.material = "C24"
		self.type = "solid timber"
		self.roof_beam_type = float()
		self.service_class = "S2"
		self.load_duration_class = "medium"
		self.enhetstyp = "beam"
		self.contact_points = [] # [id till angränsande, kontaktpunkt, vinkel till object, vinkel till världen]
		self.cover_contact_points = []
		#TODO refactor redundant variables
		self.timber_type = "Dressed Lumber"
		self.cross_section = "95x145"
		self.start_point = [0,0,0]
		self.end_point = [5,0,0]
		self.start_connectivity = {"e_x": False, "e_y": False, "e_z": False, "phi_x": False, "phi_y": True, "phi_z": True}
		self.end_connectivity = {"e_x": False, "e_y": False, "e_z": False, "phi_x": False, "phi_y": True, "phi_z": True}
		#TODO Add function for calculating the effective buckling lengths and store them here
		self.buckling_type = "placeholder"
		self.start_buckling_length = ("co_x", "co_y", "co_z")
		self.end_buckling_length = ("co_x", "co_y", "co_z")
		self.start_analytical_eccentricity = (0, 0, 0)
		self.end_analytical_eccentricity = (0, 0, 0)
		self.use_default_physical_alignment = False
		self.start_physical_eccentricity = (0, 0, 0)
		self.end_physical_eccentricity = (0, 0, 0)

		self.M_y = 1000 # [Nm]
		self.M_z = 1000 # [Nm]
		self.N = 1000 # [N]
		self.V = 1000 # [N]
		self.T = 1000 # [Nm]
		#TODO values for type, material etc must be input
		self.results = None

		self.prepare_for_calculation()

	def _init_vars(self):
		self.A = float()
		self.A_ef = float()
		self.A_f = float()
		self.A_net_v = float()
		self.C = float()
		self.E = float()
		self.E_0_05 = float()
		self.E_d = float()
		self.E_mean = float()
		self.E_mean_fin = float()
		self.F = float()
		self.F_A_Ed = float()
		self.F_A_min_d = float()
		self.F_ax_Ed = float()
		self.F_ax_Rd = float()
		self.F_ax_Rk = float()
		self.F_c = float()
		self.F_c_90_d = float()
		self.F_d = float()
		self.F_d_ser = float()
		self.F_Rd = float()
		self.F_i_c_Ed = float()
		self.F_i_t_Ed = float()
		self.F_vert_Ed = float()
		self.F_i_v_Rd = float()
		self.F_la = float()
		self.F_M_Ed = float()
		self.F_t = float()
		self.F_t_Rk = float()
		self.F_v_0_Rk = float()
		self.F_v_Ed = float()
		self.F_v_Rd = float()
		self.F_v_Rk = float()
		self.F_v_w_Ed = float()
		self.F_x_Ed = float()
		self.F_y_Ed = float()
		self.F_x_Rd = float()
		self.F_y_Rd = float()
		self.F_x_Rk = float()
		self.F_y_Rk = float()
		self.G_0_05 = float()
		self.G_d = float()
		self.G_mean = float()
		self.G_mean_fin = float()
		self.H = float()
		self.I = float()
		self.I_f = float()
		self.I_tor = float()
		self.I_z = float()
		self.K_ser = float()
		self.K_ser_fin = float()
		self.K_u = float()
		self.L_net_t = float()
		self.L_net_v = float()
		self.M_A_Ed = float()
		self.M_ap_d = float()
		self.M_d = float()
		self.M_y_crit = float()
		self.M_y_Rk = float()
		self.N = float()
		self.R_90_d = float()
		self.R_90_k = float()
		self.R_ax_d = float()
		self.R_ax_k = float()
		self.R_ax_alpha_k = float()
		self.R_d = float()
		self.R_ef_k = float()
		self.R_iv_d = float()
		self.R_k = float()
		self.R_sp_k = float()
		self.R_to_k = float()
		self.R_v_d = float()
		self.V = float()
		self.V_0 = float()
		self.V_u = float()
		self.V_I = float()
		self.W_y = float()
		self.X_d = float()
		self.X_k = float()
		# Lowercase
		self.a = float()
		self.a_1 = float()
		self.a_1_CG = float()
		self.a_2 = float()
		self.a_2_CG = float()
		self.a_3_c = float()
		self.a_3_t = float()
		self.a_4_c = float()
		self.a_4_t = float()
		self.a_bow = float()
		self.a_bow_perm = float()
		self.b = float()
		self.b_ef = float()
		self.b_i = float()
		self.b_net = float()
		self.b_w = float()
		self.d = float()
		self.d_I = float()
		self.d_c = float()
		self.d_ef = float()
		self.d_h = float()
		self.e = float()
		self.f_1 = float()
		self.f_h_i_k = float()
		self.f_a_0_0 = float()
		self.f_a_90_90 = float()
		self.f_a_alpha_beta_k = float()
		self.f_ax_k = float()
		self.f_c_0_k = float()
		self.f_c_0_d = float()
		self.f_c_w_d = float()
		self.f_f_c_d = float()
		self.f_c_90_d = float()
		self.f_c_90_k = float()
		self.f_f_t_d = float()
		self.f_h_k = float()
		self.f_head_k = float()
		self.f_I = float()
		self.f_m_k = float()
		self.f_m_d = float()
		self.f_m_y_d = float()
		self.f_m_z_d = float()
		self.f_m_alpha_d = float()
		self.f_t_0_d = float()
		self.f_t_0_k = float()
		self.f_t_90_d = float()
		self.f_t_w_d = float()
		self.f_u_k = float()
		self.f_v_0_d = float()
		self.f_v_ax_alpha_k = float()
		self.f_v_ax_90_k = float()
		self.f_v_d = float()
		self.h = float()
		self.h_ap = float()
		self.h_d = float()
		self.h_e = float()
		self.h_ef = float()
		self.h_f_c = float()
		self.h_f_t = float()
		self.h_rl = float()
		self.h_ru = float()
		self.h_w = float()
		self.i = float()
		self.k_5 = float()
		self.k_6 = float()
		self.k_7 = float()
		self.k_c_90 = float()
		self.k_c_y = float()
		self.k_c_z = float()
		self.k_cr = float()
		self.k_crit = float()
		self.k_d = float()
		self.k_def = float()
		self.k_dis = float()
		self.k_f_1 = float()
		self.k_f_2 = float()
		self.k_f_3 = float()
		self.k_h = float()
		self.k_i_q = float()
		self.k_m = float()
		self.k_m_alpha = float()
		self.k_mod = float()
		self.k_n = float()
		self.k_p = float()
		self.k_r = float()
		self.k_R_red = float()
		self.k_s = float()
		self.k_s_red = float()
		self.k_shape = float()
		self.k_sys = float()
		self.k_v = float()
		self.k_vol = float()
		self.k_y = float()
		self.k_z = float()
		self.l_a_min = float()
		self.l = float()
		self.l_A = float()
		self.l_ef_LTB = float()
		self.l_V = float()
		self.l_Z = float()
		self.m = float()
		self.n_40 = float()
		self.n_ef = float()
		self.p_d = float()
		self.q_i = float()
		self.r = float()
		self.s = float()
		self.s_0 = float()
		self.r_in = float()
		self.t = float()
		self.t_pen = float()
		self.u_creep = float()
		self.u_fin = float()
		self.u_fin_G = float()
		self.u_fin_Q1 = float()
		self.u_fin_Qi = float()
		self.u_inst = float()
		self.u_inst_G = float()
		self.u_inst_Q1 = float()
		self.u_inst_Qi = float()
		self.w_c = float()
		self.w_creep = float()
		self.w_fin = float()
		self.w_inst = float()
		self.w_net_fin = float()
		self.v = float()
		self.alpha = float()
		self.alpha_ap = float()
		self.beta = float()
		self.beta_c = float()
		self.gamma = float()
		self.gamma_M = float()
		self.lambda_y = float()
		self.lambda_z = float()
		self.lambda_rel_m = float()
		self.lambda_rel_y = float()
		self.lambda_rel_z = float()
		self.rho_a = float()
		self.rho_k = float()
		self.rho_m = float()
		self.rho_m_1 = float()
		self.rho_m_2 = float()
		self.sigma_c_0_d = float()
		self.sigma_c_90_d = float()
		self.sigma_c_alpha_d = float()
		self.sigma_f_c_d = float()
		self.sigma_f_c_max_d = float()
		self.sigma_f_t_d = float()
		self.sigma_f_t_max_d = float()
		self.sigma_k_1 = float()
		self.sigma_k_2 = float()
		self.sigma_k_3 = float()
		self.sigma_k_4 = float()
		self.sigma_m_crit = float()
		self.sigma_m_d = float()
		self.sigma_m_0_d = float()
		self.sigma_m_y_d = float()
		self.sigma_m_z_d = float()
		self.sigma_m_alpha_d = float()
		self.sigma_N = float()
		self.sigma_t = float()
		self.sigma_t_0_d = float()
		self.sigma_t_90_d = float()
		self.sigma_w_c_d = float()
		self.sigma_w_t_d = float()
		self.tao_d = float()
		self.tao_F_d = float()
		self.tao_M_d = float()
		self.tao_tor_d = float()
		self.theta = float()
		self.psi_0 = float()
		self.psi_2 = float()
		self.w = float()
		self.w_creep = float()
		self.w_inst = float()
		self.x = float()
		self.xi = float()

	def _prepare_for_xml(self, file_size="large"):
		"""Returns .xml formatted string.

		File_size: String; Whether complete information about the cross section 
						   or a compressed representation is to be exported.

		Return: String; 
		"""
		bar = Element("bar")
		bar.set("uuid", str(self.id))
		bar.set("last_change", "value")
		bar.set("action", "value")
		bar.set("type", str(self.enhetstyp))

		bar_part = Element("bar_part")
		bar.append(bar_part)
		bar_part.set("uuid", "value")
		bar_part.set("last_change", "value")
		bar_part.set("action", "value")
		bar_part.set("name", "value")

		if file_size == "small":
			bar_part.set("complex_material", "value")
			bar_part.set("complex_section", "value")

		elif file_size == "large":
			bar_part.set("cross_section_type", str(self.tvärsnitt))
			bar_part.set("material", str(self.material))
			bar_part.set("material_type", str(self.type))
			bar_part.set("service_class", str(self.service_class))
			bar_part.set("load_duration_class", str(self.load_duration_class))
			bar_part.set("cross_section_b", str(self.b))
			bar_part.set("cross_section_h", str(self.h))
			bar_part.set("cross_section_area", str(self.A))
			bar_part.set("moment_of_inertia_y", str(self.I_y))
			bar_part.set("moment_of_inertia_z", str(self.I_z))
			bar_part.set("length", str(self.l))

		bar_part.set("ecc_calc", "value")

		curve = Element("curve")
		bar_part.append(curve)
		curve.set("type", "placeholder")

		_start_point = Element("start_point")
		curve.append(_start_point)
		_start_point.set("x", str(self.start_point[0]))
		_start_point.set("y", str(self.start_point[1]))
		_start_point.set("z", str(self.start_point[2]))
		_end_point = Element("end_point")
		curve.append(_end_point)
		_end_point.set("x", str(self.end_point[0]))
		_end_point.set("y", str(self.end_point[1]))
		_end_point.set("z", str(self.end_point[2]))

		#print(self.start_point[0], self.end_point[0])

		#print(tostring(bar))

		local_y = Element("local_y")
		bar_part.append(local_y)
		local_y.set("x", "value")
		local_y.set("y", "value")
		local_y.set("z", "value")

		connectivity = Element("connectivity")
		bar_part.append(connectivity)
		connectivity.set("e_x", "value")
		connectivity.set("e_y", "value")
		connectivity.set("e_z", "value")
		connectivity.set("m_x", "value")
		connectivity.set("m_y", "value")
		connectivity.set("m_z", "value")
		bar_part.append(connectivity)
		connectivity.set("e_x", "value")
		connectivity.set("e_y", "value")
		connectivity.set("e_z", "value")
		connectivity.set("m_x", "value")
		connectivity.set("m_y", "value")
		connectivity.set("m_z", "value")

		eccentricity = Element("eccentricity")
		bar_part.append(eccentricity)
		eccentricity.set("use_default_physical_alignment", str(self.use_default_physical_alignment))

		analytical = Element("analytical")
		eccentricity.append(analytical)
		analytical.set("x", str(self.start_analytical_eccentricity[0]))
		analytical.set("y", str(self.start_analytical_eccentricity[1]))
		analytical.set("z", str(self.start_analytical_eccentricity[2]))
		eccentricity.append(analytical)
		analytical.set("x", str(self.end_analytical_eccentricity[0]))
		analytical.set("y", str(self.end_analytical_eccentricity[1]))
		analytical.set("z", str(self.end_analytical_eccentricity[2]))

		physical = Element("physical")
		eccentricity.append(physical)
		physical.set("x", "value")
		physical.set("y", "value")
		physical.set("z", "value")
		eccentricity.append(physical)
		physical.set("x", "value")
		physical.set("y", "value")
		physical.set("z", "value")

		#if bar has more than 2 supports:
			#include buckling data

		loads_part = Element("loads_part")
		bar.append(loads_part)
		loads_part.set("N", str(self.N))
		loads_part.set("V", str(self.V))
		loads_part.set("M_y", str(self.M_y))
		loads_part.set("M_z", str(self.M_z))
		loads_part.set("T", str(self.T))
		loads_part.set("uuid", "placeholder")


		result_part = Element("result_part")
		bar.append(result_part)
		result_part.set("bending_1", str(self.results.bending[0]))
		result_part.set("bending_2", str(self.results.bending[1]))
		result_part.set("shear", str(self.results.shear))
		result_part.set("torsion", str(self.results.torsion))
		result_part.set("uuid", "placeholder")

		#TODO must add results to string
		return bar

	def prepare_for_calculation(self):
		"""Saves all changes made to the instances dependent variables."""
		self.section, self.section_vertices = self.set_section(self.timber_type, self.cross_section)
		self.b, self.h = self.get_dimensions(self.section_vertices) #TODO only initialize when a new section type has been created
		self.r = sqrt(pow(self.h/2,2) + pow(self.b/2,2)) #TODO add general geometry function
		self.A = self.get_area(self.section_vertices)
		self.I_z, self.I_y = self.get_moment_of_inertia(self.section_vertices)
		self.I_tor = self.get_polar_moment_of_inertia(self.b, self.h, self.section_vertices)

		self.koordinater = array([self.start_point, self.end_point])
		#TODO förmodligen kommer längden läsas fel iom att den inte uppdateras vid skapandet av objektet
		self.l = sqrt(pow(self.koordinater[1][0] - self.koordinater[0][0], 2) +
		              pow(self.koordinater[1][1] - self.koordinater[0][1], 2) +
		              pow(self.koordinater[1][2] - self.koordinater[0][2], 2))
		self.k_mod = self.table_values.tabell_3_1(self.type, self.service_class, self.load_duration_class)
		self.rho_k = self.table_values.material_values_timber(self.material, "rho_k")
		self.gamma_M = self.table_values.tabell_2_3(self.type)
		self.f_t_0_k = self.table_values.material_values_timber(self.material, "f_t_0_k")
		self.f_c_0_k = self.table_values.material_values_timber(self.material, "f_c_0_k")
		self.f_c_90_k = self.table_values.material_values_timber(self.material, "f_c_90_k")
		self.k_c_90 = self.table_values.avsnitt_6_1_5("continuous support", "Solid softwood") #TODO skapa logik till detta val
		#TODO (A_ef) add units checker 
		self.A_ef = self.A / 2 # TODO placeholder. Lägg in geometri från anliggande element + logik
		self.f_m_k = self.table_values.material_values_timber(self.material, "f_m_k")
		self.k_m = self.table_values.avsnitt_6_1_6_2(self.tvärsnitt, self.type)
		self.f_v_k = self.table_values.material_values_timber(self.material, "f_v_k")
		self.E_0_05 = self.table_values.material_values_timber(self.material, "E_0_05")
		#self.G_0_05 = self.table_values.material_values_timber(self.material, "G_mean") #TODO ändra till G,005 ist för gmean
		self.G_0_05 = 463 #According to FEMDesign
		self.l_c = self.table_values.effektiv_längd_placeholder("ledadx2", self.l) #TODO implementera funktion när den skapas

		
class ClassicalMechanics:
	def __init__(self):
		pass

	def navier_stress_distribution(self, N=0, A=1, M_y=0, M_z=0, I_y=1, I_z=1, y=0, z=0):
		"""Returns the stress in the specified point.
		For correct stresses use right hand rule in the positive direction of the axes.
		"""
		return N/A + (M_z/I_z)*y - (M_y/I_y)*z

	def shear_stress(self, V, del_A, y, I, b):
		S = del_A * y
		tao = V*S / (I*b)

		return tao		


class SS_EN_1995_1_1(ClassicalMechanics):

	def __init__(self):
		super().__init__()
		self.table_values = TableValues()
		self.unit = StructuralUnit(000) # This is only for intelli-ref for variables

	def ekv_2_1(self, K_u, K_ser):
		K_u = 2/3 * K_ser

		return K_u

	def ekv_2_2(self, u_fin, u_fin_G, u_fin_Q1,u_fin_Qi):
		#TODO lägg till summa av alla Q
		u_fin = u_fin_G + u_fin_Q1 + u_fin_Qi

		return u_fin

	def ekv_2_3(self, u_fin_G, u_inst_G, k_def):
		u_fin_G = u_inst_G * (1 + k_def)

		return u_fin_G

	def ekv_2_4(self, u_fin_Q1, u_inst_Q1, psi_2_1, k_def):
		#TODO lägg till samtliga psivärden från eurocode 0, varje
		#TODO lastfall behöver ev. en egen class
		u_fin_Q1 = u_inst_Q1 * (1 + psi_2_1 * k_def)

		return u_fin_Q1

	def ekv_2_5(self, u_fin_Qi, u_inst_Qi, psi_2_i, k_def):
		#TODO samma som ekv 2.4 och ekv 2.2
		u_fin_Qi = u_inst_Qi * (psi_2_i * k_def)

		return u_fin_Qi

	def ekv_2_6(self, k_mod_1, k_mod_2):
		#TODO gäller om members har olika k_mod, ta hänsyn till detta
		k_mod = math.sqrt(k_mod_1 * k_mod_2)

		return k_mod

	def ekv_2_7(self, E_mean_fin, E_mean, k_def):
		E_mean_fin = E_mean / (1 + k_def)

		return E_mean_fin

	def ekv_2_8(self, G_mean_fin, G_mean, k_def):
		G_mean_fin = G_mean / (1 + k_def)

		return G_mean_fin

	def ekv_2_9(self, K_ser_fin, K_ser, k_def):
		K_ser_fin = K_ser / (1 + k_def)

		return K_ser_fin

	def ekv_2_10(self, E_mean_fin, E_mean, psi_2, k_def):
		E_mean_fin = E_mean / (1 + psi_2 * k_def)

		return E_mean_fin

	def ekv_2_11(self, G_mean_fin, G_mean, psi_2, k_def):
		G_mean_fin = G_mean / (1 + psi_2 * k_def)

		return G_mean_fin

	def ekv_2_12(self, K_ser_fin, K_ser, psi_2, k_def):
		K_ser_fin = K_ser / (1 + psi_2 * k_def)

		return K_ser_fin

	def ekv_2_13(self, k_def, k_def_1, k_def_2):
		#TODO gäller om members har olika k_mod, ta hänsyn till detta
		k_def = 2 * math.sqrt(k_def_1 * k_def_2)

		return k_def

	def ekv_2_14(self, X_k, k_h=1):
		"""Calculates X_d for a given X_k
		Params:
			X_k: characteristic value
			k_h: when applicable, else k_h=1"""
		return k_h * self.unit.k_mod * X_k / self.unit.gamma_M

	def ekv_2_15(self):
		"""E_d = E_mean / gamma_M"""
		return self.unit.E_mean / self.unit.gamma_M

	def ekv_2_16(self):
		"""G_d = G_mean / gamma_M"""
		return self.unit.G_mean / self.unit.gamma_M
	
	def ekv_3_1(self):
		"""
		For rectangular solid timber with a characteristic timber density A 700 kg/m3, the reference
		depth in bending or width (maximum cross-sectional dimension) in tension is 150 mm. For
		depths in bending or widths in tension of solid timber less than 150 mm the characteristic values
		for.fn,k and./t·,o.k may be increased by the factor kh , given by:
		Input variables:
			self.unit.rho_k
			self.unit.h
		Output:
			self.unit.k_h
		"""
		# Gäller solitt trä (f_m_k + f_t_0_k)
		if self.unit.rho_k <= 700 and self.unit.h < 150:
			self.unit.k_h = min(math.pow(150 / self.unit.h, 0.2), 1.3)
		else:
			self.unit.k_h = 1

		return self.unit.k_h

	def ekv_3_2(self):
		"""
		Input variables:
			self.unit.h
		Output:
			self.unit.k_h
		"""
		# Limträ (f_m_k + f_t_0_k)
		if self.unit.h < 600:
			self.unit.k_h = min(math.pow(600 / self.unit.h, 0.1), 1.1)
		else:
			self.unit.k_h = 1

		return self.unit.k_h

	def ekv_3_3(self):
		"""
		Input variables:
			self.unit.h
			self.unit.s
		Output:
			self.unit.k_h
		"""
		# LVL (f_m_k + f_t_0_k)
		self.unit.s = "placeholder" #TODO fixa exponeneten

		if self.unit.h < 300:
			self.unit.k_h = min(math.pow(300 / self.unit.h, self.unit.s), 1.2)
		else:
			self.unit.k_h = 1

		return self.unit.k_h

	def ekv_3_4(self):
		"""
		Input variables:
			self.unit.h
			self.unit.s
		Output:
			self.unit.k_l
		"""
		# LVL, längd (f_m_k + f_t_0_k)
		if self.unit.l < 3000:
			self.unit.k_l = min(math.pow(3000 / self.unit.l, (self.unit.s / 2)), 1.1)
		else:
			self.unit.k_l = 1

		return self.unit.k_l

	def ekv_5_1(self):
		"""
		Input variables:
			self.unit.h
		Output:
			self.unit.theta
		"""
		#TODO spåra upp var theta går in 
		if self.unit.h <= 5:
			self.unit.theta = 0.0005
		elif self.unit.h > 5:
			self.unit.theta = 0.0005 * math.sqrt(5 / self.unit.h)

		return self.unit.theta

	def ekv_5_2(self):
		"""
		Input variables:
			self.unit.l
		Output:
			self.unit.e
		"""
		self.unit.e = 0.0025 * self.unit.l

		return self.unit.e

	### 6.1.2 Tension parallel to the grain ###
	def ekv_6_1(self):
		"""
		The following expression shall be satisfied:
			self.unit.sigma_t_0_d / self.unit.f_t_0_d <= 1

		Output:
			self.unit.sigma_t_0_d / self.unit.f_t_0_d
		"""
		self.unit.sigma_t_0_d = self.ekv_6_36()
		self.unit.f_t_0_d = self.ekv_2_14(self.unit.f_t_0_k, self.unit.k_h)

		return self.unit.sigma_t_0_d / self.unit.f_t_0_d

	### 6.1.4 Compression parallel to the grain ###
	def ekv_6_2(self):
		"""
		The following expression shall be satisfied:
			self.unit.sigma_c_0_d / self.unit.f_c_0_d <= 1

		Output:
			# The abs() is because compression forces is defined as negative
			abs(self.unit.sigma_c_0_d / self.unit.f_c_0_d)
		"""
		self.unit.f_c_0_d = self.ekv_2_14(self.unit.f_c_0_k)
		self.unit.sigma_c_0_d = self.ekv_6_36()

		return abs(self.unit.sigma_c_0_d / self.unit.f_c_0_d)

	### 6.1.5 Compression perpendicular to the grain ###
	def ekv_6_3(self):
		"""
		The following expression shall be satisfied:
			self.unit.sigma_c_90_d / (self.unit.k_c_90 * self.unit.f_c_90_d) <= 1
		Output:
			self.unit.sigma_c_90_d / (self.unit.k_c_90 * self.unit.f_c_90_d)
		"""
		self.unit.f_c_90_d = self.ekv_2_14(self.unit.f_c_90_k)
		self.unit.sigma_c_90_d = self.ekv_6_4()
		
		return self.unit.sigma_c_90_d / (self.unit.k_c_90 * self.unit.f_c_90_d)

	def ekv_6_4(self):
		"""
		Input variables:
			self.unit.A_ef
		Output:
			self.unit.sigma_c_90_d
		"""
		self.F_c_90_d = 19000 # TODO placeholder. Lägg in krafer från andra element + logik
		self.unit.sigma_c_90_d = self.unit.F_c_90_d / self.unit.A_ef

		return self.unit.sigma_c_90_d

	#TODO Look for the missing equations (6.5-6.10)
	### 6.1.6 Bending ###
	def ekv_6_11(self):
		"""
		The following expressions shall be satisfied:
			sigma_m_y_d / f_m_y_d + k_m * sigma_m_z_d / f_m_z_d <= 1
			and
			ekv_6_12()

		Output:
			self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.k_m * self.unit.sigma_m_z_d / self.unit.f_m_z_d
		"""
		#TODO clean up
		self.unit.k_h = self.ekv_3_1()
		#TODO add k_sys (I don't understand excactly)
		self.unit.f_m_y_d = self.unit.f_m_z_d = self.ekv_2_14(self.unit.f_m_k, self.unit.k_h)
		self.unit.sigma_m_y_d = max(self.unit.M_y * self.unit.b/2 * 10e2 / self.unit.I_y, self.unit.M_y * (self.unit.h/-2) * 10e2 / self.unit.I_y)
		#TODO find out why 10e-7 and not 10e-6
		#TODO it shouldn't be b/2 and h/2, but biggest general distance from centroid to edge
		self.unit.sigma_m_y_d = 10e-7*self.navier_stress_distribution(
			M_y=self.unit.M_y, I_y=self.unit.I_y*10e-12, z=self.unit.b/2*10e-3)

		self.unit.sigma_m_z_d = 10e-7*self.navier_stress_distribution(
			M_z=self.unit.M_z, I_z=self.unit.I_z*10e-12, y=self.unit.h/2*10e-3)
		#TODO why is sigma_y bigger than sigma_z in FEMDesign?
		return self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.k_m * self.unit.sigma_m_z_d / self.unit.f_m_z_d

	def ekv_6_12(self):
		"""
		The following expressions shall be satisfied:
			k_m * sigma_m_y_d / f_m_y_d + sigma_m_z_d / f_m_z_d <= 1
			and
			ekv_6_11()
		Output:
			self.unit.k_m * self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.sigma_m_z_d / self.unit.f_m_z_d
		"""
		#TODO clean up
		self.unit.k_h = self.ekv_3_1()
		#TODO add k_sys (I don't understand excactly)
		self.unit.f_m_y_d = self.unit.k_mod * self.unit.k_h * self.unit.f_m_k / self.unit.gamma_M
		self.unit.f_m_z_d = self.unit.k_mod * self.unit.k_h * self.unit.f_m_k / self.unit.gamma_M
		#TODO find out why 10e2
		#TODO it shouldn't be b/2 and h/2, but biggest general distance from centroid to edge 
		self.unit.sigma_m_y_d = max(self.unit.M_y * self.unit.b/2 * 10e2 / self.unit.I_y, self.unit.M_y * (self.unit.h/-2) * 10e2 / self.unit.I_y)
		self.unit.sigma_m_z_d = max(self.unit.M_z * self.unit.h/2 * 10e2 / self.unit.I_z, self.unit.M_z * self.unit.h/-2 * 10e2 / self.unit.I_z)

		#TODO why is sigma_y bigger than sigma_z in FEMDesign?
		return self.unit.k_m * self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.sigma_m_z_d / self.unit.f_m_z_d

	### 6.1.7 Shear ###
	def ekv_6_13(self):
		"""
		Output:
			abs(self.unit.tao_d / self.unit.f_v_d)
		"""
		self.unit.f_v_d = self.ekv_2_14(self.unit.f_v_k)
		#TODO verify fvd, it's higher in FEMDesign

		#TODO the moment is 0 when the shear stress is at it's largest, where is the line?
		if self.unit.M_z != 0 or self.unit.M_y != 0:
			self.unit.b_ef = self.ekv_6_13_a()
		else:
			self.unit.b_ef = self.unit.b

		#TODO change implementations when FEM module is deployed
		self.unit.tao_d = self.shear_stress(self.unit.V, self.unit.h/2*self.unit.b, 
			self.unit.h/4, self.unit.I_y, self.unit.b_ef)

		#TODO implement clause (3)
		ratio = abs(self.unit.tao_d / (self.unit.f_v_d))

		return ratio

	def ekv_6_13_a(self):
		"""
		Variables used:
			self.unit.type
			self.unit.k_cr
		Output:
			self.unit.b_ef
		"""
		# k_cr is subject to national annexes
		if self.unit.type == "solid timber" or self.unit.type == "glued laminated timber":
		    self.unit.k_cr = 0.67
		else:
		    self.unit.k_cr = 1

		self.unit.b_ef = self.unit.k_cr * self.unit.b

		return self.unit.b_ef

	### 6.1.8 Torsion ###
	def ekv_6_14(self):
		"""
		Output:
			abs(self.unit.tao_tor_d / (self.unit.k_shape * self.unit.f_v_d))
		"""
		self.unit.f_v_d = self.ekv_2_14(self.unit.f_v_k)
		self.unit.k_shape = self.ekv_6_15()
		self.unit.tao_tor_d = self.unit.T*1e03 * self.unit.r / self.unit.I_tor

		return abs(self.unit.tao_tor_d / (self.unit.k_shape * self.unit.f_v_d))

	def ekv_6_15(self):
		"""
		Variables used:
			self.unit.tvärsnitt
		Output:
			self.unit.k_shape
		"""
		#TODO general polygon function
		if self.unit.tvärsnitt == "rectangular":
			self.unit.k_shape = min(1 + 0.15 * self.unit.h / self.unit.b, 2)
		elif self.unit.tvärsnitt == "circular":
			self.unit.k_shape = 1.2

		return self.unit.k_shape

	### 6.2.2 Compression stresses at an angle to the grain ###
	def ekv_6_16(self):
		"""
		Output:
			Bool
		"""
		#TODO kontrollera ekvationen
		if self.unit.sigma_c_alpha_d <= self.unit.f_c_0_d / ((self.unit.f_c_0_d / (self.unit.k_c_90 * self.unit.f_c_90_d)) * (math.pow(math.sin(self.unit.alpha), 2) + math.pow(math.cos(self.unit.alpha), 2))):
			return True
		else:
			return False

	### 6.2.3 Combined bending and axial tension ###
	def ekv_6_17(self):
		"""
		Output:
			self.unit.sigma_t_0_d / self.unit.f_t_0_d + self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.k_m * self.unit.sigma_m_z_d / self.unit.f_m_z_d
		"""
		#TODO kontrollera ekvation
		print("6.17")
		self.unit.k_h = self.ekv_3_1()
		#TODO Add k_sys 
		self.unit.f_m_y_d = self.unit.f_m_z_d = self.unit.k_mod * self.unit.k_h * self.unit.f_m_k / self.unit.gamma_M
		self.unit.f_t_0_d = self.unit.k_mod * self.unit.k_h * self.unit.f_t_0_k / self.unit.gamma_M
		#TODO fattar inte varför 10e2 och inte 10e3
		self.unit.sigma_t_0_d = self.ekv_6_36()
		self.unit.sigma_m_y_d = max(self.unit.M_y * self.unit.b/2 * 10e2 / self.unit.I_y, self.unit.M_y * (self.unit.b/-2) * 10e2 / self.unit.I_y)
		self.unit.sigma_m_z_d = max(self.unit.M_z * self.unit.h/2 * 10e2 / self.unit.I_z, self.unit.M_z * self.unit.h/-2 * 10e2 / self.unit.I_z)

		return self.unit.sigma_t_0_d / self.unit.f_t_0_d + self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.k_m * self.unit.sigma_m_z_d / self.unit.f_m_z_d
	
	def ekv_6_18(self):
		"""
		Output:
			self.unit.sigma_t_0_d / self.unit.f_t_0_d + self.unit.k_m * self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.sigma_m_z_d / self.unit.f_m_z_d
		"""
		#TODO kontrollera ekvation
		self.unit.k_h = self.ekv_3_1()
		#TODO lägga in k_sys (Jag försåtr inte riktigt)
		self.unit.f_m_y_d = self.unit.f_m_z_d = self.unit.k_mod * self.unit.k_h * self.unit.f_m_k / self.unit.gamma_M
		self.unit.f_t_0_d = self.unit.k_mod * self.unit.k_h * self.unit.f_t_0_k / self.unit.gamma_M
		#TODO fattar inte varför 10e2 och inte 10e3
		self.unit.sigma_m_y_d = max(self.unit.M_y * self.unit.b/2 * 10e2 / self.unit.I_y, self.unit.M_y * (self.unit.b/-2) * 10e2 / self.unit.I_y)
		self.unit.sigma_m_z_d = max(self.unit.M_z * self.unit.h/2 * 10e2 / self.unit.I_z, self.unit.M_z * self.unit.h/-2 * 10e2 / self.unit.I_z)
		self.unit.sigma_t_0_d = self.ekv_6_36()

		return self.unit.sigma_t_0_d / self.unit.f_t_0_d + self.unit.k_m * self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.sigma_m_z_d / self.unit.f_m_z_d

	### 6.2.4 Combined bending and axial compression ###
	def ekv_6_19(self):
		"""
		Output:
			math.pow((self.unit.sigma_c_0_d / self.unit.f_c_0_d), 2) + \
							self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.k_m * self.unit.sigma_m_z_d / self.unit.f_m_z_d
		"""
		#TODO kontrollera ekvation
		#TODO Slutkontroll
		#TODO lägga in k_sys (Jag försåtr inte riktigt)
		self.unit.k_h = self.ekv_3_1()
		self.unit.f_m_y_d = self.unit.f_m_z_d = self.unit.k_mod * self.unit.k_h * self.unit.f_m_k / self.unit.gamma_M
		self.unit.f_c_0_d = self.unit.k_mod * self.unit.k_h * self.unit.f_c_0_k / self.unit.gamma_M
		#TODO fattar inte varför 10e2 och inte 10e3: 1e3
		self.unit.sigma_m_y_d = max(self.unit.M_y * self.unit.b/2 * 10e2 / self.unit.I_y, self.unit.M_y * (self.unit.b/-2) * 10e2 / self.unit.I_y)
		self.unit.sigma_m_z_d = max(self.unit.M_z * self.unit.h/2 * 10e2 / self.unit.I_z, self.unit.M_z * self.unit.h/-2 * 10e2 / self.unit.I_z)
		self.unit.sigma_c_0_d = self.ekv_6_36()

		return math.pow((self.unit.sigma_c_0_d / self.unit.f_c_0_d), 2) + \
							self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.k_m * self.unit.sigma_m_z_d / self.unit.f_m_z_d

	def ekv_6_20(self):
		"""
		Output:
			math.pow((self.unit.sigma_c_0_d / self.unit.f_c_0_d), 2) + self.unit.k_m * self.unit.sigma_m_y_d / self.unit.f_m_y_d + \
							self.unit.sigma_m_z_d / self.unit.f_m_z_d
		"""
		#TODO kontrollera ekvation
		#TODO Slutkontroll
		self.unit.k_h = self.ekv_3_1()
		#TODO lägga in k_sys (Jag försåtr inte riktigt)
		self.unit.f_m_y_d = self.unit.f_m_z_d = self.unit.k_mod * self.unit.k_h * self.unit.f_m_k / self.unit.gamma_M
		self.unit.f_c_0_d = self.unit.k_mod * self.unit.k_h * self.unit.f_c_0_k / self.unit.gamma_M
		#TODO fattar inte varför 10e2 och inte 10e3
		self.unit.sigma_m_y_d = max(self.unit.M_y * self.unit.b/2 * 10e2 / self.unit.I_y, self.unit.M_y * (self.unit.b/-2) * 10e2 / self.unit.I_y)
		self.unit.sigma_m_z_d = max(self.unit.M_z * self.unit.h/2 * 10e2 / self.unit.I_z, self.unit.M_z * self.unit.h/-2 * 10e2 / self.unit.I_z)
		self.unit.sigma_c_0_d = self.ekv_6_36()

		return math.pow((self.unit.sigma_c_0_d / self.unit.f_c_0_d), 2) + self.unit.k_m * self.unit.sigma_m_y_d / self.unit.f_m_y_d + \
							self.unit.sigma_m_z_d / self.unit.f_m_z_d

	### 6.3.2 Columns subjected to either compression or combined compression and bending ###
	def ekv_6_21(self):
		"""
		Variables used:
			self.unit.f_c_0_k
			self.unit.E_0_05
			self.unit.i_y
			self.unit.l_c
			self.unit.lambda_y
			self.unit.lambda_rel_y
		Output:
			self.unit.lambda_rel_y
		"""
		#TODO general calculation of i
		#TODO fix units
		self.unit.i_y = self.unit.b*10e-6 / math.sqrt(12)
		self.unit.lambda_y = self.unit.l_c / self.unit.i_y
		self.unit.lambda_rel_y = self.unit.lambda_y / math.pi * math.sqrt(self.unit.f_c_0_k / (self.unit.E_0_05*10e3))

		return self.unit.lambda_rel_y

	def ekv_6_22(self):
		"""
		Variables used:
			self.unit.f_c_0_k
			self.unit.E_0_05
			self.unit.i_z
			self.unit.lambda_z
		Output:
			self.unit.lambda_rel_z
		"""
		#TODO general calculation of i
		#TODO fix units
		self.unit.i_z = self.unit.h*10e-6 / math.sqrt(12)
		self.unit.lambda_z = self.unit.l_c / self.unit.i_z
		self.unit.lambda_rel_z = self.unit.lambda_z / math.pi * math.sqrt(self.unit.f_c_0_k / (self.unit.E_0_05*10e3))

		return self.unit.lambda_rel_z

	def ekv_6_23(self):
		"""
		Output:
			math.pow((self.unit.sigma_c_0_d / self.unit.f_c_0_d), 2) + \
							self.unit.sigma_m_y_d / self.unit.f_m_y_d + self.unit.k_m * self.sunit.sigma_m_z_d / self.unit.f_m_z_d
		"""
		#TODO fix units
		self.unit.k_h = self.ekv_3_1()
		self.unit.k_c_y = self.ekv_6_25()
		#TODO Add k_sys
		self.unit.f_m_y_d = self.unit.f_m_z_d = self.ekv_2_14(self.unit.f_m_k, self.unit.k_h)
		#TODO why 10e-7 not -6?
		#TODO check if the "max()" behaviour is suitable
		self.unit.sigma_m_y_d = max(10e-7*self.navier_stress_distribution(
			M_y=self.unit.M_y, I_y=self.unit.I_y*10e-12, z=self.unit.b/2*10e-3),
			10e-7*self.navier_stress_distribution(
			M_y=self.unit.M_y, I_y=self.unit.I_y*10e-12, z=-self.unit.b/2*10e-3))

		self.unit.sigma_m_z_d = 10e-7*self.navier_stress_distribution(
			M_z=self.unit.M_z, I_z=self.unit.I_z*10e-12, y=self.unit.h/2*10e-3)
		
		self.unit.sigma_c_0_d = self.ekv_6_36()
		self.unit.f_m_y_d = 18.79

		return (abs(self.unit.sigma_c_0_d) / (self.unit.k_c_y * self.unit.f_c_0_d) + 
				self.unit.sigma_m_y_d / self.unit.f_m_y_d + 
				self.unit.k_m * self.unit.sigma_m_z_d / self.unit.f_m_z_d)
		
	def ekv_6_24(self):
		"""
		Output:
			math.pow((self.unit.sigma_c_0_d / self.unit.f_c_0_d), 2) + self.unit.k_m * self.unit.sigma_m_y_d / self.unit.f_m_y_d + \
							self.unit.sigma_m_z_d / self.unit.f_m_z_d
		"""
		#TODO kontrollera ekvation
		self.unit.k_h = self.ekv_3_1()
		#TODO lägga in k_sys (Jag försåtr inte riktigt)
		self.unit.k_c_z = self.ekv_6_26()
		self.unit.f_m_y_d = self.unit.f_m_z_d = self.unit.k_mod * self.unit.k_h * self.unit.f_m_k / self.unit.gamma_M
		self.unit.f_c_0_d = self.unit.k_mod * self.unit.k_h * self.unit.f_c_0_k / self.unit.gamma_M
		#TODO fattar inte varför 10e2 och inte 10e3
		#TODO fmyd in FEMdesign > this, why?
		self.unit.sigma_m_y_d = max(self.unit.M_y * self.unit.b/2 * 10e2 / self.unit.I_y, self.unit.M_y * (self.unit.b/-2) * 10e2 / self.unit.I_y)
		self.unit.sigma_m_z_d = max(self.unit.M_z * self.unit.h/2 * 10e2 / self.unit.I_z, self.unit.M_z * self.unit.h/-2 * 10e2 / self.unit.I_z)
		self.unit.sigma_c_0_d = self.ekv_6_36()

		return (abs(self.unit.sigma_c_0_d) / (self.unit.k_c_z * self.unit.f_c_0_d) + 
				self.unit.k_m * self.unit.sigma_m_y_d / self.unit.f_m_y_d + 
				self.unit.sigma_m_z_d / self.unit.f_m_z_d)

	def ekv_6_25(self):
		"""
		Output:
			self.unit.k_c_y
		"""
		#TODO kontrollera ekvation
		self.unit.k_y = self.ekv_6_27()
		self.unit.k_c_y = 1 / (self.unit.k_y + math.sqrt(math.pow(self.unit.k_y, 2) - math.pow(self.unit.lambda_rel_y, 2)))

		return self.unit.k_c_y

	def ekv_6_26(self):
		"""
		Variables used:
			self.unit.k_z
		Output:
			self.unit.k_c_z
		"""
		#TODO kontrollera ekvation
		self.unit.k_z = self.ekv_6_28()
		self.unit.k_c_z = 1 / (self.unit.k_z + math.sqrt(math.pow(self.unit.k_z, 2) - math.pow(self.unit.lambda_rel_z, 2)))

		return self.unit.k_c_z

	def ekv_6_27(self):
		"""
		Output:
			self.unit.k_y
		"""
		#TODO kontrollera ekvation
		self.unit.beta_c = self.ekv_6_29()
		self.unit.k_y = 0.5 * (1 + self.unit.beta_c * (self.unit.lambda_rel_y - 0.3) + math.pow(self.unit.lambda_rel_y, 2))

		return self.unit.k_y

	def ekv_6_28(self):
		"""
		Output:
			self.unit.k_z
		"""
		#TODO kontrollera ekvation
		self.unit.beta_c = self.ekv_6_29()
		self.unit.lambda_rel_z = self.ekv_6_22()
		self.unit.k_z = 0.5 * (1 + self.unit.beta_c * (self.unit.lambda_rel_z - 0.3) + math.pow(self.unit.lambda_rel_z, 2))

		return self.unit.k_z

	def ekv_6_29(self):
		"""
		Output:
			self.unit.beta_c
		"""
		if self.unit.type == "solid timber":
			self.unit.beta_c = 0.2
		elif self.unit.type == "glued laminated timber" or "LVL":
			self.unit.beta_c = 0.1

		return self.unit.beta_c

	### 6.3.3 Beams subjected to either bending or combined bending and compression ###
	def ekv_6_30(self):
		"""
		Output:
			self.unit.lambda_rel_m
		"""
		self.unit.sigma_m_crit = self.ekv_6_31()
		self.unit.lambda_rel_m = math.sqrt(self.unit.f_m_k / self.unit.sigma_m_crit)

		return self.unit.lambda_rel_m

	def ekv_6_31(self):
		"""
		Output:
			self.unit.sigma_m_crit
		"""
		#TODO fix units
		#TODO function must be created to take in to account the different load sides (currently "compression")
		self.unit.l_ef_LTB = self.table_values.tabell_6_1(
			self.unit.l, "Simply supported", "Uniformly distributed load", True, True, "compression", self.unit.h)
		#TODO kontrollera ekvation
		self.unit.W_z = self.unit.I_z / self.unit.h * 2
		self.unit.sigma_m_crit = (math.pi * math.sqrt(self.unit.E_0_05 * self.unit.I_y * self.unit.G_0_05 * self.unit.I_tor) 
			/ (self.unit.l_ef_LTB*1e3 * self.unit.W_z))

		return self.unit.sigma_m_crit

	def ekv_6_32(self):
		"""
		Output:
			self.unit.sigma_m_crit
		"""
		#TODO kontrollera ekvation
		self.unit.sigma_m_crit = 0.78 * math.pow(self.unit.b, 2) / (self.unit.h * self.unit.l_ef_LTB) * self.unit.E_0_05

		return self.unit.sigma_m_crit

	def ekv_6_33(self):
		"""
		Output:
			self.unit.sigma_m_z_d / (self.unit.k_crit * self.unit.f_m_z_d)
		"""
		self.unit.k_h = self.ekv_3_1()
		self.unit.f_m_z_d = self.unit.k_mod * self.unit.k_h * self.unit.f_m_k / self.unit.gamma_M
		self.unit.k_crit = self.ekv_6_34()
		self.unit.sigma_m_z_d = max(self.unit.M_z * self.unit.h/2 * 1e3 / self.unit.I_z, 
			self.unit.M_z * self.unit.h/-2 * 1e3 / self.unit.I_z)
		ratio = self.unit.sigma_m_z_d / (self.unit.k_crit * self.unit.f_m_z_d)
		
		return ratio

	def ekv_6_34(self, supported = False):
		"""
		Variables used:
			supported
			self.unit.lambda_rel_m
		Output:
			self.unit.k_crit
		"""
		#TODO logic for if supported beam
		if supported == False:
			self.unit.lambda_rel_m = self.ekv_6_30()

			if self.unit.lambda_rel_m <= 0.75:
				self.unit.k_crit = 1
			elif 0.75 < self.unit.lambda_rel_m <= 1.4:
				self.unit.k_crit = 1.56 - 0.75 * self.unit.lambda_rel_m
			elif 1.4 < self.unit.lambda_rel_m:
				self.unit.k_crit = 1 / math.pow(self.unit.lambda_rel_m, 2)
		else:
			self.unit.k_crit = 1

		return self.unit.k_crit

	def ekv_6_35(self):
		"""
		Output:
			math.pow((self.unit.sigma_m_z_d / (self.unit.k_crit * self.unit.f_m_z_d)), 2) + self.unit.sigma_c_0_d / (self.unit.k_c_z * self.unit.f_c_0_d)
		"""
		#TODO kontrollera ekvation
		self.unit.k_h = self.ekv_3_1()
		self.unit.f_m_z_d = self.ekv_2_14(self.unit.f_m_k, self.unit.k_h)
		self.unit.k_crit = self.ekv_6_34()
		# max() to get highest tension
		#TODO fix units
		#TODO general 
		self.unit.sigma_m_z_d = max(self.navier_stress_distribution(M_z=1e3*self.unit.M_z, I_z=self.unit.I_z, y=self.unit.h/2),
								self.navier_stress_distribution(M_z=1e3*self.unit.M_z, I_z=self.unit.I_z, y=self.unit.h/2))
		self.unit.sigma_c_0_d = abs(self.ekv_6_36())
		self.unit.k_c_z = self.ekv_6_26()
		self.unit.f_c_0_d = self.ekv_2_14(self.unit.f_c_0_k, self.unit.k_h)

		ratio = (math.pow((self.unit.sigma_m_z_d / (self.unit.k_crit * self.unit.f_m_z_d)), 2) + 
			self.unit.sigma_c_0_d / (self.unit.k_c_y * self.unit.f_c_0_d))

		return ratio

	def ekv_6_36(self):
		"""
		Variables used:
			self.unit.N
			self.unit.A
		Output:
			self.unit.sigma_N
		"""
		self.unit.sigma_N = self.unit.N / self.unit.A

		return self.unit.sigma_N

	def ekv_6_37(self):
		"""
		Variables used:
			self.unit.M_d
			self.unit.b
			self.unit.h
		Output:
			self.unit.sigma_m_alpha_d or self.unit.sigma_m_0_d ((?) TODO)
		"""
		self.unit.sigma_m_alpha_d = self.unit.sigma_m_0_d = 6 * self.unit.M_d / (self.unit.b * pow(self.unit.h, 2))
		#TODO vilken ska returneras? logik
		return self.unit.sigma_m_alpha_d

	def ekv_6_38(self):
		"""
		Variables used:
			self.unit.sigma_m_alpha_d
			self.unit.k_m_alpha
			self.unit.f_m_d
		Output:
			Bool
		"""
		if self.unit.sigma_m_alpha_d <= self.unit.k_m_alpha * self.unit.f_m_d:
			return True
		else:
			return False

	def ekv_6_39(self):
		"""
		Variables used:
			self.unit.f_m_d
			self.unit.f_v_d
			self.unit.alpha
			self.unit.f_t_90_d
		Output:
			self.unit.k_m_alpha
		"""
		#TODO kontrollera ekvation
		self.unit.k_m_alpha = 1 / math.sqrt(1 + math.pow(( self.unit.f_m_d / (0.75 * self.unit.f_v_d) * math.tan(self.unit.alpha)), 2) +
										math.pow(self.unit.f_m_d / self.unit.f_t_90_d * pow(math.tan(self.unit.alpha), 2), 2))

		return self.unit.k_m_alpha

	def ekv_6_40(self):
		"""
		Variables used:
			self.unit.f_m_d
			self.unit.f_v_d
			self.unit.alpha
			self.unit.f_t_90_d
		Output:
			self.unit.k_m_alpha
		"""
		#TODO kontrollera ekvation
		self.unit.k_m_alpha = 1 / math.sqrt(1 + math.pow(( self.unit.f_m_d / (1.5 * self.unit.f_v_d) * math.tan(self.unit.alpha)), 2) +
										math.pow(self.unit.f_m_d / self.unit.f_t_90_d * pow(math.tan(self.unit.alpha), 2), 2))

		return self.unit.k_m_alpha

	def ekv_6_41(self):
		"""
		Variables used:
			self.unit.sigma_m_d
			self.unit.k_r
			self.unit.f_m_d
		Output:
			Bool
		"""
		if self.unit.sigma_m_d <= self.unit.k_r * self.unit.f_m_d:
			return True
		else:
			return False

	def ekv_6_42(self):
		"""
		Variables used:
			self.unit.k_l
			self.unit.M_ap_d
			self.unit.b
			self.unit.h_ap
		Output:
			self.unit.sigma_m_d
		"""
		#TODO kontrollera ekvation
		self.unit.sigma_m_d = self.unit.k_l * 6 * self.unit.M_ap_d / (self.unit.b * math.pow(self.unit.h_ap, 2))

		return self.unit.sigma_m_d

	def ekv_6_43(self):
		"""
		Variables used:
			self.unit.k_1
			self.unit.k_2
			self.unit.k_3
			self.unit.k_4
			self.unit.h_ap
			self.unit.r
		Output:
			self.unit.k_l
		"""
		self.unit.k_l = self.unit.k_1 + self.unit.k_2 * (self.unit.h_ap / self.unit.r) + self.unit.k_3 * math.pow((self.unit.h_ap / self.unit.r), 2) + self.unit.k_4 * math.pow((self.unit.h_ap / self.unit.r), 3)

		return self.unit.k_l

	def ekv_6_44(self):
		"""
		Variables used:
			self.unit.alpha_ap
		Output:
			self.unit.k_1	
		"""
		#TODO kontrollera ekvation
		self.unit.k_1 = 1 + 1.4 * math.tan(self.unit.alpha_ap) + 5.4 * math.pow(math.tan(self.unit.alpha_ap), 2)

		return self.unit.k_1

	def ekv_6_45(self):
		"""
		Variables used:
			self.unit.alpha_ap
		Output:
			self.unit.k_2	
		"""
		self.unit.k_2 = 0.35 - 8 * math.tan(self.unit.alpha_ap)

		return self.unit.k_2

	def ekv_6_46(self):
		"""
		Variables used:
			self.unit.alpha_ap
		Output:
			self.unit.k_3	
		"""
		#TODO kontrollera ekvation
		self.unit.k_3 = 0.6 + 8.3 * math.tan(self.unit.alpha_ap) - 7.8 * math.pow(math.tan(self.unit.alpha_ap), 2)

		return self.unit.k_3

	def ekv_6_47(self):
		"""
		Variables used:
			self.unit.alpha_ap
		Output:
			self.unit.k_4	
		"""
		self.unit.k_4 = 6 * math.pow(math.tan(self.unit.alpha_ap), 2)

		return self.unit.k_4

	def ekv_6_48(self):
		"""
		Variables used:
			self.unit.r_in
			self.unit.h_ap
		Output:
			self.unit.r
		"""
		self.unit.r = self.unit.r_in + 0.5 * self.unit.h_ap

		return self.unit.r

	def ekv_6_49(self):
		"""
		Variables used:
			self.unit.r_in
			self.unit.t
		Output:
			self.unit.k_r
		"""
		if self.unit.r_in / self.unit.t < 240:
			self.unit.k_r = 0.76 + 0.001 * self.unit.r_in / self.unit.t
		elif self.unit.r_in / self.unit.t >= 240:
			self.unit.k_r = 1

		return self.unit.k_r

	def ekv_6_50(self):
		"""
		Variables used:
			self.unit.sigma_t
			self.unit.k_dis
			self.unit.k_vol
			self.unit.f_t_90_d
		Output:
			Bool
		"""
		if self.unit.sigma_t <= self.unit.k_dis * self.unit.k_vol * self.unit.f_t_90_d:
			return True
		else:
			return False

	def ekv_6_51(self):
		"""
		Variables used:
			self.unit.wood_type
			self.unit.V_0
			self.unit.V
		Output:
			self.unit.k_vol
		"""
		#TODO fixa wood_type()
		if self.unit.type == "solid timber":
			self.unit.k_vol = 1
		elif self.unit.type == "glued laminated timber" or "LVL":
			self.unit.k_vol = math.pow((self.unit.V_0 / self.unit.V), 0.2)

		return self.unit.k_vol

	def roof_beam_type(self):
		"""
		Variables used:
			"placeholder"
		Output:
			"placeholder"
		"""
		return "placeholder"

	def ekv_6_52(self):
		"""
		Variables used:
			self.unit.roof_beam_type
		Output:
			self.unit.k_dis
		"""
        #TODO fixa en funktion som avgör takstolens typ
		if self.unit.roof_beam_type == "double tapered" or "curved":
			self.unit.k_dis = 1.4
		elif self.roof_beam_type() == "pitched cambered":
			self.unit.k_dis = 1.7

		return self.unit.k_dis

	def ekv_6_53(self):
		"""
		Output:
			Bool
		"""
		if self.unit.tao_d / self.unit.f_v_d + self.unit.sigma_t_90_d / (self.unit.k_dis * self.unit.k_vol * self.unit.f_t_90_d) <= 1:
			return True
		else:
			return False

	def ekv_6_54(self):
		"""
		Output:
			self.unit.sigma_t_90_d
		"""
		#TODO kontrollera ekvation
		self.unit.sigma_t_90_d = self.unit.k_p * 6 * self.unit.M_ap_d / (self.unit.b * math.pow(self.unit.h_ap, 2))

		return self.unit.sigma_t_90_d

	def ekv_6_55(self):
		"""
		Variables used:
			self.unit.k_p
			self.unit.M_ap_d
			self.unit.b
			self.unit.h_ap
			self.unit.p_d
		Output:
			self.unit.sigma_t_90_d
		"""
		#TODO kontrollera ekvation
		self.unit.sigma_t_90_d = self.unit.k_p * 6 * self.unit.M_ap_d / (self.unit.b * math.pow(self.unit.h_ap, 2)) - 0.6 * self.unit.p_d / self.unit.b

		return self.unit.sigma_t_90_d

	def ekv_6_56(self):
		"""
		Variables used:
			self.unit.k_5
			self.unit.k_6
			self.unit.h_ap
			self.unit.r
			self.unit.k_7
			self.unit.h_ap
		Output:
			self.unit.k_p
		"""
		#TODO kotnrollera ekvation
		self.unit.k_p = self.unit.k_5 + self.unit.k_6 * (self.unit.h_ap / self.unit.r) + self.unit.k_7 * (math.pow((self.unit.h_ap / self.unit.r), 2))

		return self.unit.k_p

	def ekv_6_57(self):
		"""
		Variables used:
			self.unit.alpha_ap
		Output:
			self.unit.k_5
		"""
		self.unit.k_5 = 0.2 * math.tan(self.unit.alpha_ap)

		return self.unit.k_5

	def ekv_6_58(self):
		"""
		Variables used:
			self.unit.alpha_ap
		Output:
			self.unit.k_6
		"""
		#TODO kontrollera ekvation
		self.unit.k_6 = 0.25 - 1.5 * math.tan(self.unit.alpha_ap) + 2.6 * math.pow(math.tan(self.unit.alpha_ap), 2)

		return self.unit.k_6

	def ekv_6_59(self):
		"""
		Variables used:
			self.unit.alpha_ap
		Output:
			self.unit.k_7
		"""
		#TODO kontrollera ekvation
		self.unit.k_7 = 2.1 * math.tan(self.unit.alpha_ap) - 4 * math.pow(math.tan(self.unit.alpha_ap), 2)

		return self.unit.k_7

	def ekv_6_60(self):
		"""
		Variables used:
			self.unit.tao_d
			self.unit.V
			self.unit.b
			self.unit.h_ef
		Output:
			Bool
		"""
		self.unit.tao_d = 1.5 * self.unit.V / (self.unit.b * self.unit.h_ef)

		if self.unit.tao_d <= self.unit.k_v * self.unit.f_v_d:
			return True
		else:
			return False

	def beam_notch_side(self):
		"""
		Variables used:
			placeholder
		Output:
			placeholder
		"""
		return "placeholder"

	def ekv_6_61(self):
		"""
		Variables used:
			self.beam_notch_side
		Output:
			self.unit.k_v
		"""
		#TODO kontrollera ekvationer
		if self.beam_notch_side() == "opposite":
			self.unit.k_v = 1

		return self.unit.k_v

	def ekv_6_62(self):
		"""
		Variables used:
			self.beam_notch_side
			self.unit.k_n
			self.unit.i
			self.unit.h
			self.unit.alpha
			self.unit.x
		Output:
			self.unit.k_v
		"""
		#TODO kontrollera ekvationer
		if self.beam_notch_side() == "same":
			self.unit.k_v = min((self.unit.k_n * (1 + 1.1 * math.pow(self.unit.i, 1.5) / math.sqrt(self.unit.h)) /
							(math.sqrt(self.unit.h) * (math.sqrt(self.unit.alpha * (1 - self.unit.alpha)) + 0.8 * (self.unit.x / self.unit.h) * math.sqrt(1 / self.unit.alpha - pow(self.unit.alpha, 2))))),
							1)

		return self.unit.k_v

	def ekv_6_63(self):
		"""
		Variables used:
			self.unit.wood_type
		Output:
			self.unit.k_n
		"""
		if self.unit.type == "LVL":
			self.unit.k_n = 4.5
		elif self.unit.type == "solid timber":
			self.unit.k_n = 5
		elif self.unit.type == "glued laminated timber":
			self.unit.k_n = 6.5

		return self.unit.k_n

	def ekv_7_1(self):
		"""
		Variables used:
			self.unit.rho_m_1
			self.unit.rho_m_2
		Output:
			self.unit.rho_m
		"""
		#TODO add rho_i function (kwargs?)
		self.unit.rho_m = math.sqrt(self.unit.rho_m_1 * self.unit.rho_m_2)

		return self.unit.rho_m

	def ekv_7_2(self):
		"""
		Variables used:
			self.w_inst
			self.w_creep
			self.w_c
		Output:
			self.unit.w_net_fin
		"""
		#TODO Add logic
		self.unit.w_net_fin = self.unit.w_inst + self.unit.w_creep - self.unit.w_c 
		self.unit.w_net_fin = self.unit.w_inst - self.unit.w_c
		self.unit.w_net_fin = self.unit.w_inst - self.unit.w_c

		return self.unit.w_net_fin

	def ekv_7_3(self):
		"""
		Variables used:
			self.unit.w
			self.unit.F
			self.unit.a
		Output:
			Bool
		"""
		if self.unit.w / self.unit.F <= self.unit.a:
			return True
		else:
			return False

	def ekv_7_4(self):
		"""
		Variables used:
			self.unit.v
			self.unit.b
			self.unit.f_1
			self.unit.xi
		Output:
			Bool
		"""
		#TODO kontrollera ekvation
		if self.unit.v <= math.pow(self.unit.b, (self.unit.f_1 * math.pow(self.unit.xi, -1))):
			return True
		else:
			return False

	def ekv_7_5(self):
		"""
		Variables used:
			self.unit.l
			self.unit.E
			self.unit.I
			self.unit.m
		Output:
			self.unit.f_1
		"""
		#TODO (EI)nedsänskt till l (?)
		self.unit.f_1 = (math.pi / (2 * math.pow(self.unit.l, 2))) * math.sqrt(self.unit.E * self.unit.I / self.unit.m)

		return self.unit.f_1

	def ekv_7_6(self):
		"""
		Variables used:
			self.unit.n_40
			self.unit.m
			self.unit.b
			self.unit.l
		Output:
			self.unit.v
		"""
		self.unit.v = 4 * (0.4 + 0.6 * self.unit.n_40) / (self.unit.m * self.unit.b * self.unit.l + 200)

		return self.unit.v

	def ekv_7_7(self):
		"""
		Variables used:
			self.unit.f_1
			self.unit.b
			self.unit.l
			self.unit.E
			self.unit.I
		Output:
			self.unit.n_40
		"""
		#TODO kontrollera ekvation
		#TODO (EI)nedsänskt till l (?)
		#TODO (EI)nedsänskt till b (?)
		self.unit.n_40 = pow(((pow(40 / self.unit.f_1, 2) - 1) * pow((self.unit.b / self.unit.l), 4) * self.unit.E * self.unit.I / (self.unit.E * self.unit.I)), 0.25)

	def ekv_8_1(self):
		pass

	def ekv_8_2(self):
		pass

	def ekv_8_3(self):
		pass

	def ekv_8_4(self):
		pass

	def ekv_8_5(self):
		pass

	def ekv_8_6(self):
		pass

	def ekv_8_7(self):
		pass

	def ekv_8_8(self):
		pass

	def ekv_8_9(self):
		pass

	def ekv_8_10(self):
		pass

	def ekv_8_11(self):
		pass

	def ekv_8_12(self):
		pass

	def ekv_8_13(self):
		pass

	def ekv_8_14(self):
		pass

	def ekv_8_15(self):
		pass

	def ekv_8_16(self):
		pass

	def ekv_8_17(self):
		pass

	def ekv_8_18(self):
		pass

	def ekv_8_19(self):
		pass

	def ekv_8_20(self):
		pass

	def ekv_8_21(self):
		pass

	def ekv_8_22(self):
		
		pass

	def ekv_8_23(self):
		pass

	def ekv_8_24(self):
		pass

	def ekv_8_25(self):
		pass

	def ekv_8_26(self):
		pass

	def ekv_8_27(self):
		pass

	def ekv_8_28(self):
		pass

	def ekv_8_29(self):
		pass

	def ekv_8_30(self):
		pass

	def ekv_8_31(self):
		pass

	def ekv_8_32(self):
		pass

	def ekv_8_33(self):
		pass

	def ekv_8_34(self):
		pass

	def ekv_8_35(self):
		pass

	def ekv_8_36(self):
		pass

	def ekv_8_37(self):
		pass

	def ekv_8_38(self):
		pass

	def ekv_8_39(self):
		pass

	def ekv_8_40(self):
		pass

	def ekv_8_41(self):
		pass

	def ekv_8_42(self):
		pass

	def ekv_8_43(self):
		pass

	def ekv_8_44(self):
		pass

	def ekv_8_45(self):
		pass

	def ekv_8_46(self):
		pass

	def ekv_8_47(self):
		pass

	def ekv_8_48(self):
		pass

	def ekv_8_49(self):
		pass

	def ekv_8_50(self):
		pass

	def ekv_8_51(self):
		pass

	def ekv_8_52(self):
		pass

	def ekv_8_53(self):
		pass

	def ekv_8_54(self):
		pass

	def ekv_8_55(self):
		pass

	def ekv_8_56(self):
		pass

	def ekv_8_57(self):
		pass

	def ekv_8_58(self):
		pass

	def ekv_8_59(self):
		pass

	def ekv_8_60(self):
		pass

	def ekv_8_61(self):
		pass

	def ekv_8_62(self):
		pass

	def ekv_8_63(self):
		pass

	def ekv_8_64(self):
		pass

	def ekv_8_65(self):
		pass

	def ekv_8_66(self):
		pass

	def ekv_8_67(self):
		pass

	def ekv_8_68(self):
		pass

	def ekv_8_69(self):
		pass

	def ekv_8_70(self):
		pass

	def ekv_8_71(self):
		pass

	def ekv_8_72(self):
		pass

	def ekv_8_73(self):
		pass

	def ekv_8_74(self):
		pass

	def ekv_8_75(self):
		pass

	def ekv_8_76(self):
		pass

	def ekv_8_77(self):
		pass

	def ekv_8_78(self):
		pass

	def ekv_9_1(self):
		pass

	def ekv_9_2(self):
		pass

	def ekv_9_3(self):
		pass

	def ekv_9_4(self):
		pass

	def ekv_9_5(self):
		pass

	def ekv_9_6(self):
		pass

	def ekv_9_7(self):
		pass

	def ekv_9_8(self):
		pass

	def ekv_9_9(self):
		pass

	def ekv_9_10(self):
		pass

	def ekv_9_11(self):
		pass

	def ekv_9_12(self):
		pass

	def ekv_9_13(self):
		pass

	def ekv_9_14(self):
		pass

	def ekv_9_15(self):
		pass

	def ekv_9_16(self):
		pass

	def ekv_9_17(self):
		pass

	def ekv_9_18(self):
		pass

	def ekv_9_19(self):
		pass

	def ekv_9_20(self):
		pass

	def ekv_9_21(self):
		pass

	def ekv_9_22(self):
		pass

	def ekv_9_23(self):
		pass

	def ekv_9_24(self):
		pass

	def ekv_9_25(self):
		pass

	def ekv_9_26(self):
		pass

	def ekv_9_27(self):
		pass

	def ekv_9_28(self):
		pass

	def ekv_9_29(self):
		pass

	def ekv_9_30(self):
		pass

	def ekv_9_31(self):
		pass

	def ekv_9_32(self):
		pass

	def ekv_9_33(self):
		pass

	def ekv_9_34(self):
		pass

	def ekv_9_35(self):
		pass

	def ekv_9_36(self):
		pass

	def ekv_9_37(self):
		pass

	def ekv_9_38(self):
		pass

	def ekv_A_1(self):
		pass

	def ekv_A_2(self):
		pass

	def ekv_A_3(self):
		pass

	def ekv_A_4(self):
		pass

	def ekv_A_5(self):
		pass

	def ekv_A_6(self):
		pass

	def ekv_A_7(self):
		pass

	def ekv_B_1(self):
		pass

	def ekv_B_2(self):
		pass

	def ekv_B_3(self):
		pass

	def ekv_B_4(self):
		pass

	def ekv_B_5(self):
		pass

	def ekv_B_6(self):
		pass

	def ekv_B_7(self):
		pass

	def ekv_B_8(self):
		pass

	def ekv_B_9(self):
		pass

	def ekv_B_10(self):
		pass

	def ekv_C_1(self):
		pass

	def ekv_C_2(self):
		pass

	def ekv_C_3(self):
		pass

	def ekv_C_4(self):
		pass

	def ekv_C_5(self):
		pass

	def ekv_C_6(self):
		pass

	def ekv_C_7(self):
		pass

	def ekv_C_8(self):
		pass

	def ekv_C_9(self):
		pass

	def ekv_C_10(self):
		pass

	def ekv_C_11(self):
		pass

	def ekv_C_12(self):
		pass

	def ekv_C_13(self):
		pass

	def ekv_C_14(self):
		pass

	def ekv_C_15(self):
		pass

	def ekv_C_16(self):
		pass

	def ekv_C_17(self):
		pass

	def ekv_C_18(self):
		pass

	def ekv_C_19(self):
		pass


class UltimateLimitStateTimber(SS_EN_1995_1_1):

	#TODO maybe change this to call an @classmethod (easier for different codes)
	def __init__(self):
		super().__init__()

	def set_unit(self, unit):
		self.unit = unit

	def start_calculation(self):
		"""
		Calculates the relevant equations and returns a namedtuple
		"""
		#TODO tryck_90
		#TODO correct logic for which calculations to initialize e.g.  N==0 and M != 0
		if self.unit.N == 0:
			_B = self.böjning()
			_LTB = self.slankhet_balk_böj()
		elif self.unit.N > 0:
			_B  = self.böjning_och_drag()
		elif self.unit.N < 0:
			_B = self.böjning_och_tryck()
			_FB = self.slankhet_pelare_kompression()
			_LTB = self.slankhet_balk_böj()
			#TODO add new results to results when applicable
			print("LTB", _LTB)
			print("FB", _FB)

		if self.unit.V != 0:
			_V = self.tvärkraft()
		else:
			_V = 0

		if self.unit.T != 0:
			_T = self.vridning()
		else:
			_T = 0

		#TODO kompression i vinkel
		resultat_ntuple = namedtuple("result", "bending, shear, torsion")

		return resultat_ntuple(_B, _V, _T)

	# 1 Stress one direction ===============

	# 6.1.2
	def drag_0(self):
		return self.ekv_6_1()

	# 6.1.3
	def drag_90(self):
		pass

	# 6.1.4
	def tryck_0(self):
		return self.ekv_6_2()
		#TODO lägg in modul för stabilitet (6.3.2), om column

	# 6.1.5
	def tryck_90(self):
		return self.ekv_6_3()
		#TODO lägg in modul för stabilitet (6.3.2), om column

	# 6.1.6
	def böjning(self):
		return self.ekv_6_11(), self.ekv_6_12()
		#TODO lägg in modul för stabilitet (6.3.3), om beam

	# 6.1.7
	def tvärkraft(self):
		#TODO tvärkraft verkar vara fel
		return self.ekv_6_13()

	# 6.1.8
	def vridning(self):
		return self.ekv_6_14()

	# 2 Combined stresses ===================

	# 6.2.2
	def kompression_i_vinkel(self):
		#TODO lägg in modul för stabilitet (6.3.2), om column
		pass

	# 6.2.3
	def böjning_och_drag(self):
		#TODO lägg in modul för stabilitet (6.3.3), om beam
		return self.ekv_6_17(), self.ekv_6_18()

	# 6.2.4
	def böjning_och_tryck(self):
		#TODO lägg in modul för stabilitet (6.3.2), om column
		#TODO lägg in modul för stabilitet (6.3.3), om beam
		return self.ekv_6_19(), self.ekv_6_20()

	# 3 Stability of members ================

	# 6.3.2
	def slankhet_pelare_kompression(self):
		self.unit.lambda_rel_y, self.unit.lambda_rel_z = self.ekv_6_21(), self.ekv_6_22()

		#self.unit.lambda_rel_y, self.unit.lambda_rel_z = self.ekv_6_21(), self.ekv_6_22()

		if self.unit.lambda_rel_z <= 0.3 and self.unit.lambda_rel_y <= 0.3:
			#TODO this case shouldn't add a new result
			return self.ekv_6_19(), self.ekv_6_20()

		else:
			#TODO Append result to results
			return self.ekv_6_23(), self.ekv_6_24()

	# 6.3.3
	def slankhet_balk_böj(self):
		#Add case for not stabilized around the weak axis
		if self.unit.M_z > 0 and self.unit.N == 0:
			return self.ekv_6_33() #TODO värde return
		elif self.unit.M_z > 0 and self.unit.N < 0== 0:
			return self.ekv_6_35()

	# 4 Varying cross-section or curved shape

	# 5 Notched beams =======================

	# 6 System Strength =====================

	def placeholder(self):
		pass


class Load:

    def __init__(self):
        self.koordinater = []
        self.type = "square"
        self.id = 0


class plot:

    def __init__(self):

        fig = plt.figure()
        self.ax = fig.gca(projection='3d')
        self.id = 0
        self.objects = [] # [object.id, object]
        self.loads = []
        self.covers = []


    def add_object(self, vertex1, vertex2):
        object = StructuralUnit(000)
        object.id = self.id
        object.koordinater = np.array([vertex1,vertex2])

        #print(object.id, object.koordinater)
        self._plot_line(object.koordinater)

        #TODO vet inte om det kan vara >= 0
        if len(self.objects) > 0:
            #print("id:", self.id)
            for listed_object in self.objects:
                solved = False
                for i in range(0,3):
                    try:
                        #print("==")
                        if solved == False:
                            #print("försök", i)
                            solved = self._line_collision_detection(object, listed_object, i, i + 1, 1)
                        else:
                            break
                        #print("__")

                    except np.linalg.linalg.LinAlgError:
                        pass

                    if solved == False and i == 2:
                        self._check_duplicate(object)

        else:
            # Listan ska nog användas när allt ska renderas på en gång, t.ex. vid rutbyte
            self.objects.append([object.id, object])

        self.id += 1


    def _check_duplicate(self, object):
        """
        Checks if object exists in the object list.
        :param object: checked object
        :return:
        """
        q = 0
        duplicate = False
        for _ in self.objects:
            if self.objects[q][0] == object.id:
                duplicate = True
                break
            q += 1

        if duplicate == False:
            self.objects.append([object.id, object])
        else:
            pass


    def _line_collision_detection(self, new_object, object, i, j, k):
        P2 = new_object.koordinater[0]
        V2 = new_object.koordinater[1] - new_object.koordinater[0]
        #print("2", P2, V2, "({}, {})".format(new_object.koordinater[0], new_object.koordinater[1]))

        P1 = object[1].koordinater[0]
        V1 = object[1].koordinater[1] - object[1].koordinater[0]
        #print("1", P1, V1, "({}, {})".format(object[1].koordinater[0], object[1].koordinater[1]))

        if np.all(P1 == P2) and np.all(V1 == V2):
            return True

        X = np.array([V1, -V2])
        #print("X", X, sep="\n")

        Y = np.array([P2 - P1])
        #print("Y", Y, sep="\n")
        #print("=" * 20)

        X = np.delete(X, np.s_[i:j:k], 1)
        #print("X avskalad", X, sep="\n")

        Y = np.delete(Y, np.s_[i:j:k], 1)
        #print("Y", Y)
        #print("=" * 40)

        Y.resize((2,1))
        #print("Y avskalad", Y, sep="\n")

        ans = np.linalg.solve(X, Y)
        #print("ans", ans)

        #TODO tror inte detta är en bra lösning pga vinkeln
        CO1 = P1 + abs(ans[0]) * V1
        CO2 = P2 + abs(ans[1]) * V2
        #print("*********CO",  CO1, CO2, "************", sep="\n")

        #print("CO1: {} \n CO2: {}".format(CO1, CO2))

        if np.all(CO1 == CO2) and abs(ans[0]) <= 1 and abs(ans[1] <= 1):
            self._check_duplicate(new_object)
            i = 0
            for _ in self.objects:
                if self.objects[i][0] == new_object.id:
                    j = 0
                    for _ in self.objects:
                        if self.objects[j][0] == object[0]:
                            #print(self._set_relative_angle(V1, V2))
                            self.objects[i][1].contact_points.append([self.objects[j][1].id, CO2, self._set_relative_angle(V1, V2), self._set_absolute_angle(V1)])
                            self.objects[j][1].contact_points.append([self.objects[i][1].id, CO1, self._set_relative_angle(V1, V2), self._set_absolute_angle(V2)])

                            #print(self.objects[i][1].id, self.objects[i][1].contact_points)
                            #print(self.objects[j][1].id, self.objects[j][1].contact_points)

                            #for q in range(len(self.objects) + 1):
                                #print(self.objects[q][1].id)

                            #print("objekten:", self.objects)

                            return True
                        j += 1
                i += 1

        else:
            return False
            #self.objects.append([o_id, new_object])


    def _set_relative_angle(self, V1, V2):
        #print(V1)
        #print(V2)

        V1_V2_dot = np.dot(V1, V2)
        #print(V1_V2_dot)

        abs_V1 = np.linalg.norm(V1)
        abs_V2 = np.linalg.norm(V2)

        #print(abs_V1)
        #print(abs_V2)

        alpha = np.degrees(math.acos(V1_V2_dot / (abs_V1 * abs_V2)))
        #print("alpha", alpha)

        return alpha


    def _set_absolute_angle(self, V1):
        #print(V1)
        #print(V2)
        plane_normal = np.array([0,1,0])

        V1_OP_dot = np.dot(V1, plane_normal)
        #print(V1_V2_dot)

        abs_V1 = np.linalg.norm(V1)
        abs_V2 = np.linalg.norm(plane_normal)

        #print(abs_V1)
        #print(abs_V2)

        alpha = np.degrees(math.acos(V1_OP_dot / (abs_V1 * abs_V2)))
        #print("alpha", alpha)

        return alpha


    def add_load(self, load_type, p1, p2=None, p3=None, p4=None, **kwargs):
        """
        :param load_type: String, type of load
        :param p1: first vertex in 3D
        :param p2: (optional) second vertex in 3D
        :param p3: (optional) third vertex in 3D
        :param p4: (optional) forth vertex in 3D
        :param kwargs: further vertices in 3D
        :return: None
        """

        if load_type == "point":
            pass

        if load_type == "line":
            pass

        if load_type == "square":
            pass

        if load_type == "polygon":
            pass


    def add_square_face(self, p1, p2):
        """
        Prepares input for graphing in 3D and initializes collision detection with said face.

        :param p1: first point in rectangle.
        :param p2: Second point of rectangle, diagonally from p1.
        :return: -
        """
        v1 = p1
        v2 = [p1[0], (p2[1]+p1[1])/2, p2[2]]
        v3 = p2
        v4 = [p2[0], (p2[1]+p1[1])/2, p1[2]]
        face = np.array([v1, v2, v3, v4])
        #print(face)


        X = np.array(v1)
        Y = np.array(v2)
        X, Y = np.meshgrid(X, Y)
        Z = np.array([[p1[1]],[p1[1]],[p1[1]]])
        #print(X, Y, Z, sep="\n")

        surf = self.ax.plot_surface(X, Y, Z)

        self._face_collision_detection(face)


    def _face_collision_detection(self, surface):
        """

        :param surface: Surface defined by 4 points.
        :return:
        """
        # Creates cover object and appends to cover object list.
        cover = CoverUnit()
        cover.id = self.id
        self.covers.append([cover.id, cover])

        #TODO FUNKAR BARA OM DENNA GÖRS EFTER LINJERNA
        # Defining the planes equation in normal form.
        V1 = np.subtract(surface[1], surface[0])
        V2 = np.subtract(surface[3], surface[0])

        # N = D <=> ax + by + cz = D
        N = np.cross(V1, V2)
        D = np.multiply(N, surface[0])


        # Checks list of objects for collision coordinates.
        for obj in self.objects:
            p0 = obj[1].koordinater[0]
            p0p = obj[1].koordinater[1] - obj[1].koordinater[0]

            # Line segment is adjacent to plane. Check for boundaries.
            if np.sum(np.multiply(p0p, N)) == 0:
                print("gör koll för anliggande linje")
                #obj[1].cover_contact_points.append([cover.id, intersection])
                #cover.contact_points.append([obj[1].id, "beam", intersection])

            # Line segment intersects plane.
            else:
                t = (np.sum(D) - np.sum(np.multiply(p0, N))) / np.sum(np.multiply(p0p, N))
                if 0 <= t <= 1:
                    # Checks if line intersects plane segment
                    intersection = p0 + np.multiply(t, p0p)

                    if surface[0][0] <= intersection[0] <= surface[2][0] and surface[0][2] <= intersection[2] <= surface[2][2]:
                        # Stores intersecting point of line segment in lines object.
                        obj[1].cover_contact_points.append([cover.id, intersection])
                        cover.contact_points.append([obj[1].id, "column", intersection])




            #print(np.sum(np.multiply(p0, N)))
            #print(np.sum(np.multiply(p0p, N)))
            print("=" * 40)

        self.id += 1






    def _plot_line(self, koordinater):
        #TODO ändra flip; jag flippade Z och Y pga matplotlib
        X = np.array([[koordinater[0][0]], [koordinater[1][0]]])
        Y = np.array([[koordinater[0][2]], [koordinater[1][2]]])
        Z = np.array([[koordinater[0][1]], [koordinater[1][1]]])

        self.ax.plot_wireframe(X, Y, Z)


    def show(self):
        plt.show()


class Database:

	def __init__(self):
		self.members = {}
		self.ULS_timber = UltimateLimitStateTimber()

	def add_unit(self):
		"""Creates structuralUnit instance and assigns an unique id to it."""
		id = str(uuid4())
		self.id = id
		self.members[id] = {"object_instance": StructuralUnit(id), "result": None}

	def remove_all_units(self):
		"""Removes every unit listed."""
		self.members.clear()

	def save_result(self, id, result):
		"""Collects results of the calculated member and stores them in a dictionary.

		id: String; Objects UUID
		result: namedtuple; results of calculation
		"""
		self.members[id]["result"] = result
		self.members[id]["object_instance"].results = result


	def create_xml(self):
		"""Combines the .xml strings from each objects to an .xml file."""
		root = Element("database")
		tree = ElementTree(root)
		root.set("xmlns:xsd", "placeholder")
		root.set("xmlns:xsi", "placeholder")
		root.set("version", "version_placeholder")
		root.set("source_software", "placeholder")
		root.set("start_time", "time_placeholder")
		root.set("end_time", "time_placeholder")
		root.set("uuid", "uuid_placeholder")
		root.set("hash", "hash_placeholder")
		root.set("country", "SWE")
		root.set("xmlns", "urn:placeholder")

		entities = Element("entities")
		root.append(entities)

		with open("test.xml", "w") as f:
			for id in self.members:
				entities.append(self.members[id]["object_instance"]._prepare_for_xml())
				
			f.write(parseString(tostring(root)).toprettyxml())
