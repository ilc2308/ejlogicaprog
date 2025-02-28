# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 08:01:25 2025

@author: B09S115est
"""

### Sección 3 Funciones
from datetime import datetime
## Ejemplo Funciones

def saludar():
    print('Hola hptas')

print('Programa para demostrar el uso de funciones')
saludar()
n=range(3)
for ciclo in n:
 saludar()

print('Tabla de multiplicar')
dato_ing= input('Ingresa un numero:')
numero=int(dato_ing)
def visualizar_multiplicaciones(numero):
    for multiplicador in range(1,11):
        resultado= numero*multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')

def calcular_cubo(numero):
    cubo=numero**3
    return cubo


def obtener_fecha_actual():
    # Devuelve solo la fecha actual
    fecha_obtenida=datetime.now()
    fecha_formateada=fecha_obtenida.strftime('%d-%m-%Y %H:%M:%S')
    return fecha_formateada


valor_cubico=calcular_cubo(numero)
visualizar_multiplicaciones(numero)
fecha = obtener_fecha_actual()
print("Fecha actual:", fecha)


