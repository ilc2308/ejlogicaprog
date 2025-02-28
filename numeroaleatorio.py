# -*- coding: utf-8 -*-
"""
Editor de Spyder


"""

import random

# Variables
lim_inf = 1
lim_sup = 100
num_aleatorio = random.randint(lim_inf, lim_sup)

# print(f'El numero aleatorio es: {num_aleatorio}')  # Para depuración

# Entrada
conteo_intentos = 0
dato_ing = 0

# Ciclo de control
while dato_ing != num_aleatorio:
    dato_ing = int(input(f'Ingrese un número entre {lim_inf} y {lim_sup}: '))
    conteo_intentos += 1  # Incremento del conteo de intentos

    # Validar que el dato esté en el rango
    if dato_ing < lim_inf or dato_ing > lim_sup:
        print(f'El dato ingresado {dato_ing} debe estar entre {lim_inf} y {lim_sup}')
        continue  # Continuar al siguiente intento sin realizar otras comprobaciones

    # Comprobaciones del valor ingresado
    if dato_ing > num_aleatorio:
        print(f'El dato ingresado {dato_ing} es mayor que el número secreto')
    elif dato_ing < num_aleatorio:
        print(f'El dato ingresado {dato_ing} es menor que el número secreto')

# Al finalizar el ciclo
print(f'¡Felicitaciones! Adivinaste el número secreto {num_aleatorio} en {conteo_intentos} intentos.')



