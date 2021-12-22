"""
En este archivo una materia es un diccionario con los siguientes campos:
    - "nombre" : str = Nombre de la materia (en computación)
    - "año" : int = Año en el cuál está la materia
    - "cuatrimestre" : int = Cuatrimestre en el cuál está la materia
    - "otrasCarreras" : dict = Misma materia en las otras carreras
        Un diccionario con clave = carrera, valor = Nombre en esa carrera
    - "extra" : str = String extra para esa materia

Los nombres de las materias tienen que coincidir con el nombre que aparece en la carpeta
"""

import os

def generarTexto(materia : dict) -> str:
    """
    Genera el texto que va para la materia en el README.md

    Una materia es un diccionario con los siguientes campos:
    - "nombre" : str = Nombre de la materia (en computación)
    - "año" : int = Año en el cuál está la materia
    - "cuatrimestre" : int = Cuatrimestre en el cuál está la materia
    - "otrasCarreras" : dict | list str = misma materia en las otras carreras
        Un diccionario con clave = carrera, valor = nombre en esa carrera si la carrera es importante
        Una lista si la carrera no es importante (o si es muy complicado ponerla, como en Álgebra)
    - "extra" : str = String extra para esa materia
    """

    # nombreSolo_TodasLasCarreras = f"{materia["nombre"]} - {materia["otrasCarreras"][carrera1]} - {materia["otrasCarreras"][carrera2]} - ... - {materia["otrasCarreras"][carreraN]}"
    nombreSolo_TodasLasCarreras = f"{materia['nombre']}"
    for nombre in materia["otrasCarreras"]:
        nombreSolo_TodasLasCarreras += f" - {nombre}"

    # Si no hay otras carreras
    if len(materia["otrasCarreras"]) == 0: # len funciona para listas y para diccionarios
        nombreCarrera_TodasLasCarreras = f"{materia['nombre']} de la carrera Ciencias de la Computación"
    else: # Si hay otras carreras
        if type(materia["otrasCarreras"]) == list:
            nombreCarrera_TodasLasCarreras = f"{materia['nombre']}"
            for nombre in materia["otrasCarreras"]:
                nombreCarrera_TodasLasCarreras += f" - {nombre}"
        elif type(materia["otrasCarreras"]) == dict:
            nombreCarrera_TodasLasCarreras = f"{materia['nombre']} (Computación)"
            for carrera, nombre in materia["otrasCarreras"].items():
                nombreCarrera_TodasLasCarreras += f" - {nombre} ({carrera})"

    carpetaMateria = f"..{os.sep}{materia['año']}° {materia['cuatrimestre']}C {materia['nombre']}"
    exámenesQueHay = set(os.listdir(carpetaMateria)) - {".git", "README.md"}
    hayExámenes = len(exámenesQueHay) > 0

    texto = f"""\
# Exámenes viejos {nombreSolo_TodasLasCarreras} - FaMAF

Exámenes viejos de la materia {nombreCarrera_TodasLasCarreras} de FaMAF.

Cualquier contribución con un examen viejo que no esté es bienvenida, ya sea como pull request, o como mandar el examen por cualquier otro medio.
{"(En esta materia todavía nadie subio ningún exámen, pero igual se puede contribuir)" if not hayExámenes else ""}

{f"{materia['extra']}" if "extra" in materia else ""}
        """
    
    return texto

print(generarTexto({"nombre":"Introducción a los algoritmos", "año":1, "cuatrimestre":1, "otrasCarreras":[]}))
print("------------------------------")
print(generarTexto({"nombre":"Álgebra", "año":1, "cuatrimestre":2, "otrasCarreras":["Álgebra 2", "Álgebra lineal"]}))
print("------------------------------")
print(generarTexto({"nombre":"Análisis matemático 2", "año":1, "cuatrimestre":2, "otrasCarreras":{"Matemática Aplicada": "Calculo 2"}}))
