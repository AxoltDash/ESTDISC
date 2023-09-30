#Pérez Servin Darshan Israel
#PROYECTO 1
import sys
import unicodedata #Para evitar problemas en los strings de operaciónes

from src.genera_archivos import enteros_aleatorios
from src.borrador import borrar_archivos

print("\n/////////////////////////////////////////////////////////")
print("-= ¡BIENVENID@ AL PROGRAMA DE OPERACIONES MATEMÁTICAS! =-")
print("/////////////////////////////////////////////////////////\n")

def obtener_datos():
    return ("DiviSION   ", 10)

def main():
    operacion, entero = obtener_datos()

    #=============================================================================

    #Guardamos los enteros de datos.txt en una lista llamada lista_numeros
    with open("datos.txt", "r") as archivoDatos:
        lista_numeros = []
        # Lee cada línea
        for linea in archivoDatos:
            # Convierte la línea a un número entero y agrega a la lista
            numero = int(linea.strip())  # strip() elimina los espacios en blanco y saltos de línea
            lista_numeros.append(numero)
    print("\nLos números son:\n",lista_numeros,"\n")

    #=============================================================================

    #Para iniciar el programa se debe verifican los datos (En este caso se guardarán en booleans)
    #I) Verificamos que el string operación sea válido:
    operacion = operacion.rstrip() #Quitamos espacios
    operacion = operacion.lower() #Quitamos mayúsculas
    operacion = operacion.replace("ó", "o") #Quitamos acentos "ó":
    
    operaciones_validas = ["suma", "resta", "multiplicacion", "division"]
    
    if operacion in operaciones_validas:
        StarIf_Operación = True
    else:
        print("El operador que usted ingresó no es correcto")
        print("Por favor, ingrese uno de los siguientes operadores a la próxima:")
        print("\t - suma\n\t - resta\n\t - multiplicación\n\t - división")
        StarIf_Operación = False

    #II) Verificamos que el entero sea un valor entero para continuar:
    if isinstance(entero, int):
        StarIf_Entero = True
    else:
        print("El valor de entero que usted ingresó no es correcto.")
        StarIf_Entero = False

    #=============================================================================
    
    #Vamos a guardar los resultados de segun su operación:
    #(Si y solo si se ingresó los valores correctos)
    if ((StarIf_Operación and StarIf_Entero) == True):
        resultado = []

        if operacion == "suma":
            print("El resultado de la ",operacion," con ",entero," es:")
            for i in lista_numeros:
                resultado.append(i + entero)  
            print(resultado)   

        elif operacion == "resta": 
            print("El resultado de la ",operacion," con ",entero," es:")
            for j in lista_numeros:
                resultado.append(j - entero)  
            print(resultado)   

        elif operacion == "multiplicacion": 
            print("El resultado de la ",operacion," con ",entero," es:")
            for k in lista_numeros:
                resultado.append(k * entero)  
            print(resultado) 

        elif operacion == "division":
            #Verificamos que el usuario no meta el valor 0
            if (entero != 0):
                print("El resultado de la ",operacion," entre ",entero," es:")
                for l in lista_numeros:
                    resultado.append(l / entero)  
                print(resultado)
            else:
                print("¡No se puede dividir entre cero!")
        else: 
            print("Usted no ingresó un operador válido. Error inesperado")

    #=============================================================================

        #Empezamos a guardar los resultados de la cadena en resultados.txt
        with open("resultados.txt", "w") as archivoDatosResultados:
            # Lee cada línea
            for lineaR in resultado:
                archivoDatosResultados.write(str(lineaR) + "\n")

        print("\nSe han guardado los números en 'resultados.txt'.")

    #=============================================================================

    #Si no inició el programa de operación por variables incorrectas
    else:
        print("No se pudo iniciar las operaciones debido a que se ingresaron valores incorrectos.")
        print("Por favor, inténtelo de nuevo.")
    
    #=-=-=-=-=-
    


if __name__ == "__main__":
    borrar_archivos()
    num = 10
    archivoDatos = "datos.txt"
    enteros_aleatorios(num, archivoDatos)
    main()
