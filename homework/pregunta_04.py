"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para contar la cantidad de registros por cada mes
        counts = {}

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener la tercera columna (mes) de la fila
            month = row[2].split('-')[1]

            # Incrementar el contador del mes en 1
            counts[month] = counts.get(month, 0) + 1

        # Convertir el diccionario en una lista de tuplas
        result = list(counts.items())

        # Ordenar la lista de tuplas por la primera columna (mes)
        result.sort(key=lambda x: x[0])

        # Imprimir la lista de tuplas
        print(result)

        return result
    
pregunta_04()