def contador_frecuencia_palabras(texto):
    """
    Esta funcion recibe un texto (String) y devuelve un diccionario
    con la frecuencia de cada palabra , convierte el texto a minúsculas
    Args:
        texto (str): El texto del cual se desea contar la frecuencia de palabras.
    Returns:
        dict: Un diccionario donde las claves son las palabras y los valores son sus frecuencias.
    """
    palabras = texto.lower().split()
    frecuencia = {}

    for palabra in palabras:
            frecuencia[palabra] = frecuencia.get(palabra, 0) + 1
    return frecuencia

texto = input("Ingrese el texto para contar la frecuencia de palabras: ")
resultado = contador_frecuencia_palabras(texto)
print("Frecuencia de palabras:")
for palabra, cuenta in resultado.items():
    print(f"{palabra}: {cuenta}")

