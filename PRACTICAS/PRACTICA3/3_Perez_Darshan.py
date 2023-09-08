#Pérez Servin Darshan Israel
#PRACTICA 3

print("\n//////////////////////////////////////////////////////")
print("-= ¡BIENVENID@ A LA GESTIÓN DE LA LISTA DE TAREAS! =-")
print("//////////////////////////////////////////////////////")
print("\n-= OPCIONES =-")
print("1. Agregar Tarea")
print("2. Listar Tareas")
print("3. Marcar Tarea como Completada")
print("4. Eliminar Tarea")
print("5. Salir")

ListaTareas = []
contadorTareas = 0
while True:
    opcionOMG = input("\n\tElige una opción: ")
    #----------------------------------------------------------------------------------------------------------------#
    # OPCION 1 #
    if opcionOMG == "1":
        TareaIngresada = input("\n1. Ingresa la descripcion de la tarea: ")
        ListaTareas.append({"descripcionTarea": TareaIngresada, "completada": False}) #Para agregar claves a la lista, se necesita {} y el append
        contadorTareas += 1
        print("Tarea agregada con éxito.")
        
    #----------------------------------------------------------------------------------------------------------------#
    # OPCION 2 #
    elif opcionOMG == "2":
        print("\n2. Lista de tareas: ")
        if contadorTareas > 0:

            for i, j in enumerate(ListaTareas): #j esta en el numero de tareas de la lista
                estado = "[X]" if j["completada"] else "[ ]" #Para que aparezca [x] o [ ] definimos si es true o false
                print(i+1,".", estado, j["descripcionTarea"])
        else:
            print("No hay tareas que mostar.")

    #----------------------------------------------------------------------------------------------------------------#
    # OPCION 3 #
    elif opcionOMG == "3":
        numero_tarea = int(input("\nIngresa el número de la tarea que deseas marcar como completada: "))
        #Cuando usamos input, nos devuelve un string, asi que lo forzamos con un int para que sea un entero
        if 1 <= numero_tarea <= contadorTareas:
            #Comparamos que no sea negativo con "1 <="
            #Comparamos que no sea un numero que no exista dentro de la lista con "<= contadorTareas"

            ListaTareas[numero_tarea - 1]["completada"] = True
            print("Tarea marcada como completada.")
        else:
            print("Número de tarea inválido.")

    #----------------------------------------------------------------------------------------------------------------#
    # OPCION 4 #
    elif opcionOMG == "4":
        #Mismo procedimiento que en la opcion 3:
        numero_tarea = int(input("\nIngresa el número de la tarea que deseas eliminar: "))
        if 1 <= numero_tarea <= contadorTareas:
            
            tarea_eliminada = ListaTareas.pop(numero_tarea - 1) # "-1" por que siempre las listas se cuentan desde 0
            contadorTareas -= 1
            #print(f"Tarea '{tarea_eliminada['descripcion']}' eliminada con éxito.")
            print("Tarea ", tarea_eliminada["descripcionTarea"], " eliminada con éxito.")
        else:
            print("Número de tarea inválido.")

    #----------------------------------------------------------------------------------------------------------------#
    # OPCION 5 #
    elif opcionOMG == "5":
        print("\n¡Hasta luego!\n")
        break

    #----------------------------------------------------------------------------------------------------------------#
    else:
        print("\nOpción inválida.")



