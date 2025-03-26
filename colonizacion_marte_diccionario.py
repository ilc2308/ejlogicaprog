# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 08:44:56 2025

@author: B09S205est
"""
def calcular_promedio_efectividad(peso_carga, cantidad_lanzamientos):
    return peso_carga / cantidad_lanzamientos if cantidad_lanzamientos > 0 else 0

print('Programa de monitoreo de lanzamientos a Marte')
print('Se lanzarán cargamentos a las siguientes planicies:\n')

planicies = {
    'A': {'nombre': 'Acidalia', 'carga': 0, 'lanzamientos': 0},
    'E': {'nombre': 'Elysium', 'carga': 0, 'lanzamientos': 0},
    'U': {'nombre': 'Utopia', 'carga': 0, 'lanzamientos': 0}
}

for key, data in planicies.items():
    print(f'- {key}: {data["nombre"]}')

carga_minima = 0
carga_maxima = 10000
total_lanzamientos = 15
lanzamiento_actual = 1

while lanzamiento_actual <= total_lanzamientos:
    planicie = input(f'\nLanzamiento No. {lanzamiento_actual}, ingresa la inicial de la planicie (A/E/U): ').upper()
    
    if planicie not in planicies:
        print('Error: Inicial de planicie incorrecta. Intenta nuevamente.')
        continue

    peso_carga = input('Ingresa el peso de la carga que llegó a la planicie: ')

    try:
        peso_carga = float(peso_carga)
        if not (carga_minima <= peso_carga <= carga_maxima):
            print(f'Error: El peso debe estar en el rango [{carga_minima}, {carga_maxima}]. Intenta nuevamente.')
            continue
    except ValueError:
        print('Error: El dato ingresado no es un número válido. Intenta nuevamente.')
        continue

    # Si todo es válido, actualizamos los datos
    planicies[planicie]['carga'] += peso_carga
    planicies[planicie]['lanzamientos'] += 1
    lanzamiento_actual += 1  # Se incrementa solo si la entrada es válida

print('\n*** Resultados Obtenidos ***')
for key, data in planicies.items():
    promedio = calcular_promedio_efectividad(data['carga'], data['lanzamientos'])
    print(f"{data['nombre']}: Carga total: {data['carga']} kg, Lanzamientos: {data['lanzamientos']}, Promedio: {promedio:.2f} kg/lanzamiento")
