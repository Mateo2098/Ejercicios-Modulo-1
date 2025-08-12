def calculo_imc(peso, est):
    """
    Ejercicio 1 Calculo del IMC
    Este programa calcula el indice de masa corporal (IMC) de una persona
    a partir de su peso en kilogramos y su estatura en metros.

    Args:
        peso (float): Peso de la persona en kilogramos.
        est (float): Estatura de la persona en metros.
    Returns:
        float: El indice de masa corporal (IMC) redondeado a dos decimales.
    """
    return peso/(est**2)
peso = float (input('¿Cual es su peso en kilogramos? '))
est =  float (input('¿Cual es su estatura en metros? '))

rta = calculo_imc(peso, est)
print(f'El IMC es: {round(rta, 2)}')
