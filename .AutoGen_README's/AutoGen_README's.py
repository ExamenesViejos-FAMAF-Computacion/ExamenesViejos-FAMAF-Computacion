"""
Este archivo genera el README.md para cada materia


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

def pathCarpetaMateria(materia : dict) -> str:
    """
    Calcula el path desde la ubicación de este archivo hasta la carpeta de la materia
    Tambien verifica que el path exista, y si no lo hace, lanza una excepción
    """
    path = f"..{os.sep}{materia['año']}° {materia['cuatrimestre']}C {materia['nombre']}"
    if not os.path.exists(path):
        raise Exception(f"El path \"{path}\" no existe")
    return path


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

    # Si no hay otras carreras
    if "otrasCarreras" not in materia: # len funciona para listas y para diccionarios
        nombreCarrera_TodasLasCarreras = f"{materia['nombre']} de la carrera Ciencias de la Computación"
    elif materia["otrasCarreras"] == None: # Está en otras carreras, pero con el mismo nombre
        nombreCarrera_TodasLasCarreras = f"{materia['nombre']}"
    else: # Si hay otras carreras
        if type(materia["otrasCarreras"]) == list:
            for nombre in materia["otrasCarreras"]:
                nombreSolo_TodasLasCarreras += f" - {nombre}"
            nombreCarrera_TodasLasCarreras = f"{materia['nombre']}"
            for nombre in materia["otrasCarreras"]:
                nombreCarrera_TodasLasCarreras += f" - {nombre}"
        elif type(materia["otrasCarreras"]) == dict:
            for nombre in materia["otrasCarreras"].values():
                nombreSolo_TodasLasCarreras += f" - {nombre}"
            nombreCarrera_TodasLasCarreras = f"{materia['nombre']} (Computación)"
            for carrera, nombre in materia["otrasCarreras"].items():
                nombreCarrera_TodasLasCarreras += f" - {nombre} ({carrera})"

    carpetaMateria = pathCarpetaMateria(materia)
    exámenesQueHay = set(os.listdir(carpetaMateria)) - {".git", "README.md"}
    hayExámenes = len(exámenesQueHay) > 0

    texto = f"""\
# Exámenes viejos {nombreSolo_TodasLasCarreras} - FaMAF

Exámenes viejos de la materia {nombreCarrera_TodasLasCarreras} de FaMAF.

Cualquier contribución con un examen viejo que no esté es bienvenida, ya sea como pull request, o como mandar el examen por cualquier otro medio.
{"(En esta materia todavía nadie subio ningún examen, pero igual se puede contribuir)" if not hayExámenes else ""}

{f"{materia['extra']}" if "extra" in materia else ""}\
"""
    return texto


def crearArchivo(materia : dict):
    """
    Crea el archivo README.md para la materia
    """
    carpetaMateria = pathCarpetaMateria(materia)
    texto = generarTexto(materia)

    with open(f"{carpetaMateria}{os.sep}README.md", 'r', encoding="UTF-8") as README: # 'r' lo abre para leer
        REDMEtext = README.read()
    
    if texto != REDMEtext:
        with open(f"{carpetaMateria}{os.sep}README.md", 'w', encoding="UTF-8") as README: # 'w' lo abre truncando todo lo que tiene
            print(f"Modificando el README de {materia['nombre']}")
            README.write(texto)


materias = [
    {
        "nombre":"Análisis matemático 1",
        "año":1, "cuatrimestre":1,
        "otrasCarreras":{"Matemática aplicada": "Calculo 1"}
    },
    {
        "nombre":"Introducción a los algoritmos",
        "año":1, "cuatrimestre":1
    },
    {
        "nombre":"Matemática discreta 1",
        "año":1, "cuatrimestre":1,
        "otrasCarreras":None # Matemática aplicada
    },
    {
        "nombre":"Algoritmos y estructuras de datos 1",
        "año":1, "cuatrimestre":2
    },
    {
        "nombre":"Análisis matemático 2",
        "año":1, "cuatrimestre":2,
        "otrasCarreras":{"Matemática aplicada": "Calculo 2"}
    },
    {
        "nombre":"Álgebra",
        "año":1, "cuatrimestre":2,
        "otrasCarreras":["Álgebra 2", "Álgebra lineal"]
    },
    {
        "nombre":"Algoritmos y estructuras de datos 2",
        "año":2, "cuatrimestre":1
    },
    {
        "nombre":"Análisis numérico",
        "año":2, "cuatrimestre":1,
        "otrasCarreras":None # Matemática
    },
    {
        "nombre":"Organización del computador",
        "año":2, "cuatrimestre":1
    },
    {
        "nombre":"Introducción a la lógica y a la computación",
        "año":2, "cuatrimestre":2
    },
    {
        "nombre":"Probabilidad y estadística",
        "año":2, "cuatrimestre":2,
        "otrasCarreras":{"profesorados": "Introducción a la probabilidad y estadística"}
    },
    {
        "nombre":"Sistemas operativos",
        "año":2, "cuatrimestre":2
    },
    {
        "nombre":"Matemática discreta 2",
        "año":3, "cuatrimestre":1
    },
    {
        "nombre":"Paradigmas de la programación",
        "año":3, "cuatrimestre":1,
        "extra":"En esta materia los profes comparten los exámenes, así que son faciles de conseguir, pero igual está este repositorio para que haya uno de cada materia"
    },
    {
        "nombre":"Redes y sistemas distribuídos",
        "año":3, "cuatrimestre":1
    },
    {
        "nombre":"Arquitectura de computadoras",
        "año":3, "cuatrimestre":2
    },
    {
        "nombre":"Bases de datos",
        "año":3, "cuatrimestre":2
    },
    {
        "nombre":"Ingeniería del software 1",
        "año":3, "cuatrimestre":2
    },
    {
        "nombre":"Lenguajes formales y computabilidad",
        "año":4, "cuatrimestre":1
    },
    {
        "nombre":"Modelos y simulación",
        "año":4, "cuatrimestre":1
    },
    {
        "nombre":"Física",
        "año":4, "cuatrimestre":2
    },
    {
        "nombre":"Lógica",
        "año":4, "cuatrimestre":2
    },
    {
        "nombre":"Ingeniería del software 2",
        "año":5, "cuatrimestre":1
    },
    {
        "nombre":"Lenguajes y compiladores",
        "año":5, "cuatrimestre":1
    }
]


def crearArchivos():
    for materia in materias:
        crearArchivo(materia)

def main():
    crearArchivos()

if __name__ == "__main__":
    main()
