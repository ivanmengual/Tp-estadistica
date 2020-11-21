# Tp de estadistica
import random

#1. Utilizando únicamente la función random de su lenguaje (la función que genera un número aleatorio uniforme entre 0 y 1),
def calcularAleatorio():
    numAleatorio = random.random()
    return numAleatorio

#implemente una función que genere un número distribuido Bernoulli con probabilidad p.

#No entiendo
def generarBernoulli(p):
    probabilidad_exito = p
    if (probabilidad_exito < calcularAleatorio()):
        return 1
    else:
        return 0

#2. Utilizando la función del punto anterior, implemente otra que genere un número binomial con los parámetros n,p.

#3. Utilizando el procedimiento descrito en el capítulo 6 del Dekking (método de la función inversa o de Monte Carlo), imple-
#mentar una función que permita generar un número aleatorio con distribución E xp(λ).

#4. Investigar como generar números aleatorios con distribución normal. Implementarlo.