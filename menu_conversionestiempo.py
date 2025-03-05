# -*- coding: utf-8 -*-
"""
Created on Wed Mar  5 08:08:48 2025

@author: B09S205est
"""

##Ejercicio de Clase
def convertir_a_segundos():
    while True:
        try:
            horas=int(input('Ingrese la cantidad de horas:'))
            minutos=float(input('Ingrese la cantidad de minutos:'))
            if horas<0 or minutos<0:
                print('Los valores deben ser positivos, Intente nuevamente')
                continue
            segundos=(horas*3600)+(minutos*60)
            print(f'\n {horas} horas y {minutos:.2f} minutos equivalen a {segundos} segundos')
            break
        except ValueError:
            print('Entrada invalida, Asegurese de ingresar valores numericos')
    
def convertir_desde_segundos():
    while True:
        try:
            segundos=int(input('Ingrese la cantidad de segundos:'))
            if segundos<0:
                print('El valor debe ser positivo, Intente nuevamente')
                continue
            horas=segundos//3600
            minutos=(segundos%3600)/60
            print(f'\n {segundos} segundos equivalen a {minutos:.2f} minutos y a {horas} horas')
            break
        except ValueError:
            print('Entrada invalida, Asegurese de ingresar un numero entero')

def menu():
    # Muestra el menú de opciones y gestiona la ejecución del programa
    while True:
        print('\n Conversor de Tiempo')
        print('1. Convertir desde segundos a horas y minutos')
        print('2. Convertir desde horas y minutos a segundos')
        print('3. Regresar al menú principal')
        
        try: 
            opcion = int(input('Seleccione una opción (1, 2 o 3):'))  
            
            if opcion == 1:
                convertir_a_segundos()  
            elif opcion == 2:
                convertir_desde_segundos()  
            elif opcion == 3:
                print('Saliendo del programa, Hasta Luego')
                break
            else:
                print('Opción no válida, Intente nuevamente')
        except ValueError:
            print('Entrada inválida, Ingrese un número válido')

#Ejecutar el menu principal
menu()

            