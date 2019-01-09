import math
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class TableValues:
	def __init__(self):
		pass

	def tabell_2_1(self, duration):
		tabell = {"permanent" : "more than 10 years",
					"long term" : "6 months - 10 years",
					"meadium term" : "1 week - 6 months",
					"instantaneous" : "0"}

	def tabell_2_3(self, type):
		#TODO lägg till så stora eller små bokstäver inte har betydelse
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
		#TODO gör klart listan + logik för "fler" än 3 serviceklasser

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
		#TODO gör klart tabell + logik, typ if type == True
		tabell = {"solid timber": {"S1": 0.6, "S2": 0.8, "S3": 2},
				  "glued laminated timber": {"S1": 0.6, "S2": 0.8, "S3": 2},
                  "LVL": {"S1": 0.6, "S2": 0.8, "S3": 2},  #ej klart nedåt
                  "plywood": {"S1": 6, "S2": 6, "S3": 6},
                  "OSB": {"S1": 6, "S2": 6, "S3": 6},
                  "particleboard": {"S1": 6, "S2": 6, "S3": 6},
                  "hard fibreboard": {"S1": 6, "S2": 6, "S3": 6},
                  "medium fibreboard": {"S1": 6, "S2": 6, "S3": 6},
                  "MDF fibreboard": {"S1": 6, "S2": 6, "S3": 6}}
		
		k_def = tabell.get(type).get(service_class)
		return k_def

	def tabell_6_1(self, l, stödtyp, lasttyp, torsionally_restrained, center, load_side, h):

		tabell = {"Simply supported": {"Constant moment": 1,
										"Uniformly distributed load": 0.9,
										"Concentrated force at the middle of the span": 0.8},
					"Cantilever": {"Uniformly distributed load": 0.5,
									"Concentrated force at the free end": 0.8}}

		if torsionally_restrained == True and center == True:
			l_ef = tabell.get(stödtyp).get(lasttyp) * l

			if load_side == "compression":
				l_ef = l_ef + 2 * h
			elif load_side == "tension":
				l_ef = l_ef - 0.5 * h

		else:
			l_ef = 1 * l


		return l_ef



	#TODO hitta rätt på denna info i EC, inte i femdesign
	# http://download.strusoft.com/FEM-Design/inst130x/theory.pdf
	# TODO gör detta för D-klasser och limträ
	def material_values_timber(self, material, konst):
		tabell = {#                N/mm2                                                                            kN/mm2                                                           kg/m3
			"C14": {"f_m_k": 14, "f_t_0_k": 8, "f_t_90_k": 0.4, "f_c_0_k": 16, "f_c_90_k": 2.0, "f_v_k": 1.7, "E_0_mean": 7, "E_0_05": 4.7, "E_90_mean": 0.23, "G_mean": 0.44, "rho_k": 290, "rho_mean": 350},
			"C16": {"f_m_k": 16, "f_t_0_k": 10, "f_t_90_k": 0.5, "f_c_0_k": 17, "f_c_90_k": 2.2, "f_v_k": 1.8, "E_0_mean": 8, "E_0_05": 5.4, "E_90_mean": 0.27, "G_mean": 0.5, "rho_k": 310, "rho_mean": 370},
			"C18": {"f_m_k": 18, "f_t_0_k": 11, "f_t_90_k": 0.5, "f_c_0_k": 18, "f_c_90_k": 2.2, "f_v_k": 2.0, "E_0_mean": 9, "E_0_05": 6.0, "E_90_mean": 0.30, "G_mean": 0.56, "rho_k": 320, "rho_mean": 380},
			"C20": {"f_m_k": 20, "f_t_0_k": 12, "f_t_90_k": 0.5, "f_c_0_k": 19, "f_c_90_k": 2.3, "f_v_k": 2.2, "E_0_mean": 9.5, "E_0_05": 6.4, "E_90_mean": 0.32, "G_mean": 0.59, "rho_k": 330, "rho_mean": 390},
			"C22": {"f_m_k": 22, "f_t_0_k": 13, "f_t_90_k": 0.5, "f_c_0_k": 20, "f_c_90_k": 2.4, "f_v_k": 2.4, "E_0_mean": 10, "E_0_05": 6.7, "E_90_mean": 0.33, "G_mean": 0.63, "rho_k": 340, "rho_mean": 410},
			"C24": {"f_m_k": 24, "f_t_0_k": 14, "f_t_90_k": 0.5, "f_c_0_k": 21, "f_c_90_k": 2.5, "f_v_k": 2.5, "E_0_mean": 11, "E_0_05": 7.4, "E_90_mean": 0.37, "G_mean": 0.69, "rho_k": 350, "rho_mean": 420},
			"C27": {"f_m_k": 27, "f_t_0_k": 16, "f_t_90_k": 0.6, "f_c_0_k": 22, "f_c_90_k": 2.6, "f_v_k": 2.8, "E_0_mean": 11.5, "E_0_05": 7.7, "E_90_mean": 0.38, "G_mean": 0.72, "rho_k": 370, "rho_mean": 450},
			"C30": {"f_m_k": 30, "f_t_0_k": 18, "f_t_90_k": 0.6, "f_c_0_k": 23, "f_c_90_k": 2.7, "f_v_k": 3.0, "E_0_mean": 12, "E_0_05": 8.0, "E_90_mean": 0.40, "G_mean": 0.75, "rho_k": 380, "rho_mean": 460},
			"C35": {"f_m_k": 35, "f_t_0_k": 21, "f_t_90_k": 0.6, "f_c_0_k": 25, "f_c_90_k": 2.8, "f_v_k": 3.4, "E_0_mean": 13, "E_0_05": 8.7, "E_90_mean": 0.43, "G_mean": 0.81, "rho_k": 400, "rho_mean": 480},
			"C40": {"f_m_k": 40, "f_t_0_k": 24, "f_t_90_k": 0.6, "f_c_0_k": 26, "f_c_90_k": 2.9, "f_v_k": 3.8, "E_0_mean": 14, "E_0_05": 9.4, "E_90_mean": 0.47, "G_mean": 0.88, "rho_k": 420, "rho_mean": 500},
			"C45": {"f_m_k": 45, "f_t_0_k": 27, "f_t_90_k": 0.6, "f_c_0_k": 27, "f_c_90_k": 3.1, "f_v_k": 3.8, "E_0_mean": 15, "E_0_05": 10, "E_90_mean": 0.50, "G_mean": 0.94, "rho_k": 440, "rho_mean": 520},
			"C50": {"f_m_k": 50, "f_t_0_k": 30, "f_t_90_k": 0.6, "f_c_0_k": 29, "f_c_90_k": 3.2, "f_v_k": 3.8, "E_0_mean": 16, "E_0_05": 10.7, "E_90_mean": 0.53, "G_mean": 1.0, "rho_k": 460, "rho_mean": 550}}

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
		# Todo det finns två värden på dessa, men vet inte varför
		tabell = {"ledadx2": 1,
					"ledadx1": 2,
					"fast+ledad": 0.7,
					"fastx2": 0.5}

		värde = tabell.get(typ) * längd

		return värde


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
        area = 0


        i = 0
        for _ in polygon:
            try:
                area += (polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1])
                i += 1
            except IndexError:
                area += (polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1])
                break

        area = abs(area) * 1/2

        return area


    def get_centroid(self, polygon):
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
        I_x = 0
        I_y = 0
        centroid = self.get_centroid(polygon)

        i = 0
        for _ in polygon:
            try:
                area = polygon[i][0] * polygon[i+1][1] - polygon[i+1][0] * polygon[i][1]

                x = pow((polygon[i][1] - centroid[1]), 2) + (polygon[i][1] - centroid[1]) * (polygon[i+1][1] - centroid[1]) + pow((polygon[i+1][1] - centroid[1]), 2)
                y = pow((polygon[i][0] - centroid[0]), 2) + (polygon[i][0] - centroid[0]) * (polygon[i+1][0] - centroid[0]) + pow((polygon[i+1][0] - centroid[0]), 2)

                I_x += x * area
                I_y += y * area

                i += 1

            except IndexError:
                area = polygon[i][0] * polygon[0][1] - polygon[0][0] * polygon[i][1]

                x = pow((polygon[i][1] - centroid[1]), 2) + (polygon[i][1] - centroid[1]) * (polygon[0][1] - centroid[1]) + pow((polygon[0][1] - centroid[1]), 2)
                y = pow((polygon[i][0] - centroid[0]), 2) + (polygon[i][0] - centroid[0]) * (polygon[0][0] - centroid[0]) + pow((polygon[0][0] - centroid[0]), 2)

                I_x += x * area
                I_y += y * area

                break

        I_x = abs(I_x) / 12
        I_y = abs(I_y) / 12

        #test_x = 2 * (100 * pow(10, 3) / 12) + 2 * 100 * 10 * pow(45, 2) + (20 * pow(80, 3) / 12)
        #test_y = 2 * (10 * pow(100, 3) / 12) + (80 * pow(20, 3) / 12)

        I = [I_x, I_y]

        return I


class CoverUnit:

    def __init__(self):
        self.id = int()
        self.contact_points = [] # [id, unit type (e.g. beam), coordinates]


class StructuralUnit(TableValues, Sections):

    def __init__(self):
        super().__init__()
        self.id = 0
        self.tvärsnitt = "rectangular"
        self.material = "C24"
        self.type = "solid timber"
        self.service_class = "S2"
        self.load_duration_class = "medium"
        self.enhetstyp = "beam"
        self.contact_points = [] # [id till angränsande, kontaktpunkt, vinkel till object, vinkel till världen]
        self.cover_contact_points = []

        self.section = self.set_section("Dressed Lumber", "95x220")
        self.dimensioner = self.get_dimensions(self.section[1])
        self.h = self.dimensioner[1]
        self.b = self.dimensioner[0]

        self.koordinater = np.array([[0,0,0], [0,5,0]])
        #TODO förmodligen kommer längden läsas fel iom att den inte uppdateras vid skapandet av objektet
        self.l = math.sqrt(pow(self.koordinater[1][0] - self.koordinater[0][0], 2) +
                           pow(self.koordinater[1][1] - self.koordinater[0][1], 2) +
                           pow(self.koordinater[1][2] - self.koordinater[0][2], 2))

        self.M_y = 0 #Nm
        self.M_z = 1.5*2000*pow(self.l,2)/8 #Nm
        #print("mz", self.M_z)
        #self.M_z = 0
        self.N = -0.000000001
        self.V = 1.5*2000/2

        self.T = 0
        #TODO, fixa en funktion till längsta ände
        self.r = math.sqrt(pow(self.h,2) + pow(self.b,2))

        self.A = self.dimensioner[0] * self.dimensioner[1]
        self.I_y = pow(self.dimensioner[0], 3) * self.dimensioner[1] / 12
        self.I_z = pow(self.dimensioner[1], 3) * self.dimensioner[0] / 12

        #TODO värden om typ, material osv måste matas in

    def variables(self):
        self.A = float()
        self.A_ef = float()
        self.A_f = float()
        self.A_net_v = float()
        self.C = float()
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
        self.V_u = float()
        self.V_I = float()
        self.W_y = float()
        self.X_d = float()
        self.X_k = float()
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
        self.b_i = float()
        self.b_net = float()
        self.b_w = float()
        self.d = float()
        self.d_I = float()
        self.d_c = float()
        self.d_ef = float()
        self.d_h = float()
        self.f_h_i_k = float()
        self.f_a_0_0 = float()
        self.f_a_90_90 = float()
        self.f_a_alpha_beta_k = float()
        self.f_ax_k = float()
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
        #self.h = float(), det var två som hette h (?)
        self.h_ef = float()
        self.h_f_c = float()
        self.h_f_t = float()
        self.h_rl = float()
        self.h_ru = float()
        self.h_w = float()
        self.i = float()
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
        self.k_mod = float()
        self.k_n = float()
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
        self.l_ef = float()
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
        self.beta = float()
        self.beta_c = float()
        self.gamma = float()
        self.gamma_M = float()
        self.lambda_y = float()
        self.lambda_z = float()
        self.lambda_rel_y = float()
        self.lambda_rel_z = float()
        self.rho_a = float()
        self.rho_k = float()
        self.rho_m = float()
        self.sigma_c_0_d = float()
        self.sigma_c_alpha_d = float()
        self.sigma_f_c_d = float()
        self.sigma_f_c_max_d = float()
        self.sigma_f_t_d = float()
        self.sigma_f_t_max_d = float()
        self.sigma_m_crit = float()
        self.sigma_m_y_d = float()
        self.sigma_m_z_d = float()
        self.sigma_m_alpha_d = float()
        self.sigma_N = float()
        self.sigma_t_0_d = float()
        self.sigma_t_90_d = float()
        self.sigma_w_c_d = float()
        self.sigma_w_t_d = float()
        self.tao_d = float()
        self.tao_F_d = float()
        self.tao_M_d = float()
        self.tao_tor_d = float()
        self.psi_0 = float()
        self.psi_2 = float()
        self.xi = float()


class SS_EN_1995_1_1(StructuralUnit):

    def __init__(self):
        super().__init__()

    def ekv_2_1(self):
        self.K_u = 2/3 * self.K_ser

        return self.K_u

    def ekv_2_2(self):
        #TODO lägg till summa av alla Q
        self.u_fin = self.u_fin_G + self.u_fin_Q1 + self.u_fin_Qi

        return self.u_fin

    def ekv_2_3(self):
        self.u_fin_G = self.u_inst_G * (1 + self.k_def)

        return self.u_fin_G

    def ekv_2_4(self):
        #TODO lägg till samtliga psivärden från eurocode 0, varje
        #TODO lastfall behöver ev. en egen class
        self.u_fin_Q1 = self.u_inst_Q1 * (1 + self.psi_2_1 * self.k_def)

        return self.u_fin_Q1

    def ekv_2_5(self):
        #TODO samma som ekv 2.4 och ekv 2.2
        self.u_fin_Qi = self.u_inst_Qi * (self.psi_2_i * self.k_def)

        return self.u_fin_Qi

    def ekv_2_6(self):
        #TODO gäller om members har olika k_mod, ta hänsyn till detta
        self.k_mod = math.sqrt(self.k_mod_1 * self.k_mod_2)

        return self.k_mod

    def ekv_2_7(self):
        self.E_mean_fin = self.E_mean / (1 + self.k_def)

        return self.E_mean_fin

    def ekv_2_8(self):
        self.G_mean_fin = self.G_mean / (1 + self.k_def)

        return self.G_mean_fin

    def ekv_2_9(self):
        self.K_ser_fin = self.K_ser / (1 + self.k_def)

        return self.K_ser_fin

    def ekv_2_10(self):
        self.E_mean_fin = self.E_mean / (1 + self.psi_2 * self.k_def)

        return self.E_mean_fin

    def ekv_2_11(self):
        self.G_mean_fin = self.G_mean / (1 + self.psi_2 * self.k_def)

        return self.G_mean_fin

    def ekv_2_12(self):
        self.K_ser_fin = self.K_ser / (1 + self.psi_2 * self.k_def)

        return self.K_ser_fin

    def ekv_2_13(self):
        #TODO gäller om members har olika k_mod, ta hänsyn till detta
        self.k_def = 2 * math.sqrt(self.k_def_1 * self.k_def_2)

        return self.k_def

    def ekv_2_14(self, k_mod, k_h, X_k, gamma_M):
        X_d = k_h * k_mod * X_k / gamma_M

        return X_d

    def ekv_2_15(self):
        self.E_d = self.E_mean / self.gamma_M

        return self.E_d

    def ekv_2_16(self):
        self.G_d = self.G_mean / self.gamma_M

        return self.G_d

    def ekv_2_17(self):
        self.R_d = self.k_mod * self.R_k / self.gamma_M

    # Gäller solitt trä (f_m_k + f_t_0_k)
    def ekv_3_1(self):
        self.rho_k = self.material_values_timber(self.material, "rho_k")
        self.h = self.dimensioner[1]

        if self.rho_k <= 700 and self.h < 150:
            self.k_h = min(math.pow(150 / self.h, 0.2), 1.3)
        else:
            self.k_h = 1

        return self.k_h

    # Limträ (f_m_k + f_t_0_k)
    def ekv_3_2(self):
        self.h = self.dimensioner[1]

        if self.h < 600:
            self.k_h = min(math.pow(600 / self.h, 0.1), 1.1)
        else:
            self.k_h = 1

        return self.k_h

    # LVL (f_m_k + f_t_0_k)
    def ekv_3_3(self):
        self.h = self.dimensioner[1]

        self.s = "placeholder" #TODO fixa exponeneten

        if self.h < 300:
            self.k_h = min(math.pow(300 / self.h, self.s), 1.2)
        else:
            self.k_h = 1

        return self.k_h

    # LVL, längd (f_m_k + f_t_0_k)
    def ekv_3_4(self):

        if self.l < 3000:
            self.k_l = min(math.pow(3000 / self.l, (self.s / 2)), 1.1)
        else:
            self.k_l = 1

        return self.k_l

    def ekv_5_1(self):
        #TODO spåra upp var theta går in (finns inte i variabellistan)
        if self.h <= 5:
            self.theta = 0.0005
        elif self.h > 5:
            self.theta = 0.0005 * math.sqrt(5 / self.h)

        return self.theta

    def ekv_5_2(self):
        #TODO self.e finns inte i variabellistan
        self.e = 0.0025 * self.l

        return self.e

    def ekv_6_1(self):
        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()

        self.gamma_M = self.tabell_2_3(self.type)

        self.f_t_0_k = self.material_values_timber(self.material, "f_t_0_k")


        self.sigma_t_0_d = self.ekv_6_36()


        self.f_t_0_d = self.k_mod * self.k_h * self.f_t_0_k / self.gamma_M

        kontroll = self.sigma_t_0_d / self.f_t_0_d

        return kontroll

    def ekv_6_2(self):
        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.gamma_M = self.tabell_2_3(self.type)

        self.f_c_0_k = self.material_values_timber(self.material, "f_c_0_k")


        self.f_c_0_d = self.k_mod * self.f_c_0_k / self.gamma_M


        self.sigma_c_0_d = self.ekv_6_36()

        #print(self.sigma_c_0_d)
        #print(self.f_c_0_d)

        kontroll = -self.sigma_c_0_d / self.f_c_0_d

        return kontroll

    def ekv_6_3(self):
        #TODO self.f_c_90_k finns, men inte d
        #TODO sigma_c_90_d finns inte i varibaellistan, men i ekv 6.4
        #TODO self.k_c_90 finns inte
        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.gamma_M = self.tabell_2_3(self.type)

        self.f_c_90_k = self.material_values_timber(self.material, "f_c_90_k")

        self.f_c_90_d = self.k_mod * self.f_c_90_k / self.gamma_M


        self.sigma_c_90_d = self.ekv_6_4()

        #TODO skapa logik till detta val
        self.k_c_90_d = self.avsnitt_6_1_5("continuous support", "Solid softwood")


        kontroll = self.sigma_c_90_d / (self.k_c_90_d * self.f_c_90_d)

        return kontroll

    def ekv_6_4(self):
        #TODO self.F_c_90_d finns inte i variabellistan

        self.A_ef = 100 * 100 # TODO placeholder. Lägg in geometri från anliggande element + logik

        self.F_c_90_d = 19000 # TODO placeholder. Lägg in krafer från andra element + logik

        self.sigma_c_90_d = self.F_c_90_d / self.A_ef

        return self.sigma_c_90_d


    def ekv_6_5(self):
        pass

    def ekv_6_6(self):
        pass

    def ekv_6_7(self):
        pass

    def ekv_6_8(self):
        pass

    def ekv_6_9(self):
        pass

    def ekv_6_10(self):
        pass

    def ekv_6_11(self):
        #TODO slutkontroll
        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()

        #TODO lägga in k_sys (Jag försåtr inte riktigt)

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.gamma_M = self.tabell_2_3(self.type)

        self.f_m_y_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M
        #print("fmyd", self.f_m_y_d)

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M
        #print("fmzd", self.f_m_z_d)

        #print("Iz", self.I_z)
        #print("mz", self.M_z)
        #print("höjd", self.h / 2)

        self.sigma_m_y_d = max(self.M_y * self.dimensioner[0]/2 * 10e2 / self.I_y, self.M_y * (self.dimensioner[1]/-2) * 10e2 / self.I_y)
        #print("sigmamyd", self.sigma_m_y_d)

        self.sigma_m_z_d = self.M_z * 10e2 * self.h/2 / self.I_z
        #print("sigmamzd", self.sigma_m_z_d)

        self.k_m = self.avsnitt_6_1_6_2(self.tvärsnitt, self.type)

        kontroll = self.sigma_m_y_d / self.f_m_y_d + self.k_m * self.sigma_m_z_d / self.f_m_z_d

        return kontroll

    def ekv_6_12(self):
        #TODO slutkontroll
        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()

        #TODO lägga in k_sys (Jag försåtr inte riktigt)

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.gamma_M = self.tabell_2_3(self.type)

        self.f_m_y_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        #TODO fattar inte varför 10e2 och inte 10e3
        self.sigma_m_y_d = max(self.M_y * self.dimensioner[0]/2 * 10e2 / self.I_y, self.M_y * (self.dimensioner[1]/-2) * 10e2 / self.I_y)

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)

        self.k_m = self.avsnitt_6_1_6_2(self.tvärsnitt, self.type)

        kontroll = self.k_m * self.sigma_m_y_d / self.f_m_y_d + self.sigma_m_z_d / self.f_m_z_d

        return kontroll

    def ekv_6_13(self):
        #TODO det verkar vara andra värden för fvk i femdesign
        self.f_v_k = self.material_values_timber(self.material, "f_v_k")
        #print("fvk", self.f_v_k)

        self.gamma_M = self.tabell_2_3(self.type)
        #print("gammam", self.gamma_M)

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.f_v_d = self.k_mod * self.f_v_k / self.gamma_M
        #print("fvd", self.f_v_d)

        #############################
        self.b_ef = self.ekv_6_13_a()

        A_ef = self.b_ef * self.dimensioner[1]

        self.tao_d = self.V / A_ef
        #print("taod", self.tao_d)

        ##############################
        kontroll = self.tao_d / self.f_v_d

        #TODO det finns en klausul (3) om supports som inte är i koden

        return kontroll

    def ekv_6_13_a(self):
        #TODO self.b_ef finns inte i variabellistan

        # k_cr kan ha nationellt annex
        if self.type == "solid timber" or self.type == "glued laminated timber":
            self.k_cr = 0.67
        else:
            self.k_cr = 1

        self.b = self.dimensioner[0]

        self.b_ef = self.k_cr * self.b

        return self.b_ef

    def ekv_6_14(self):
        self.f_v_k = self.material_values_timber(self.material, "f_v_k")

        self.gamma_M = self.tabell_2_3(self.type)

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.f_v_d = self.k_mod * self.f_v_k / self.gamma_M

        ###################################

        self.k_shape = self.ekv_6_15()

        ####################

        self.I_tor = self.I_y + self.I_z

        #print("r", self.r)

        self.tao_tor_d = self.T * self.r / self.I_tor

        ####################
        kontroll = self.tao_tor_d / (self.k_shape * self.f_v_d)

        return kontroll

    def ekv_6_15(self):
        #TODO gör en allmän formel för alla geometrier

        #TODO lägg till self.crossection + funktion som kontrollerar detta
        if self.tvärsnitt == "rectangular":
            self.k_shape = min(1 + 0.15 * self.h / self.b, 2)
        elif self.tvärsnitt == "circular":
            self.k_shape = 1.2

        return self.k_shape

    def ekv_6_16(self):
        #TODO self.k_c_90 finns inte i variabellistan
        #TODO self.f_c_90_d finns inte i variabellistan, men i en annan funktion tror jag
        #TODO kontrollera ekvationen
        if self.sigma_c_alpha_d <= self.f_c_0_d / ((self.f_c_0_d / (self.k_c_90 * self.f_c_90_d)) * (math.pow(math.sin(self.alpha), 2) + math.pow(math.cos(self.alpha), 2))):
            return True
        else:
            return False

    def ekv_6_17(self):
        #TODO kontrollera ekvation

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()

        self.gamma_M = self.tabell_2_3(self.type)


        #TODO lägga in k_sys (Jag försåtr inte riktigt)

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.f_t_0_k = self.material_values_timber(self.material, "f_t_0_k")



        self.f_m_y_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_t_0_d = self.k_mod * self.k_h * self.f_t_0_k / self.gamma_M


        #TODO fattar inte varför 10e2 och inte 10e3
        self.sigma_t_0_d = self.ekv_6_36()

        self.sigma_m_y_d = max(self.M_y * self.dimensioner[0]/2 * 10e2 / self.I_y, self.M_y * (self.dimensioner[1]/-2) * 10e2 / self.I_y)

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)


        self.k_m = self.avsnitt_6_1_6_2(self.tvärsnitt, self.type)

        kontroll = self.sigma_t_0_d / self.f_t_0_d + self.sigma_m_y_d / self.f_m_y_d + self.k_m * self.sigma_m_z_d / self.f_m_z_d

        return kontroll

    def ekv_6_18(self):
        #TODO kontrollera ekvation

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()


        #TODO lägga in k_sys (Jag försåtr inte riktigt)

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.f_t_0_k = self.material_values_timber(self.material, "f_t_0_k")

        self.gamma_M = self.tabell_2_3(self.type)


        self.f_m_y_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_t_0_d = self.k_mod * self.k_h * self.f_t_0_k / self.gamma_M


        #TODO fattar inte varför 10e2 och inte 10e3
        self.sigma_m_y_d = max(self.M_y * self.dimensioner[0]/2 * 10e2 / self.I_y, self.M_y * (self.dimensioner[1]/-2) * 10e2 / self.I_y)

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)

        self.sigma_t_0_d = self.ekv_6_36()


        self.k_m = self.avsnitt_6_1_6_2(self.tvärsnitt, self.type)

        kontroll = self.sigma_t_0_d / self.f_t_0_d + self.k_m * self.sigma_m_y_d / self.f_m_y_d + self.sigma_m_z_d / self.f_m_z_d

        return kontroll


    def ekv_6_19(self):
        #TODO kontrollera ekvation
        #TODO Slutkontroll

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()


        #TODO lägga in k_sys (Jag försåtr inte riktigt)

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.f_c_0_k = self.material_values_timber(self.material, "f_c_0_k")

        self.gamma_M = self.tabell_2_3(self.type)


        self.f_m_y_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M
        #print("fmyd", self.f_m_y_d)

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M
        #print("fmzd", self.f_m_z_d)

        self.f_c_0_d = self.k_mod * self.k_h * self.f_c_0_k / self.gamma_M
        #print("fcod", self.f_c_0_d)

        #TODO fattar inte varför 10e2 och inte 10e3
        self.sigma_m_y_d = max(self.M_y * self.dimensioner[0]/2 * 10e2 / self.I_y, self.M_y * (self.dimensioner[1]/-2) * 10e2 / self.I_y)

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)

        self.sigma_c_0_d = self.ekv_6_36()


        self.k_m = self.avsnitt_6_1_6_2(self.tvärsnitt, self.type)

        kontroll = math.pow((self.sigma_c_0_d / self.f_c_0_d), 2) + \
                   self.sigma_m_y_d / self.f_m_y_d + self.k_m * self.sigma_m_z_d / self.f_m_z_d

        return kontroll

    def ekv_6_20(self):
        #TODO kontrollera ekvation
        #TODO Slutkontroll

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()


        #TODO lägga in k_sys (Jag försåtr inte riktigt)

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.f_c_0_k = self.material_values_timber(self.material, "f_c_0_k")

        self.gamma_M = self.tabell_2_3(self.type)


        self.f_m_y_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_c_0_d = self.k_mod * self.k_h * self.f_c_0_k / self.gamma_M


        #TODO fattar inte varför 10e2 och inte 10e3
        self.sigma_m_y_d = max(self.M_y * self.dimensioner[0]/2 * 10e2 / self.I_y, self.M_y * (self.dimensioner[1]/-2) * 10e2 / self.I_y)

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)

        self.sigma_c_0_d = self.ekv_6_36()


        self.k_m = self.avsnitt_6_1_6_2(self.tvärsnitt, self.type)


        kontroll = math.pow((self.sigma_c_0_d / self.f_c_0_d), 2) + self.k_m * self.sigma_m_y_d / self.f_m_y_d + \
                   self.sigma_m_z_d / self.f_m_z_d

        return kontroll

    def ekv_6_21(self):
        #TODO self.f_c_0_k finns inte i varibellistan
        self.f_c_0_k = self.material_values_timber(self.material, "f_c_0_k")

        self.E_0_05 = self.material_values_timber(self.material, "E_0_05")

        #####################################
        i_y = math.sqrt(self.A / self.I_y)

        self.l_c = self.effektiv_längd_placeholder("ledadx2", self.l) #TODO implementera funktion när den skapas

        self.lambda_y = self.l_c / i_y

        ######################################
        self.lambda_rel_y = self.lambda_y / math.pi * math.sqrt(self.f_c_0_k / (self.E_0_05*10e3))

        #print(self.lambda_rel_y)
        return self.lambda_rel_y

    def ekv_6_22(self):
        #TODO self.f_c_0_k finns inte i varibellistan
        self.f_c_0_k = self.material_values_timber(self.material, "f_c_0_k")

        self.E_0_05 = self.material_values_timber(self.material, "E_0_05")

        #####################################
        i_z = math.sqrt(self.A / self.I_z)

        self.l_c = self.effektiv_längd_placeholder("ledadx2", self.l) #TODO implementera funktion när den skapas

        self.lambda_z = self.l_c / i_z

        ######################################
        self.lambda_rel_z = self.lambda_z / math.pi * math.sqrt(self.f_c_0_k / (self.E_0_05*10e3))

        #print(self.lambda_rel_z)
        return self.lambda_rel_z

    def ekv_6_23(self):
        #TODO kontrollera ekvation
        #print("ekv623")

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()

        self.k_c_y = self.ekv_6_25()


        #TODO lägga in k_sys (Jag försåtr inte riktigt)

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.f_c_0_k = self.material_values_timber(self.material, "f_c_0_k")

        self.gamma_M = self.tabell_2_3(self.type)


        self.f_m_y_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_c_0_d = self.k_mod * self.k_h * self.f_c_0_k / self.gamma_M


        #TODO fattar inte varför 10e2 och inte 10e3
        self.sigma_m_y_d = max(self.M_y * self.dimensioner[0]/2 * 10e2 / self.I_y, self.M_y * (self.dimensioner[1]/-2) * 10e2 / self.I_y)

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)

        self.sigma_c_0_d = self.ekv_6_36()


        self.k_m = self.avsnitt_6_1_6_2(self.tvärsnitt, self.type)

        kontroll = math.pow((self.sigma_c_0_d / self.f_c_0_d), 2) + \
                   self.sigma_m_y_d / self.f_m_y_d + self.k_m * self.sigma_m_z_d / self.f_m_z_d

        return kontroll

    def ekv_6_24(self):
        #TODO kontrollera ekvation

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()


        #TODO lägga in k_sys (Jag försåtr inte riktigt)

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.f_c_0_k = self.material_values_timber(self.material, "f_c_0_k")

        self.gamma_M = self.tabell_2_3(self.type)

        self.k_c_z = self.ekv_6_26()


        self.f_m_y_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M

        self.f_c_0_d = self.k_mod * self.k_h * self.f_c_0_k / self.gamma_M


        #TODO fattar inte varför 10e2 och inte 10e3
        self.sigma_m_y_d = max(self.M_y * self.dimensioner[0]/2 * 10e2 / self.I_y, self.M_y * (self.dimensioner[1]/-2) * 10e2 / self.I_y)

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)

        self.sigma_c_0_d = self.ekv_6_36()


        self.k_m = self.avsnitt_6_1_6_2(self.tvärsnitt, self.type)


        kontroll = math.pow((self.sigma_c_0_d / self.f_c_0_d), 2) + self.k_m * self.sigma_m_y_d / self.f_m_y_d + \
                   self.sigma_m_z_d / self.f_m_z_d

        return kontroll

    def ekv_6_25(self):
        #TODO kontrollera ekvation
        self.k_y = self.ekv_6_27()

        self.k_c_y = 1 / (self.k_y + math.sqrt(math.pow(self.k_y, 2) - math.pow(self.lambda_rel_y, 2)))

        return self.k_c_y

    def ekv_6_26(self):
        #TODO kontrollera ekvation
        self.k_z = self.ekv_6_28()

        self.k_c_z = 1 / (self.k_z + math.sqrt(math.pow(self.k_z, 2) - math.pow(self.lambda_rel_z, 2)))

        return self.k_c_z

    def ekv_6_27(self):
        #TODO kontrollera ekvation
        self.beta_c = self.ekv_6_29()

        self.k_y = 0.5 * (1 + self.beta_c * (self.lambda_rel_y - 0.3) + math.pow(self.lambda_rel_y, 2))

        return self.k_y

    def ekv_6_28(self):
        #TODO kontrollera ekvation
        self.beta_c = self.ekv_6_29()

        self.lambda_rel_z = self.ekv_6_22()

        self.k_z = 0.5 * (1 + self.beta_c * (self.lambda_rel_z - 0.3) + math.pow(self.lambda_rel_z, 2))

        return self.k_z

    def ekv_6_29(self):
        if self.type == "solid timber":
            self.beta_c = 0.2
        elif self.type == "glued laminated timber" or "LVL":
            self.beta_c = 0.1

        return self.beta_c

    def ekv_6_30(self):
        #TODO self.lambda_rel_m finns inte i varibaellistan
        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.sigma_m_crit = self.ekv_6_31()


        self.lambda_rel_m = math.sqrt(self.f_m_k / self.sigma_m_crit)
        #print("lambdarelm", self.lambda_rel_m)

        return self.lambda_rel_m

    def ekv_6_31(self):
        #TODO self.M_y_crit finns inte i varibalellistan
        self.E_0_05 = self.material_values_timber(self.material, "E_0_05")

        #TODO ändra till G,005 ist för gmean
        self.G_0_05 = self.material_values_timber(self.material, "G_mean")

        self.I_tor = self.I_z + self.I_y

        self.l_ef = self.tabell_6_1(self.l, "Simply supported", "Uniformly distributed load", True, True, "compression", self.h)

        ################################

        #TODO kontrollera ekvation
        self.M_z_crit = math.pi * math.sqrt(self.E_0_05 * self.I_y * self.G_0_05 * 10e3 * self.I_tor) / self.l_ef
        #print(self.M_z_crit)


        self.W_z = self.I_z / self.h
        #print(self.W_z)

        self.sigma_m_crit = self.M_z_crit / self.W_z
        #print(self.sigma_m_crit)

        return self.sigma_m_crit

    def ekv_6_32(self):
        #TODO kontrollera ekvation
        self.sigma_m_crit = 0.78 * math.pow(self.b, 2) / (self.h * self.l_ef) * self.E_0_05

        return self.sigma_m_crit

    def ekv_6_33(self):
        #TODO self.sigma_m_d finns inte i variabellistan

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.gamma_M = self.tabell_2_3(self.type)

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M
        #print("fmzd", self.f_m_z_d)
        #############################

        self.k_crit = self.ekv_6_34()
        #print("kcrit", self.k_crit)

        #############################

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)
        #print("sigmamzd", self.sigma_m_z_d)

        #############################
        kontroll = self.sigma_m_z_d / (self.k_crit * self.f_m_z_d)
        #print("kontroll", kontroll)

        return kontroll


    def ekv_6_34(self):
        stadgad = False #TODO, skapa funktion

        if stadgad == False:
            self.lambda_rel_m = self.ekv_6_30()

            if self.lambda_rel_m <= 0.75:
                self.k_crit = 1
            #TODO kontrollera denna syntax
            elif 0.75 < self.lambda_rel_m <= 1.4:
                self.k_crit = 1.56 - 0.75 * self.lambda_rel_m
            elif 1.4 < self.lambda_rel_m:
                self.k_crit = 1 / math.pow(self.lambda_rel_m, 2)
        else:
            self.k_crit = 1

        return self.k_crit

    def ekv_6_35(self):
        #TODO self.sigma_m_d finns inte i varibellistan
        #TODO self.f_m_d finns inte i varibaellistan
        #TODO kontrollera ekvation

        #TODO self.sigma_m_d finns inte i variabellistan

        self.k_mod = self.tabell_3_1(self.type, self.service_class, self.load_duration_class)

        self.k_h = self.ekv_3_1()

        self.f_m_k = self.material_values_timber(self.material, "f_m_k")

        self.gamma_M = self.tabell_2_3(self.type)

        self.f_m_z_d = self.k_mod * self.k_h * self.f_m_k / self.gamma_M
        #print("fmzd", self.f_m_z_d)
        #############################

        self.k_crit = self.ekv_6_34()
        #print("kcrit", self.k_crit)

        #############################

        self.sigma_m_z_d = max(self.M_z * self.dimensioner[1]/2 * 10e2 / self.I_z, self.M_z * self.dimensioner[1]/-2 * 10e2 / self.I_z)
        #print("sigmamzd", self.sigma_m_z_d)

        self.sigma_c_0_d = self.ekv_6_36()

        #############################

        self.k_c_z = self.ekv_6_26()

        self.f_c_0_d = self.k_mod * self.k_h * self.f_c_0_k / self.gamma_M

        #############################

        kontroll = math.pow((self.sigma_m_z_d / (self.k_crit * self.f_m_z_d)), 2) + self.sigma_c_0_d / (self.k_c_z * self.f_c_0_d)

        return kontroll

    def ekv_6_36(self):
        self.sigma_N = self.N / self.A

        return self.sigma_N

    def ekv_6_37(self):
        #TODO self.sigma_m_0_d finns inte i varibellistan
        self.sigma_m_alpha_d = self.sigma_m_0_d = 6 * self.M_d / (self.b * pow(self.h, 2))

        #TODO vilken ska returneras? logik
        return self.sigma_m_alpha_d
        #return self.sigma_m_0_d

    def ekv_6_38(self):
        #TODO self.k_m_alpha finns inte i variabellistan, men i ekv 6.39 eller 6.40
        #TODO self.f_m_d finns inte i variabellistan
        if self.sigma_m_alpha_d <= self.k_m_alpha * self.f_m_d:
            return True
        else:
            return False

    def ekv_6_39(self):
        #TODO self.f_m_d finns inte i varibellistan
        #TODO kontrollera ekvation
        self.k_m_alpha = 1 / math.sqrt(1 + math.pow(( self.f_m_d / (0.75 * self.f_v_d) * math.tan(self.alpha)), 2) +
                                       math.pow(self.f_m_d / self.f_t_90_d * pow(math.tan(self.alpha), 2), 2))

        return self.k_m_alpha

    def ekv_6_40(self):
        #TODO self.f_m_d finns inte i varibellistan
        #TODO kontrollera ekvation
        self.k_m_alpha = 1 / math.sqrt(1 + math.pow(( self.f_m_d / (1.5 * self.f_v_d) * math.tan(self.alpha)), 2) +
                                       math.pow(self.f_m_d / self.f_t_90_d * pow(math.tan(self.alpha), 2), 2))

        return self.k_m_alpha

    def ekv_6_41(self):
        #TODO self.sigma_m_d finns inte i varibellistan, men i ekv 6.42
        #TODO self.f_m_d finns inte i varibellistan
        if self.sigma_m_d <= self.k_r * self.f_m_d:
            return True
        else:
            return False

    def ekv_6_42(self):
        #TODO kontrollera ekvation
        self.sigma_m_d = self.k_l * 6 * self.M_ap_d / (self.b * math.pow(self.h_ap, 2))

        return self.sigma_m_d

    def ekv_6_43(self):
        #TODO self.sigma_k_1 - 4 finns inte i varibellistan, men i ekv nedan
        self.k_l = self.k_1 + self.k_2 * (self.h_ap / self.r) + self.k_3 * math.pow((self.h_ap / self.r), 2) + self.k_4 * math.pow((self.h_ap / self.r), 3)

        return self.k_l

    def ekv_6_44(self):
        #TODO self.alpha_ap finns inte i variabellistan
        #TODO kontrollera ekvation
        self.k_1 = 1 + 1.4 * math.tan(self.alpha_ap) + 5.4 * math.pow(math.tan(self.alpha_ap), 2)

        return self.k_1

    def ekv_6_45(self):
        #TODO self.alpha_ap finns inte i variabellistan
        self.k_2 = 0.35 - 8 * math.tan(self.alpha_ap)

        return self.k_2

    def ekv_6_46(self):
        #TODO self.alpha_ap finns inte i variabellistan
        #TODO kontrollera ekvation
        self.k_3 = 0.6 + 8.3 * math.tan(self.alpha_ap) - 7.8 * math.pow(math.tan(self.alpha_ap), 2)

        return self.k_3

    def ekv_6_47(self):
        #TODO self.alpha_ap finns inte i variabellistan
        self.k_4 = 6 * math.pow(math.tan(self.alpha_ap), 2)

        return self.k_4

    def ekv_6_48(self):
        self.r = self.r_in + 0.5 * self.h_ap

        return self.r

    def ekv_6_49(self):
        if self.r_in / self.t < 240:
            self.k_r = 0.76 + 0.001 * self.r_in / self.t
        elif self.r_in / self.t >= 240:
            self.k_r = 1

        return self.k_r

    def ekv_6_50(self):
        if self.sigma_t <= self.k_dis * self.k_vol * self.f_t_90_d:
            return True
        else:
            return False

    def ekv_6_51(self):
        #TODO fixa wood_type()
        #TODO self.V_0 finns inte i varibaellistan
        if self.wood_type() == "solid timber":
            self.k_vol = 1
        elif self.wood_type() == "glued laminated timber" or "LVL":
            self.k_vol = math.pow((self.V_0 / self.V), 0.2)

        return self.k_vol

    def roof_beam_type(self):
        return "placeholder"

    def ekv_6_52(self):
        #TODO fixa en funktion som avgör takstolens typ
        if self.roof_beam_type() == "double tapered" or "curved":
            self.k_dis = 1.4
        elif self.roof_beam_type() == "pitched cambered":
            self.k_dis = 1.7

        return self.k_dis

    def ekv_6_53(self):
        if self.tao_d / self.f_v_d + self.sigma_t_90_d / (self.k_dis * self.k_vol * self.f_t_90_d) <= 1:
            return True
        else:
            return False

    def ekv_6_54(self):
        #TODO kontrollera ekvation
        #TODO self.k_p finns inte i variabellistan, men i ekv 6.56
        self.sigma_t_90_d = self.k_p * 6 * self.M_ap_d / (self.b * math.pow(self.h_ap, 2))

        return self.sigma_t_90_d

    def ekv_6_55(self):
        #TODO kontrollera ekvation
        #TODO self.k_p finns inte i variabellistan, men i ekv 6.56
        self.sigma_t_90_d = self.k_p * 6 * self.M_ap_d / (self.b * math.pow(self.h_ap, 2)) - 0.6 * self.p_d / self.b

        return self.sigma_t_90_d

    def ekv_6_56(self):
        #TODO kotnrollera ekvation
        #TODO self.K_5 - 7 finns i ekv nedan
        self.k_p = self.k_5 + self.k_6 * (self.h_ap / self.r) + self.k_7 * (math.pow((self.h_ap / self.r), 2))

        return self.k_p

    def ekv_6_57(self):
        #TODO self.alpha_ap finns inte i variabellistan
        self.k_5 = 0.2 * math.tan(self.alpha_ap)

        return self.k_5

    def ekv_6_58(self):
        #TODO self.alpha_ap finns inte i variabellistan
        #TODO kontrollera ekvation
        self.k_6 = 0.25 - 1.5 * math.tan(self.alpha_ap) + 2.6 * math.pow(math.tan(self.alpha_ap), 2)

        return self.k_6

    def ekv_6_59(self):
        #TODO self.alpha_ap finns inte i variabellistan
        #TODO kontrollera ekvation
        self.k_7 = 2.1 * math.tan(self.alpha_ap) - 4 * math.pow(math.tan(self.alpha_ap), 2)

        return self.k_7

    def ekv_6_60(self):
        self.tao_d = 1.5 * self.V / (self.b * self.h_ef)

        if self.tao_d <= self.k_v * self.f_v_d:
            return True
        else:
            return False

    def beam_notch_side(self):
        return "placeholder"

    def ekv_6_61(self):
        #TODO self.k_n finns inte i varibaellistan
        #TODO kontrollera ekvationer
        #TODO self.x finns inte i variabellistan
        if self.beam_notch_side() == "opposite":
            self.k_v = 1

        return self.k_v

    def ekv_6_62(self):
        #TODO self.k_n finns inte i varibaellistan
        #TODO kontrollera ekvationer
        #TODO self.x finns inte i variabellistan
        if self.beam_notch_side() == "same":
            self.k_v = min((self.k_n * (1 + 1.1 * math.pow(self.i, 1.5) / math.sqrt(self.h)) /
                            (math.sqrt(self.h) * (math.sqrt(self.alpha * (1 - self.alpha)) + 0.8 * (self.x / self.h) * math.sqrt(1 / self.alpha - pow(self.alpha, 2))))),
                           1)

        return self.k_v

    def ekv_6_63(self):
        #TODO self.k_n finns inte i variabellistan
        if self.wood_type() == "LVL":
            self.k_n = 4.5
        elif self.wood_type() == "solid timber":
            self.k_n = 5
        elif self.wood_type() == "glued laminated timber":
            self.k_n = 6.5

        return self.k_n

    def ekv_7_1(self):
        #TODO räknar ihop olika members, rho_1 - 2 finns inte i variabellistan
        self.rho_m = math.sqrt(self.rho_m_1 * self.rho_m_2)

        return self.rho_m

    def ekv_7_2(self):
        #TODO finns inte creep i trä?
        #self.w_net_fin = self.w_inst + self.w_creep - self.w_c = self.w_inst - self.w_c

        self.w_net_fin = self.w_inst - self.w_c

        return self.w_net_fin

    def ekv_7_3(self):
        #TODO self.w finns inte i variabellistan
        if self.w / self.F <= self.a:
            return True
        else:
            return False

    def ekv_7_4(self):
        #TODO self.f_1 finns inte i variabellistan, men i ekv 7.5
        #TODO kontrollera ekvation
        if self.v <= math.pow(self.b, (self.f_1 * math.pow(self.xi, -1))):
            return True
        else:
            return False

    def ekv_7_5(self):
        #TODO self.E finns inte i variabellistan
        #TODO self.I finns inte i variabellistan
        #TODO (EI)nedsänskt till l (?)
        self.f_1 = (math.pi / (2 * math.pow(self.l, 2))) * math.sqrt(self.E * self.I / self.m)

        return self.f_1

    def ekv_7_6(self):
        self.v = 4 * (0.4 + 0.6 * self.n_40) / (self.m * self.b * self.l + 200)

        return self.v

    def ekv_7_7(self):
        #TODO kontrollera ekvation
        #TODO (EI)nedsänskt till l (?)
        #TODO (EI)nedsänskt till b (?)
        self.n_40 = pow(((pow(40 / self.f_1, 2) - 1) * pow((self.b / self.l), 4) * self.E * self.I / (self.E * self.I)), 0.25)

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

	def __init__(self):
		super().__init__()

		self.beräkna()

	def beräkna(self):
		resultat = []

		resultat.append(("slankhet pelare", self.slankhet_pelare_kompression()))

		resultat.append(("slankhet balk", self.slankhet_balk_böj()))

		#TODO tryck_90

		if self.N == 0:
			resultat.append(("böjning", self.böjning()))
		elif self.N > 0:
			resultat.append(("böjning+drag", self.böjning_och_drag()))
		elif self.N < 0:
			resultat.append(("böjning+tryck", self.böjning_och_tryck()))

		if self.V != 0:
			resultat.append(("tvärkraft", self.tvärkraft()))

		if self.T != 0:
			resultat.append(("vridning", self.vridning()))

		#TODO kompression i vinkel

		return "id: {}".format(self.id), resultat

	# 1 Stress one direction ===============

	# 6.1.2
	def drag_0(self):
		res_6_1 = self.ekv_6_1()

		return res_6_1

	# 6.1.3
	def drag_90(self):
		pass

	# 6.1.4
	def tryck_0(self):
		res_6_2 = self.ekv_6_2()

		#TODO lägg in modul för stabilitet (6.3.2), om column

		return res_6_2

	# 6.1.5
	def tryck_90(self):
		res_6_3 = self.ekv_6_3()

		#TODO lägg in modul för stabilitet (6.3.2), om column


		return res_6_3

	# 6.1.6
	def böjning(self):
		res_6_11 = self.ekv_6_11()
		res_6_12 = self.ekv_6_12()

		#TODO lägg in modul för stabilitet (6.3.3), om beam

		return res_6_11, res_6_12

	# 6.1.7
	def tvärkraft(self):
		#TODO tvärkrfaft verkar vara fel
		res_6_13 = self.ekv_6_13()

		return res_6_13

	# 6.1.8
	def vridning(self):
		res_6_14 = self.ekv_6_14()

		return res_6_14

	# 2 Combined stresses ===================

	# 6.2.2
	def kompression_i_vinkel(self):
		#TODO lägg in modul för stabilitet (6.3.2), om column

		pass

	# 6.2.3
	def böjning_och_drag(self):
		res_6_17 = self.ekv_6_17()
		res_6_18 = self.ekv_6_18()

		#TODO lägg in modul för stabilitet (6.3.3), om beam

		return res_6_17, res_6_18

	# 6.2.4
	def böjning_och_tryck(self):
		res_6_19 = self.ekv_6_19()
		res_6_20 = self.ekv_6_20()

		#TODO lägg in modul för stabilitet (6.3.2), om column
		#TODO lägg in modul för stabilitet (6.3.3), om beam

		return res_6_19, res_6_20

	# 3 Stability of members ================

	# 6.3.2
	def slankhet_pelare_kompression(self):
		self.lambda_rel_y = self.ekv_6_21()
		self.lambda_rel_z = self.ekv_6_22()

		if self.lambda_rel_z <= 0.3 and self.lambda_rel_y <= 0.3:
			res_1 = self.ekv_6_19()
			res_2 = self.ekv_6_20()
		else:
			res_1 = self.ekv_6_23()
			res_2 = self.ekv_6_24()


		return res_1, res_2

	# 6.3.3
	def slankhet_balk_böj(self):
		if self.M_z > 0 and self.N == 0 and self.M_y == 0: #TODO är det verkligen M_Y? inte bara N?
			return self.ekv_6_33() #TODO värde return
		elif self.M_z > 0 and self.N < 0 and self.M_y == 0:
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
        object = StructuralUnit()
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
    self.units = []
    self.count = 0

  def add_unit(self):
    self.units.append([self.count, StructuralUnit()])
    self.units[self.count][1].id = self.count

    self.count += 1