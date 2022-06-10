# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 08:44:10 2022

@author: Alumno
"""

def factorizar(n):
    numeros_primos = iter((2, 3, 5, 7, 11, 13, 17, 19, 23, 29))
    numero_primo_actual = next(numeros_primos)
    resultado = []
    cociente = None
    while cociente != 1:
        if n % numero_primo_actual != 0:
            # No se puede dividir por este número primo,
            # obtener el siguiente y volver a ejecutar
            # el bucle.
            numero_primo_actual = next(numeros_primos)
            continue
        resultado.append(numero_primo_actual)
        n = cociente = n / numero_primo_actual
    return resultado
n = int(input("Ingrese un número mayor a 1: "))
if n > 1:
    factores = factorizar(n)
    print(f"Factor de {n}:", " x ".join(map(str, factores)))
else:
    print("Ingrese un número mayor a 1.")

