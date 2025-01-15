"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import csv

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open("files/input/data.csv", 'r') as file:
    # Leer el archivo CSV separado por espacios
        reader = csv.reader(file, delimiter='	')

        # Inicializar un diccionario para contar la suma por cada letra
        counts = {}

        # Iterar sobre las filas del archivo CSV
        for row in reader:
            # Obtener la primera columna (letra) de la fila
            letter = row[0]

            # Obtener la segunda columna de la fila
            sum = int(row[1])  

            # Obtener el minimo y maximo de la segunda columna
            min_sum = min(counts.get(letter, (sum, sum))[0], sum)
            max_sum = max(counts.get(letter, (sum, sum))[1], sum)

            # Actualizar el diccionario con los valores minimos y maximos
            counts[letter] = (min_sum, max_sum)

        # Convertir el diccionario en una lista de tuplas
        result = [(letter, max_sum, min_sum) for letter, (min_sum, max_sum) in counts.items()]

        # Ordenar la lista de tuplas por la primera columna (letra)
        result.sort(key=lambda x: x[0])

        return result
    
print(pregunta_05())