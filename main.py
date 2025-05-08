# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

"Manipulación de Archivos"
print("Programa para la manipulación de archivos")

"Librerías"
import csv
import json
import xml.etree.ElementTree as ET
try:
    import yaml
except ImportError:
    yaml=None
    print("NOTA:El formato YAML no se podrá generar porque 'pyyaml' no está instalado")
"Archivos de Salida"
xml_vf='salida.xml' 
json_vf='salida.json'
yaml_vf='salida.yaml'   
"Funciones secundarias:"

"Función para comprobar si se puede tratar el contenido como una lista"
def comprobar_si_es_lista(texto):
    return ';' in texto

"Función para realizar el procesamiento al archivo.csv"
def procesar_csv(csv_nombre):
    datos=[]
    try:
        with open(csv_nombre, newline='',encoding='utf-8') as archivo:
            lector=csv.DictReader(archivo) #Lee las columnas como claves
            for fila in lector:
                registro={}
                for columna,texto_original in fila.items():
                    texto=texto_original.strip() #Se quitan espacios
                    
                    if texto.isdigit():
                        registro[columna]=int(texto)
                    else:
                        try:
                            registro[columna]=float(texto)
                        except:
                            if comprobar_si_es_lista(texto):
                                lista=[item.strip() for item in texto.split(';')]
                                registro[columna]=lista
                            else:
                                registro[columna]=texto
            datos.append(registro)
    except FileNotFoundError:
        print(f"ERROR: No se encontró el archivo '{csv_nombre}'.")
    
    return datos

#Funcion para guardar en XML:
def guardar_XML(datos):
    raiz=ET.Element('Registros')
    for fila in datos:
        registro=ET.SubElement(raiz,'Registro')
        for campo, valor in fila.items():
            if type(valor)==list:
                lista_elemento=ET.SubElement(registro,campo)
                for item in valor:
                    subitem=ET.SubElement(lista_elemento,'item')
                    subitem.text=str(item)
                else:
                    campo_elemento=ET.SubElement(registro,campo)
                    campo_elemento.text=str(valor)
    ET.ElementTree(raiz).write(xml_vf,encoding='utf-8',xml_declaration=True)
    print(f"Archivo XML guardado como '{xml_vf}'.")
    
#Función para guardar en JSON:
def guardar_JSON(datos):
    with open(json_vf,'w',encoding='utf-8') as archivo:
        json.dump(datos,archivo,indent=4,ensure_ascii=False)
    print(f"Archivo JSON guardado como '{json_vf}'.")

#Función para guardar en YAML:
def guardar_YAML(datos):
    if yaml is None:
        print(f"No se creó el archivo '{yaml}' porque falta la librería")
        return
    with open(yaml_vf,'w',encoding='utf-8') as archivo:
        yaml.dump(datos,archivo,allow_unicode=True,sort_keys=False)
    print(f"Archivo YAML guardado como '{yaml_vf}'.")
    
"Función principal"
def main():
    nombre_archivo=input("Escribe el nombre de tu archivo CSV:").strip()
    datos_csv=procesar_csv(nombre_archivo)
    
    if datos_csv:
        guardar_XML(datos_csv)
        guardar_JSON(datos_csv)
        guardar_YAML(datos_csv)
        print("\n ¡Listo! Los 3 archivos se han generado correctamente.")
    else:
        print("No se pudo convertir el archivo. Revisa el nombre o el contenido")
        
#Programa Principal
if __name__=='__main__':
    main()

                    
                            
                    
