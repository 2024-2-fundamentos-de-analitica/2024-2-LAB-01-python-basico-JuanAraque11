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
        reader = csv.reader(file, delimiter=' ')

        # Imprimir las primeras dos filas
        for i in range(2):
            print(next(reader))


    #    second_column_sum = sum(int(row[1]) for row in reader)
    #print(second_column_sum)
    # return second_column_sum

pregunta_01()