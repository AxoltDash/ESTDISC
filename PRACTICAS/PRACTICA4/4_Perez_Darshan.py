#Pérez Servin Darshan Israel
#PRACTICA 4
import unittest
import time

print("\n//////////////////////////////////////////////////////////////")
print("-= ¡BIENVENID@ AL CÓDIGO PARA VER SI FUNCIONAN LAS PRUEBAS! =-")
print("//////////////////////////////////////////////////////////////\n")

#EL CODIGO QUE ESTA ENTRE "####" ES NADA MAS PARA IMPRIMIR UN MESNAJE
#MORADO Y QUE TENGA PUNTOS DE ESPERA, FAVOR DE IGNORAR :d
###################################################################
color_magenta = "\033[95m"
color_reset = "\033[0m"
mensaje = "\tIniciando épicamente"
#Imprime el mensaje en color magenta
print(f"{color_magenta}{mensaje}", end=" ")
#Imprime retraso con puntitos
for _ in range(6):
    print(".", end="", flush=True)
    time.sleep(0.5)
print(f"{color_reset}")
print("\n\nLa espera nada más fue para darle epicidad\n")
###################################################################

#AQUÍ EMPIEZA LA PRÁCTICA:

def PPoT(jugadaUsr):
    if jugadaUsr == "TIJERAS":
        return "PIEDRA"
    elif jugadaUsr == "PIEDRA":
        return "PAPEL"
    elif jugadaUsr == "PAPEL":
        return "TIJERAS"

class testeoEpicardo (unittest.TestCase):
    def testeoTijeras(self):
        self.assertEqual(PPoT("TIJERAS"), "PIEDRA")
    def testoPiedra(self):
        self.assertEqual(PPoT("PIEDRA"), "PAPEL")
    def testoPapel(self):
        self.assertEqual(PPoT("PAPEL"), "TIJERAS")

if __name__ == '__main__':
    unittest.main()
