# -*- coding: utf-8 -*-

##Clase 01 semana 06

#IMC = Peso (kg) / Estatura(m)^2

print('Programa para calcular el índice de masa corporal')

datos_erroneos = True

while datos_erroneos:
    try:
        # Intentamos obtener el peso
        try:
            peso = float(input('Ingresa tu peso en Kg: '))
        except ValueError:
            print('El dato del peso fue erróneo. Por favor ingresa un valor numérico válido.')
            continue  # Si el peso es erróneo, pedimos que lo ingrese nuevamente

        # Intentamos obtener la estatura
        try:
            estatura = float(input('Ingresa tu estatura en m: '))
        except ValueError:
            print('El dato de la estatura fue erróneo. Por favor ingresa un valor numérico válido.')
            continue  # Si la estatura es errónea, pedimos que lo ingrese nuevamente

        # Realizamos el cálculo si ambos datos son correctos
        indice = peso / (estatura ** 2)
       

        # Si no hubo errores, salimos del bucle
        datos_erroneos = False
    
    except Exception as e:
        print(f'Ocurrió un error inesperado: {e}')

#Resultados
print(f'Tu índice de masa corporal es {indice:.2f}')
#Categorizar el indice de masa corporal
if indice <18.5:
    print('Estas en bajo peso.')
elif indice >=18.5 and indice <25:
    print('Estas en peso normal')
elif indice >=25 and indice < 29.9:
    print('Estas en sobre peso')
else:
    print('Estas en Obesidad')

## Ciclo For:

print('Programa para demostrar el ciclo for:')
num=range(0,21,2)
conteo=0
for i in num:
    print(f'El valor de la variable es {i}')
    conteo+=1
print(f'Se ejecutó {conteo} veces')
