# Tp de estadistica
import random

#1. Utilizando únicamente la función random de su lenguaje (la función que genera un número aleatorio uniforme entre 0 y 1),
def calcularAleatorio():
    numAleatorio = random.random()
    return numAleatorio

#implemente una función que genere un número distribuido Bernoulli con probabilidad p.

#Esto genera un experimento de bernouli con probabilidad p.
def generarBernoulli(p):
    probabilidad_exito = p
    if (probabilidad_exito > calcularAleatorio()):
        return 1
    else:
        return 0

#2. Utilizando la función del punto anterior, implemente otra que genere un número binomial con los parámetros n,p.
def generarBinomial(n, p):
    j = 0
    cant_exitos = 0
    while j < n:
        if(generarBernoulli(p) == 1):
            cant_exitos +=1
        j += 1
    return cant_exitos

#p -> probabilidad de exito de un experimento
#n -> cantidad de experimentos
#x -> la probabilidad de que x experimentos sean exitosos


#3. Utilizando el procedimiento descrito en el capítulo 6 del Dekking (método de la función inversa o de Monte Carlo), implementar
# una función que permita generar un número aleatorio con distribución Exp(λ).

#4. Investigar como generar números aleatorios con distribución normal. Implementarlo.