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

def generarInversa2(lambdaExponencial,aleatorio):
    return (-(1/lambdaExponencial)*math.log(1-aleatorio)) 

#1-4. Investigar como generar números aleatorios con distribución normal. Implementarlo.

def generarNormal(media, varianza):
    return (1/(math.sqrt(2*math.pi*varianza)))*math.e**((-(calcularAleatorio()-media)**2)/2*varianza)


#RV

#Funcion graficar. Recibe a = array de datos , ancho = ancho de barras , titulo del grafico, nombre eje x , nombre eje y
    
def graficar(a,rango,ancho,titulo,x,y):
    #Definir los datos
    #tamaño
    plt.figure(figsize=(10,10))
    #rango x e y, tambien ancho de barras.
    plt.bar(range(0,rango),a,width = ancho)
    #Definir título y nombres de ejes (los ponemos por parametro)
    plt.title(titulo)
    plt.ylabel(y)
    plt.xlabel(x)
    #Mostrar figura
    plt.show()

#2-1 Generar tres muestras de números aleatorios Exp(0,5) de tamaño n = 10, n = 30 y n = 200. Para cada una,
# computar la media y varianza muestral. ¿Qué observa?

#2-2 Para las tres muestras anteriores, graficar los histogramas de frecuencias relativas con anchos de banda 0,4, 0,2 y 0,1;
# es decir,un total de 9 histogramas. ¿Qué conclusiones puede obtener?


# Como el punto 2-2 pide repetir lo anterior con distintos anchos de banda, creo una funcion general
def DosUno_Inversa(n,ancho,exp):

    varianza = 0
    media = 0
    muestra1 = []
    #inserto 0,0000 en los 10 lugares del array
    for i in range(n):
        muestra1.append(0.0000)

    #inserto el calculo generar inversa en cada posición y aprovecho para calcular la media (falta dividir por el total despues)
    for i in range(0,n):
        a = calcularAleatorio()
        print ("El aleatorio1 obtenido es:",a)
        ale = float(round(generarInversa2(exp,a), 4))
        muestra1[i] = ale
        media = media + muestra1[i]
        print ("Las muestras1 son:", muestra1[i])

    media = media/n
    #recorro nuevamente para calcular la varianza
    for i in range(0,n):
        varianza = varianza + ((muestra1[i]-media)**2)

    print("La media de la muestra 1 de numeros aleatorios es:", media)
    print("La varianza de la muestra 1 de numeros aleatorios es:", varianza)

    graficar(muestra1,n,ancho,"Exponenciales muestra","Muestras","Valores")


# Función que llama a resolver todo el punto 2-2
def DosUno():

    #genero numero aleatorio con funcion inversa de N 10
    #DosUno_Inversa(10,0.4,0.5)
    #DosUno_Inversa(10,0.2,0.5)
    #DosUno_Inversa(10,0.1,0.5)
   
    #genero lo mismo anterior pero con cambio de N 30 
    DosUno_Inversa(30,0.4,0.5)
    DosUno_Inversa(30,0.2,0.5)
    DosUno_Inversa(30,0.1,0.5)

    #genero lo mismo anterior pero con cambio de N 200
    #DosUno_Inversa(200,0.4,0.5)
    #DosUno_Inversa(200,0.2,0.5)
    #DosUno_Inversa(200,0.1,0.5)

# TEST del punto 2-1
DosUno()

def grafico_test():

    #Definir los datos
    a = [0.2200,0.5500,0.6200,0.4533,0.2123,0.2211,0.6434,0.5442,0.8340,0.8675]
    b = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]

    #Configurar las características del gráfico
    plt.hist(a, b, histtype = 'bar', rwidth = 0.4, color = 'lightgreen')
    #plt.hist(a, b, alpha=1, edgecolor = 'black',  linewidth=1)

    #Definir título y nombres de ejes
    plt.title('Exponenciales')
    plt.ylabel('Función Inversa')
    plt.xlabel('Muestras')
    #Mostrar figura
    plt.show()

#TEST DE GRAFICO
#grafico_test()

def grafico_test2():

    #Definir los datos
    a = [0.2200,0.5500,0.6200,0.4533,0.2123,0.2211,0.6434,0.5442,0.8340,0.8675]
    b = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]


    plt.figure(figsize=(10,5))
    plt.bar(range(0,10),a)
    #Configurar las características del gráfico
    #plt.hist(a, b, histtype = 'bar', rwidth = 0.4, color = 'lightgreen')

    #Definir título y nombres de ejes
    plt.title('Exponenciales')
    plt.ylabel('Función Inversa')
    plt.xlabel('Muestras')
    #Mostrar figura
    plt.show()
    
#grafico_test2()

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
        #print ("muestra",muestra1[i])
        empirica[i] = float(round(muestra1[i]/50, 4))
        #print ("empirica",empirica[i])

# 2-4 A partir de la función de distribución empírica del punto anterior, generar una nueva muestra de números aleatorios utilizando
# el método de simulación de la primera parte. Computar la media y varianza muestral y graficar el histograma

    muestraAleatoria1 = []
    media1 = 0.000
    varianza1 = 0.0000
    aleatorio = 0.0000
    for i in range(50):
        muestraAleatoria1.append(0.0000)
    for i in range(0,50):
        aleatorio = calcularAleatorio()
        muestraAleatoria1[i] = aleatorio
        media1 = media1 + muestraAleatoria1[i]
    media1 = media1/50
    for i in range(0,49):
        varianza1 = varianza1 + ((muestraAleatoria1[i]-media1)**2)

    print("La media de la muestra de numeros aleatorios es:", media1)
    print("La varianza de la muestra de numeros aleatorios es:", varianza1)

    for i in range(50):
         print("La muestraaleatoria1 es:", muestraAleatoria1[i])

    #grafico
    graficar(muestraAleatoria1,50,0.8,"Muestra Aleatoria","Rango","Cantidad Muestras")

#Test del punto 2-4
#print(calcularAleatorio())
#DosTres()    
    
# 2-5 Repetir el experimento de los dos puntos anteriores con dos muestras aleatorias más generadas con los mismos parámetros.
# ¿Qué conclusión saca? 

#entiendo que llamando a l funcion anterior 2 veces mas, ya estaría...
#DosTres() 
#DosTres()

# 3-1 Generar cuatro muestras de números aleatorios de tamaño 100, todas con distribución binomial con p = 0,40 y n = 10, n = 20,
# n = 50 y n = 100 respectivamente. Graficar sus histogramas. ¿Qué observa?

def Tres_Uno():
    
    # Creo las 4 muestras como array
    muestraAleatoria1 = []
    muestraAleatoria2 = []
    muestraAleatoria3 = []
    muestraAleatoria4 = []

    # Les asigno 0.000 en todas las posiciones
    for i in range(100):
        muestraAleatoria1.append(0.0000)
    for i in range(100):
        muestraAleatoria2.append(0.0000)
    for i in range(100):
        muestraAleatoria3.append(0.0000)
    for i in range(100):
        muestraAleatoria4.append(0.0000)

    # Luego asigno la distribucion binomial en todas las posiciones
    for i in range(0,100):
        muestraAleatoria1[i] = float(round(generarBinomial(10,0.4), 4))
    for i in range(0,100):
        muestraAleatoria2[i] = float(round(generarBinomial(20,0.4), 4))
    for i in range(0,100):
        muestraAleatoria3[i] = float(round(generarBinomial(50,0.4), 4))
    for i in range(0,100):
        muestraAleatoria4[i] = float(round(generarBinomial(100,0.4), 4))

    #grafico histogramas
    graficar(muestraAleatoria1,100,0.8,"Muestra Aleatoria Binomial","Rango","Cantidad de muestras")
    graficar(muestraAleatoria2,100,0.8,"Muestra Aleatoria Binomial","Rango","Cantidad de muestras")
    graficar(muestraAleatoria3,100,0.8,"Muestra Aleatoria Binomial","Rango","Cantidad de muestras")
    graficar(muestraAleatoria4,100,0.8,"Muestra Aleatoria Binomial","Rango","Cantidad de muestras")






