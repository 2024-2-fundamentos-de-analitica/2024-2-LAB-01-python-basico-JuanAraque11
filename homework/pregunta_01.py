"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    
    with open("files/input/data.csv", 'r') as file:
        # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar la variable para almacenar la suma
        suma = 0

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Convertir la segunda columna en un número entero y agregarla a la suma
            suma += int(row[1])

        # Imprimir la suma
        print(suma)

    return  suma
