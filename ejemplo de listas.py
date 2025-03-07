# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 08:01:29 2025

@author: B09est155
"""
# Programa para demostrar el funcionamiento y manipulación de una lista
print('Programa para demostrar el funcionamiento y manipulación de una lista')

# Crear una lista
lista = [15, 20, 40, 0, 8678]

# Imprimir los valores de la lista
print('Mi lista tiene los valores:', lista)

# Mostrar la longitud de la lista
print(f'Mi lista tiene {len(lista)} valores')

# Imprimir los elementos de la lista uno por uno
print('Mi lista colocando un elemento por línea es:')
for e in lista:
    print(e)

# Modificar un elemento de la lista
lista[3] = 5643256
print('Después de modificar el cuarto elemento, la lista es:', lista)


import random

# Crear una lista vacía
lista_aleatoria = []

# Llenar la lista con 100 números aleatorios entre 1 y 1000 usando un ciclo for
for _ in range(100):
    lista_aleatoria.append(random.randint(1, 1000))

# Función para clasificar los números en pares e impares
def clasificar_pares_impares(lista):
    pares = []
    impares = []
    
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    return pares, impares

# Función para imprimir los números 10 por línea
def imprimir_por_linea(lista, elementos_por_linea=10):
    for i in range(0, len(lista), elementos_por_linea):
        print(lista[i:i+elementos_por_linea])

# Clasificar la lista en pares e impares
pares, impares = clasificar_pares_impares(lista_aleatoria)

# Imprimir los números pares
print("Números pares:")
imprimir_por_linea(pares)

# Imprimir los números impares
print("\nNúmeros impares:")
imprimir_por_linea(impares)
