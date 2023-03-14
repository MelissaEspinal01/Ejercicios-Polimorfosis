class Paseo:
    def __init__(self, nombreMascota):
        self.nombreMascota = nombreMascota

class Melissa(Paseo):
    def Paseo(self):
        return "A melissa le toca pasear a {}".format(self.nombreMascota)

class Jhonny(Paseo):
    def Paseo(self):
        return "A jhonny le toca pasear a {}".format(self.nombreMascota)

Mascota1 = Paseo("Max")
Mascota2 = Paseo("Snoopy")
Paseador1 = Melissa("Max")
Paseador2 = Jhonny("Snoopy")

print(Paseador1.Paseo())
print(Paseador2.Paseo())