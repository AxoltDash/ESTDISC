#Pérez Servin Darshan Israel
import time
print("///////////////////////////////////////////////////////")
print("-= ¡BIENVENID@ AL ASOMBROSO PROGRAMA IMPRIME TABLAS! =-")
print("///////////////////////////////////////////////////////")
EJECUTAR = input("¿Quieres ejecutar el programa? (Si/No): ")

#Generador de las tablas:
if EJECUTAR == "Si" or EJECUTAR == "si" or EJECUTAR == "SI":
    for i in range(1, 11):
        print(f"Tabla de multiplicar del {i}:")
        for j in range(1, 11):
            resultado = i * j
            print(f"{i} x {j} = {resultado}")
        print()  # Agrega una línea en blanco entre tablas
        time.sleep(0.4) #Un pequeño delay
        
    print("Hasta aquí llegó el ASOMBROSO programa... ¿Gracias por ejecutar?")
#Si dices que no o cualquier otra cosa:
else:
    print()
    print("Bueno, se intentó...")
