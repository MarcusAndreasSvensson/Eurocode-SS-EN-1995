import pickle
import math

# Hela filen ska använda SI-enheter

# Skapar de olika punkterna för det kordinatisystem som stomlinjer baseras på
def skapa_koordinater():
	koordinater = [[0, 0, 0]]

	target_x = 81
	target_y = 81
	target_z = 51
	#i = 0

	for delta_x in range(1, target_x):
		for delta_z in range(1, target_z):
			for delta_y in range(1, target_y):
				koordinater.append([delta_x, delta_y, delta_z])
				#print([delta_x, delta_y, delta_z])
				#i += 1
				#print(i)
	#print(koordinater)


# Allt detta kanske bör hamna i .csv istället för pickle (Filstorlek)
class SkapaLaster:

    def __init__(self):
        self._skapa_snölast()
        self._skapa_vindlast()
        self._skapa_nyttig_last()
        self._skapa_maskinlast()

    def _skapa_snölast(self):
        # Genererar snölaster
        self.snölast = []
        self.min_snölast = 1
        self.max_snölast = 21

        for last in range(self.min_snölast, self.max_snölast):
            self.snölast.append(last/2)

    def _skapa_vindlast(self):
        # Genererar vindlaster
        self.vindlast = []
        self.min_vindlast = 1
        self.max_vindlast = 16

        for last in range(self.min_vindlast, self.max_vindlast):
            self.vindlast.append(last/10)

    def _skapa_nyttig_last(self):
        #genererar nyttiglaster
        self.nyttig_last = []
        self.min_nyttig_last = 1
        self.max_nyttig_last = 25

        for last in range(self.min_nyttig_last, self.max_nyttig_last):
            self.nyttig_last.append(last/4)

    def _skapa_maskinlast(self):
        #genererar maskinlaster
        self.maskinlast = []
        self.min_maskinlast = 1
        self.max_maskinlast = 40

        for last in range(self.min_maskinlast, self.max_maskinlast):
            self.maskinlast.append(last)

if __name__ == "__main__":
    skapa_koordinater()

"""
tankar:
Bör man ha med både betong, trä och stål i samma modell för att kunna ha med vad som är mest 
kostnadseffektivt som parameter?


"""

