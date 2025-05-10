# -*- coding: utf-8 -*-
"""
Created on Sat May 10 12:25:46 2025

@author: ISMAEL LÓPEZ CARDOZO
"""

import csv
print('Programa para generar archivos CSV')

#Datos del encabezado
encabezado=[]
encabezado.append('Nombre')
encabezado.append('Edad')
encabezado.append('Ciudad')

#Datos del contenido del archivo
personas = []  # Lista vacía
# Agregamos a Ana
ana = []                     
ana.append("Ana")           
ana.append(30)               
ana.append("Bogotá")         
personas.append(ana)         
# Agregamos a Luis
luis = []
luis.insert(0, "Luis")       
luis.insert(1, 25)
luis.insert(2, "Medellín")
personas.append(luis)
# Agregamos a Carla
carla = []
carla.append("Carla")
carla.append(28)
carla.append("Cali")
personas.append(carla)


# Función para escribir el encabezado:
def escribir_encabezado(nombre_archivo, encabezado):
    with open(nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerow(encabezado)  # Solo una fila para el encabezado

# Función para escribir los datos del contenido:
def escribir_datos(nombre_archivo, datos):
    with open(nombre_archivo, mode="a", newline="", encoding="utf-8") as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(datos)  # Varias filas


# Función principal:
def main():
    nombre_archivo = "personas.csv"
    escribir_encabezado(nombre_archivo, encabezado)
    escribir_datos(nombre_archivo, personas)

    print("Archivo CSV generado con exito.")

#Programa Principal
if __name__=='__main__':
    main()