# Tp de estadistica
import random
import math
import matplotlib.pyplot as plt
import numpy as np # Importamos numpy como el alias np

#1-1. Utilizando únicamente la función random de su lenguaje (la función que genera un número aleatorio uniforme entre 0 y 1),
def calcularAleatorio():
    numAleatorio = random.random()
    return float(round(numAleatorio,4))

#implemente una función que genere un número distribuido Bernoulli con probabilidad p.

#Esto genera un experimento de bernouli con probabilidad p.
def generarBernoulli(p):
    probabilidad_exito = p
    if (probabilidad_exito > calcularAleatorio()):
        return 1
    else:
        return 0

#1-2. Utilizando la función del punto anterior, implemente otra que genere un número binomial con los parámetros n,p.

## devuelve la cantidad de exitos en n experimentos bernoulli
#p -> probabilidad de exito de un experimento
#n -> cantidad de experimentos
def generarBinomial(n, p):
    j = 0
    cant_exitos = 0
    while j < n:
        if(generarBernoulli(p) == 1):
            cant_exitos +=1
        j += 1
    return cant_exitos

#RV
#Agrego la formula del binomial por si mas adelante necesitamos implementarla
def binomialFormula(x,n,p):

    factorial= math.factorial(n)/(math.factorial(x)*math.factorial(n-x))
    probabilidad = p**x*(1-p)**(n-x)
    return factorial*probabilidad
    

#1-3. Utilizando el procedimiento descrito en el capítulo 6 del Dekking (método de la función inversa o de Monte Carlo), implementar
# una función que permita generar un número aleatorio con distribución Exp(λ).

#Realiza el calculo de la funcion inversa con un numero aleatorio
def generarInversa(lambdaExponencial):
    return (-(math.log(1-calcularAleatorio())))/lambdaExponencial

#1-4. Investigar como generar números aleatorios con distribución normal. Implementarlo.

def generarNormal(media, varianza):
    return (1/(math.sqrt(2*math.pi*varianza)))*math.e**((-(calcularAleatorio()-media)**2)/2*varianza)


#RV
#2-1 Generar tres muestras de números aleatorios Exp(0,5) de tamaño n = 10, n = 30 y n = 200. Para cada una,
# computar la media y varianza muestral. ¿Qué observa?
#2-1 Para las tres muestras anteriores, graficar los histogramas de frecuencias relativas con anchos de banda 0,4, 0,2 y 0,1;
# es decir,un total de 9 histogramas. ¿Qué conclusiones puede obtener?

def DosUno():

    media1 = 0
    media2 = 0
    media3 = 0
    varianza1 = 0
    varianza2 = 0
    varianza3 = 0
    #muestra1 = [0,0000,0,0000,0,0000,0,0000,0,0000,0,0000,0,0000,0,0000,0,0000,0,0000]
    muestra1 = []
#inserto 0,0000 en los 10 lugares del array
    for i in range(10):
        muestra1.append(0.0000)

#inserto el calculo generar inversa en cada posición y aprovecho para calcular la media (falta dividir por el total despues)
    for i in range(0,9):
        muestra1[i] = float(round(generarInversa(0.5), 4))
        media1 = media1 + muestra1[i]
        print ("Las muestras1 son:", muestra1[i])
    media1 = media1/10
#recorro nuevamente para calcular la varianza
    for i in range(0,9):
        varianza1 = varianza1 + ((muestra1[i]-media1)**2)

    print("La media de la muestra 1 de numeros aleatorios es:", media1)
    print("La varianza de la muestra 1 de numeros aleatorios es:", varianza1)

#genero lo mismo anterior pero con cambio de N 30 
    print("")      
    muestra2 = []
    for i in range(30):
        muestra2.append(0.0000)
    for i in range(0,29):
        muestra2[i] = float(round(generarInversa(0.5), 4))
        media2 = media2 + muestra2[i]
        #print ("Las muestras2 son:", muestra2[i])
    media2 = media2/30
    for i in range(0,29):
        varianza2 = varianza2 + ((muestra2[i]-media2)**2)

    print("La media de la muestra 2 de numeros aleatorios es:", media2)
    print("La varianza de la muestra 2 de numeros aleatorios es:", varianza2)

#genero lo mismo anterior pero con cambio de N 200
    print("")    
    muestra3 = []
    for i in range(200):
        muestra3.append(0.0000)
    for i in range(0,199):
        muestra3[i] = float(round(generarInversa(0.5), 4))
        media3 = media3 + muestra3[i]
        #print ("Las muestras3 son:", muestra3[i])
    media3 = media3/200
    for i in range(0,199):
        varianza3 = varianza3 + ((muestra3[i]-media3)**2)
    
    print("La media de la muestra 3 de numeros aleatorios es:", media3)
    print("La varianza de la muestra 3 de numeros aleatorios es:", varianza3)
        

#GRAFICO SOLAMENTE DEL N = 10
#Definir los datos del eje x
    b = [0,1,2,3,4,5,6,7,8,9,10]

#Configurar las características del gráfico
    plt.subplot(2,2,1)
    plt.hist(muestra1, b, histtype = 'bar', rwidth = 0.4, color = 'lightgreen')

#Definir título y nombres de ejes
    plt.title('Exponenciales Muestra 1')
    plt.ylabel('Dato obtenido')
    plt.xlabel('Muestras')

    plt.subplot(2,2,2)
    plt.hist(muestra1, b, histtype = 'bar', rwidth = 0.2, color = 'lightgreen')

#Definir título y nombres de ejes
    plt.title('Exponenciales Muestra 1')
    plt.ylabel('Dato obtenido')
    plt.xlabel('Muestras')

    plt.subplot(2,2,3)
    plt.hist(muestra1, b, histtype = 'bar', rwidth = 0.1, color = 'lightgreen')
       
#Definir título y nombres de ejes
    plt.title('Exponenciales Muestra 1')
    plt.ylabel('Dato obtenido')
    plt.xlabel('Muestras')
#Mostrar figura
    plt.show()

def grafico_test(a,b,titulo,x,y):

    #Definir los datos
    a = [22,55,62,45,21,22,34,42,42,4,2,102,95,85,55,110,120,70,65,55,111,115,80,75,65,54,44,43,42,48]
    b = [0,1,2,3,4,5,6,7,8,9,10]

    #Configurar las características del gráfico
    plt.hist(a, b, histtype = 'bar', rwidth = 0.8, color = 'lightgreen')

    #Definir título y nombres de ejes
    plt.title('Exponenciales')
    plt.ylabel('Función Inversa')
    plt.xlabel('Muestras')
    #Mostrar figura
    plt.show()

#TEST DE GRAFICO
#DosUno()
#grafico_test()
    
def graficar(a,b,titulo,x,y):
    #Definir los datos
    lista = a[0]
    rango = []
    for i in range(b):
        rango.append(i+1)

    #Configurar las características del gráfico
    plt.hist(lista, rango, histtype = 'bar', rwidth = 0.8, color = 'lightgreen')

    #Definir título y nombres de ejes
    plt.title(titulo)
    plt.ylabel(y)
    plt.xlabel(x)
    #Mostrar figura
    plt.show()


# 2-3 Generar una muestra de números Bin(n=10, p=0,3) de tamaño de la muestra = 50. Construir la función de
# distribución empírica de dicha muestra.

def DosTres():

    muestra1 = []
    empirica = []
    for i in range(50):
        muestra1.append(0.0000)
        empirica.append(0.0000)
    for i in range(0,49):
        #muestra1[i] = float(round(binomialFormula(i,50,0.3), 4))
        muestra1[i] = float(round(generarBinomial(50,0.3), 4))
        print ("muestra",muestra1[i])
        empirica[i] = float(round(muestra1[i]/50, 4))
        print ("empirica",empirica[i])

# 2-4
    muestraAleatoria1 = []
    media1 = 0.000
    varianza1 = 0.0000
    aleatorio = 0.0000
    for i in range(50):
        muestraAleatoria1.append(0.0000)
    for i in range(0,49):
        aleatorio = calcularAleatorio()
        muestraAleatoria1[i] = aleatorio
        media1 = media1 + muestraAleatoria1[i]
    media1 = media1/50
    for i in range(0,49):
        varianza1 = varianza1 + ((muestraAleatoria1[i]-media1)**2)

    print("La media de la muestra de numeros aleatorios es:", media1)
    print("La varianza de la muestra de numeros aleatorios es:", varianza1)

    #grafico
    graficar(muestraAleatoria1,50,"Muestra Aleatoria","Cantidad Muestras","Datos Obtenidos")

print(calcularAleatorio())
DosTres()    
    














