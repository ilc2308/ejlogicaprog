# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 16:09:40 2025

@author: ISMAEL LÓPEZ CARDOZO
"""

# Esta linea es un comentario
#Caracteres:
#Letras: a b c d A H K L
#Numeros: 0 1 2 3 4 5 6 7 8 9
#Simbolos: @ # $ % & * + - / = ? ^ _ ()



print('¡Hola Mundo!')  
print('El numero PI es:'+ str(3.141592))
#Declaracion de Variables:darle un nombre y asignarle un valor
frase = 'Hola Itaguí'
frase2='Me gusta vivir acá'
print(frase,frase2)
print(frase + '\n' +frase2)
print(type(frase),type(frase2))
print(frase)
print(type(str(frase)))

#Operaciones Aritmeticas
# + - Suma y resta
# * \ Multiplicación y división
# ** Potencia
# // División entera
# % Modulo
print(3+12,5-23,8*3,12/5,2**5,12//7,21%3)
print(3+12*5+27/3)

nombre = input('Nombre?')
print('Hola',nombre)

#Ejercicio 1

horas= input('Horas?')
minutos= 60*int(horas)
print('La Cantidad de minutos son:',minutos)