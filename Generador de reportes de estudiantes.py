def calcular_promedio(calificaciones):
    """
    Calcula el promedio de una lista de calificaciones.

    Args:
        calificaciones (list): Lista de números (floats o ints) representando las calificaciones.

    Returns:
        float: Promedio de las calificaciones. Si la lista está vacía, retorna 0.0.
    """
    if not calificaciones:
        return 0.0
    return sum(calificaciones) / len(calificaciones)


def obtener_estado(promedio):
    """
    Determina el estado académico de un estudiante según su promedio.

    Args:
        promedio (float): Promedio calculado de las calificaciones de un estudiante.

    Returns:
        str: "Aprobado" si el promedio es >= 3.0, "Reprobado" en caso contrario.
    """
    return "Aprobado" if promedio >= 3.0 else "Reprobado"


def generar_reporte(estudiantes):
    """
    Genera e imprime un reporte formateado con los promedios y estados de cada estudiante.

    Args:
        estudiantes (dict): Diccionario con nombres de estudiantes como claves y listas de calificaciones como valores.

    Returns:
        None
    """
    print("\nReporte de Calificaciones:")
    print("_____________________________")

    for nombre, calificaciones in estudiantes.items():
        promedio = calcular_promedio(calificaciones)
        estado = obtener_estado(promedio)
        print(f"- Estudiante: {nombre}, Promedio: {promedio:.1f}, Estado: {estado}")

    print("_______________________________\n")

estudiantes = {
    "Ana": [4.0, 5.0, 4.5],
    "Juan": [2.5, 3.0, 2.9],
    "Lucía": [3.5, 3.8, 4.2],
    "Carlos": [2.0, 2.5],
    "Valentina": []
}

generar_reporte(estudiantes)