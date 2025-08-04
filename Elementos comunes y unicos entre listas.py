def elementos_comunes_y_unicos(lista1, lista2):
    """
    Esta función recibe dos listas y devuelve los elementos
    unicos y los repetidos entre ambas listas.

    Args:
        lista1 (list): Primera lista de elementos.
        lista2 (list): Segunda lista de elementos.

    Returns:
        tuple: Una tupla que contiene tres componentes:
            - Una lista con los elementos comunes entre ambas listas.
            - La primera lista contiene los elementos comunes entre ambas listas.
            - La segunda lista contiene los elementos únicos de ambas listas.
    """
    comun = set(lista1) & set(lista2)
    unicos_1 = set(lista1) - set(lista2)
    unicos_2 = set(lista2) - set(lista1)
    return (comun,unicos_1, unicos_2)

lista1 = [1, 2, 3, 4, 5]
lista2 = [5, 5, 6, 6, 8]

rta = elementos_comunes_y_unicos(lista1, lista2)
print("Elementos comunes: ", rta[0])
print("Elementos unicos en la lista 1: ", rta[1])
print("Elementos unicos en la lista 2: ", rta[2])
