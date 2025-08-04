def analisis_de_calificaciones (cal):
    """
    Esta funcion recibe una lista de calificaiones y calcula
    el promedio, la calificaion mas alta y la calificacion mas baja.

    Args:
    cal : lista de notas .

    Returns:
    tuple: Un tuple que contiene el promedio, la calificación más baja y la calificación más alta.
    """
    prom = sum(cal)/ len(cal)
    calfalta = max(cal)
    calfbaja = min(cal)
    return (prom, calfalta, calfbaja)

notas = [1.5, 3.8, 4.0, 2.0, 2.8]

rta = analisis_de_calificaciones(notas)
print(f"El promedio es: {rta[0]} \n la calificación más alta es: {rta[1]} \n la calificación más baja es: {rta[2]}")
