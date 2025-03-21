# -*- coding: utf-8 -*-
"""
Created on Fri Mar 21 08:03:52 2025

@author: B09S115est
"""

#Programa para validar palindromos

#Metodo 1: comparar con reverso
def comprobar_palindromo_m1(frase):
    frase_limpia = frase.replace(" ", "").lower()
    return frase_limpia == frase_limpia[::-1] 

#Metodo 2: Verificar caracter por caracter
def comprobar_palindromo_m2(frase):
    frase_limpia = frase.replace(" ", "").lower()  # Eliminar espacios y poner en minúsculas
    longitud = len(frase_limpia)
    for i in range(longitud // 2):  # Comparar desde ambos extremos hacia el centro
     if frase_limpia[i] != frase_limpia[longitud - i - 1]:
         return False
    return True

#Metodo 3: Usar dos punteros
def comprobar_palindromo_m3(frase):
  frase_limpia = frase.replace(" ", "").lower()  # Eliminar espacios y poner en minúsculas
  izquierda = 0
  derecha = len(frase_limpia) - 1
    
  while izquierda < derecha:
        if frase_limpia[izquierda] != frase_limpia[derecha]:
            return False
        izquierda += 1
        derecha -= 1
  return True

#Función para visualizar el menú
def mostrar_menu():
    print("\nMenú de Verificación de Palíndromos")
    print("1. Verificar con método 1 (Comparar con reverso)")
    print("2. Verificar con método 2 (Comparar carácter por carácter)")
    print("3. Verificar con método 3 (Usar punteros)")
    print("4. Salir")

#Funcion principal
def main_principal():
    # Solicitar al usuario que ingrese la frase al principio
    frase = input("Introduce la frase que deseas verificar: ")
    
    opcion = None  # Inicializamos la opción
    while opcion != '4':  
        mostrar_menu()  
        opcion = input("Selecciona una opción (1-4): ")
        
        # Verificación de la opción seleccionada
        if opcion == '1':  
            resultado = comprobar_palindromo_m1(frase)
            if resultado:
                print("Resultado Método 1: Es palíndromo")
            else:
                print("Resultado Método 1: No es palíndromo")
        
        elif opcion == '2':  
            resultado = comprobar_palindromo_m2(frase)
            if resultado:
                print("Resultado Método 2: Es palíndromo")
            else:
                print("Resultado Método 2: No es palíndromo")
        
        elif opcion == '3':  
            resultado = comprobar_palindromo_m3(frase)
            if resultado:
                print("Resultado Método 3: Es palíndromo")
            else:
                print("Resultado Método 3: No es palíndromo")
        
        elif opcion == '4':  # Si la opción es 4, salir del programa
            print("Saliendo del programa. ¡Hasta luego!")
        
        else:  
            print("Opción no válida. Por favor, selecciona una opción válida.")


# Ejecutar el programa
main_principal()

 

  
    