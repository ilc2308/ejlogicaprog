"Ismael López C."
import random
#Programa para seleccionar combinaciones de empanadas
#Listas con opciones de empanadas
colores=["Amarillo","Verde","Morado"]
masas=["Maíz","Quinua","Trigo"]
rellenos=["Papa","Ranchera","Verduras"]

#Diccionario para almacenar combinaciones de empanadas
diccionario_empanadas={}
#Generacion de empanadas aleatorias
cant_max_emp=300
contador_emp=0
while contador_emp<cant_max_emp:
    #Generar una combianción aleatoria
    masa=random.choice(masas)
    color=random.choice(colores)
    relleno=random.choice(rellenos)
    llave_emp=(masa,color,relleno)
    
    #Actualizar diccionario
    if llave_emp in diccionario_empanadas:
        diccionario_empanadas[llave_emp]+=1
    else:
        diccionario_empanadas[llave_emp]=1
    contador_emp+=1

#Función para hallar la combinación exitosa
def hallar_empanada_exitosa(diccionario):
    mayor_frecuencia=0
    comb_exitosa=None
    claves_emp=list(diccionario.keys())
    indice=0
    while indice < len(claves_emp):
        clave=claves_emp[indice]
        cantidad_emp=diccionario[clave]
        
        if cantidad_emp>mayor_frecuencia:
            mayor_frecuencia=cantidad_emp
            comb_exitosa=clave
        indice+=1
    return comb_exitosa,mayor_frecuencia

#Obtener combinacion más frecuente
comb_exitosa,cantidad_emp=hallar_empanada_exitosa(diccionario_empanadas)
#Porcentaje
porcentaje=(cantidad_emp/cant_max_emp)*100

#Resultados
print("===RESULTADOS DE LA SIMULACIÓN===")
print(f"Masa: {comb_exitosa[0]}")
print(f"Color: {comb_exitosa[1]}")
print(f"Relleno: {comb_exitosa[2]}")
print(f"Cantidad producida:{cantidad_emp}")
print(f"Porcentaje del total:{porcentaje:.2f} %")


            
        
    





