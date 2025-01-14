"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """

    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para contar la suma por cada letra
        sums = {}

                # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener la primera columna (letra) de la fila
            letter = row[0]

            # Obtener la segunda columna (suma) de la fila
            sum = int(row[1])  
            # Incrementar el contador de la letra en la suma
            sums[letter] = sums.get(letter, 0) + sum  

        # Convertir el diccionario en una lista de tuplas
        result = list(sums.items())

        # Ordenar la lista de tuplas por la primera columna (letra)
        result.sort(key=lambda x: x[0])

        # Imprimir la lista de tuplas  
        print(result)
    return result 
