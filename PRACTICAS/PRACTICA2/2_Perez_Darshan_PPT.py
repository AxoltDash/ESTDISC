#Pérez Servin Darshan Israel
print("//////////////////////////////////////////////////////////////")
print("-= ¡BIENVENID@ AL JUEGO IMPOSIBLE DE PIEDRA PAPEL O TIJERA! =-")
print("//////////////////////////////////////////////////////////////")
i =  True
j =  True

while i == True:
    j =  True #Reinicia sistema para peguntar si desea volver a jugar
    
    print()
    jugada_usuario = input("Ingresa tu jugada (piedra, papel o tijeras): ")

# Determina quién gana
    if jugada_usuario == "piedra" or jugada_usuario == "PIEDRA" or jugada_usuario == "Piedra":
        print("\t¡Computadora usó papel! Perdiste.")
    elif jugada_usuario == "papel" or jugada_usuario == "PAPEL" or jugada_usuario == "Papel":
        print("\t¡Computadora usó tijeras! Perdiste.")
    elif jugada_usuario == "tijeras" or jugada_usuario == "TIJERAS" or jugada_usuario == "Tijeras":
        print("\t¡Computadora usó piedra! Perdiste.")
    else:
        print("\tNo ingresaste una jugada válida...")

#Sistema para volver a jugar
    while j == True:
        print()
        print("¿Quíeres jugar otra vez?")
        PlayOtraVez = input("Elije una opción (Si/No) : ")
        if PlayOtraVez == "Si" or PlayOtraVez == "si" or PlayOtraVez == "SI":
            i = True
            j = False #En caso de cualquier fallo
        elif PlayOtraVez == "No" or PlayOtraVez == "no" or PlayOtraVez == "NO":
            i = False
            j = False #En caso de cualquier fallo
        else:
            print("Me saliste bien Azteca ¡Escribe bien!... Asi que te lo vuelvo a preguntar:")
            j = True
#Resetea el sistema
jugada_usuario = ()