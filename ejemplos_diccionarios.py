# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 08:05:10 2025

@author: B09S205est
"""

##Diccionarios en python

print('Programa para demostrar el funcionamiento de un diccionario')

#Función que visualiza un diccionario
def visualizar_dic(dato_diccionario):
    print('El contenido del diccionario es:')
    for llave in dicc.keys():
        print(f'\n Llave:{llave} \n valor:{dicc[llave]}')
   
    print(f'El diccionario es de tipo{type(dato_diccionario)} y tiene {len(dato_diccionario)} elementos')
    
def visualizar_llaves(dato_llaves):
    print('las llaves del diccionario son:')
    for llave in dato_llaves:
        print(llave)

    

dicc={
      'recorcholis':'expresión autoctona tipica de la región central de Colombia',
      'Futbol':'Deporte en el que todo un pais puede llorar al mismo tiempo',
      'Zapato':'Prenda de vestir que se usa para caminar',
      'Collar':'Accesorio que se usa en el cuello',
      'Palindromo':'Palabra que se lee igual al derecho y al reves'}

print(f'El diccionario es de tipo{type(dicc)} y tiene {len(dicc)} elementos')

print('las llaves del diccionario son:')
for llave in dicc.keys():
    print(llave)


#Buscar elementos de la lista
llave_buscada=input('\n Ingrese la llave que desea buscar:')

if llave_buscada not in list(dicc.keys()):
    print('La llave no existe en el diccionario')
else:
    print(f'La definición para {llave_buscada} es \n {dicc[llave_buscada]}')

#Agregar llaves
nueva_llave=input('\n Ingrese la nueva llave que:')
nueva_definicion=input('\n Ingrese la nueva definición:')
dicc[nueva_llave]=nueva_definicion

visualizar_dic(dicc)
visualizar_llaves(dicc.keys())