import sys
from src.genera_archivos import enteros_aleatorios
from src.borrador import borrar_archivos


def obtener_datos():
    return ("suma", 10)


def main():
    operacion, entero = obtener_datos()

    # Obtenemos los valores para operar con ellos
    # Operamos con los numeros y los guardamos en el archivo resultados


if __name__ == "__main__":
    borrar_archivos()
    num = 10
    archivo = "datos.txt"
    enteros_aleatorios(num, archivo)
    main()
