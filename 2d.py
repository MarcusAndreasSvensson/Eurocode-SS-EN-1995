import pymunk as pm

space = pm.Space()

b = pm.Body()
b.Posistion = 0, 0

shape = pm.Poly(b, [(0,0), (0,10), (40,10), (40,90), (0,90), (0,100),
                    (100,100), (100,90), (60,90), (60,10), (100, 10), (100,0)])

print(shape.get_vertices())
print(shape.area)
print(shape.moment)
print(pm.moment_for_poly(shape.mass, shape.get_vertices()))


def beräkna_tyngdpunkt():
    pass


def rita_profil():
    pass


def placeholder():
    pass