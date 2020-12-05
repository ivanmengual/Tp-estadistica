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
    aleatorio = calcularAleatorio()
    print("Numero aleatorio generado: ", aleatorio)
    if (probabilidad_exito > aleatorio):
        return 1
    else:
        return 0

#1-2. Utilizando la función del punto anterior, implemente otra que genere un número binomial con los parámetros n,p.

## devuelve la cantidad de exitos en n experimentos bernoulli
#p -> probabilidad de exito de un experimento
#n -> cantidad de ensayos bernoulli
def generarBinomial(n, p):
    j = 0
    cant_exitos = 0
    while j < n:
        if(generarBernoulli(p) == 1):
            cant_exitos +=1
        j += 1
    return cant_exitos

#1-3. Utilizando el procedimiento descrito en el capítulo 6 del Dekking (método de la función inversa o de Monte Carlo), implementar
# una función que permita generar un número aleatorio con distribución Exp(λ).

#Realiza el calculo de la funcion inversa con un numero aleatorio
def generarInversa(lambdaExponencial):
    aleatorio = calcularAleatorio()
    print("El numero aleatorio generado es: ", aleatorio)
    #return float(round(((-(math.log(1-aleatorio)))/lambdaExponencial),4))

    return float(round(((-(math.log(aleatorio)))/lambdaExponencial),4))

#1-4. Investigar como generar números aleatorios con distribución normal. Implementarlo.

#def generarNormal2(media, varianza):
#    aleatorio = calcularAleatorio()
#    #print("El numero aleatorio generado es: ", aleatorio)
#    return float(round(((1/(math.sqrt(2*(3.1415)*varianza)))*(2.7182)**((-(aleatorio-media)**2)/2*varianza)),4))

def GenerarNormal(media, varianza):

    u1 = calcularAleatorio()
    u2 = calcularAleatorio()
    #print("El numero aleatorio U1 generado es: ", u1)
    #print("El numero aleatorio U2 generado es: ", u2)

    z = (math.sqrt(-2*(math.pi)*(u1)))*math.cos(math.radians(2*(math.pi)*(u2)))

    return (media + (varianza*z))

def GenerarNormalEjemplo():

    u1 = 0.2841
    u2 = 0.8336
    #print("El numero aleatorio U1 generado es: ", u1)
    #print("El numero aleatorio U2 generado es: ", u2)

    a = ((-2)*(math.log(u1)))
    b = math.cos(math.radians((2)*(math.pi)*(u2)))
    
    print ("resultado a: ", (math.sqrt(a)))
    print ("resultado b: ", (b))
    
    z = ((math.sqrt(a))*(b))
    print ("resultado z: ", z)
    result = float(round((168 + (8*z)),4))
    print ("resultado: ", result)
    

#RV

#Funcion graficar. Recibe a = array de datos , rango = numero de muestas, ancho = ancho de barras , titulo del grafico, nombre eje x , nombre eje y
    
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

def grafico_histograma(muestra,n,ancho,titulo,x,y):

    #Definir los datos
    #a = [0.2200,0.5500,0.6200,0.4533,0.2123,0.2211,0.6434,0.5442,0.8340,0.8675]

    b = []

    for i in range(0,100):
        b.append(0.0000)
    
    for i in range(0,100):

        if n == 10:
            b[i]=i/n
            print ("n = 10: ", b[i])

        if n == 20:
            b[i]=i/(n/4)
            print ("n = 20: ", b[i])
            
        if n == 50:
            b[i]=i/(n/25)
            print ("n = 30: ", b[i])

        if n == 100:
            b[i]=i/(n/100)
            print ("n = 10: ", b[i])

#    b = [0.0,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,
#         1.0,1.1,1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9,
#         2.0,2.1,2.2,2.3,2.4,2.5,2.6,2.7,2.8,2.9,
#         3.0,3.1,3.2,3.3,3.4,3.5,3.6,3.7,3.8,3.9,
#         4.0,4.1,4.2,4.3,4.4,4.5,4.6,4.7,4.8,4.9,
#         5.0,5.1,5.2,5.3,5.4,5.5,5.6,5.7,5.8,5.9,
#         6.0,6.1,6.2,6.3,6.4,6.5,6.6,6.7,6.8,6.9,
#         7.0,7.1,7.2,7.3,7.4,7.5,7.6,7.7,7.8,7.9,
#         8.0,8.1,8.2,8.3,8.4,8.5,8.6,8.7,8.8,8.9,
#         9.0,9.1,9.2,9.3,9.4,9.5,9.6,9.7,9.8,9.9]
         
    
    #Configurar las características del gráfico
    plt.hist(muestra, b, histtype = 'bar', rwidth = ancho, color = 'lightgreen')
    #plt.hist(a, b, alpha=1, edgecolor = 'black',  linewidth=1)

    #Definir título y nombres de ejes
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
# Recibe como parametros n = cantidad de muestas, ancho = ancho de las barras del grafico,
# exp = lamda exponencial de la funcion

def DosUno_Inversa(n,ancho,exp):

    varianza = 0
    media = 0
    muestra = []
    #inserto 0,0000 en los 10 lugares del array
    for i in range(n):
        muestra.append(0.0000)

    #inserto el calculo generar inversa en cada posición y aprovecho para calcular la media 
    for i in range(0,n):
        aleatorio_con_formula_exponencial = generarInversa(exp)
        muestra[i] = aleatorio_con_formula_exponencial
        media = media + muestra[i]
        print ("Las muestras son:", muestra[i])
    media = float(round((media/n),4))

    #recorro nuevamente para calcular la varianza
    for i in range(0,5):
        
        a = (muestra[i]-media)
        
        varianza = varianza + (a**2)

    varianza = float(round((varianza/n),4))

    print("La media de la muestra 1 de numeros aleatorios es:", media)
    print("La varianza de la muestra 1 de numeros aleatorios es:", varianza)

    grafico_histograma(muestra,n,ancho,"Exponenciales muestra","Muestras","Valores")


# 2-3 Generar una muestra de números Bin(n=10, p=0,3) de tamaño de la muestra = 50. Construir la función de
# distribución empírica de dicha muestra.
def generarEmpirica(muestra):
    funcion_acumulada = []
    numero_anterior = 0
    saltos = []
    altura = 1
    total_datos = len(muestra) #5 con el array hardcodeado
    espacios_array = 0
    
    while espacios_array < total_datos:
        funcion_acumulada.append(0.0000)
        saltos.append(0)
        espacios_array += 1#Sale con 6 
        
    for i in range(0,total_datos):
        if i == 0:
            numero_anterior = muestra[i]
            saltos[i] = altura
            funcion_acumulada[i] = (saltos[i])/total_datos
        elif muestra[i] == numero_anterior:
            aux = numero_anterior
            cant_repetidos = 1
            altura += 1
            saltos[i] = altura
            funcion_acumulada[i] = (saltos[i])/total_datos
            while aux == numero_anterior:
                funcion_acumulada[i - cant_repetidos] = (saltos[i])/total_datos    
                cant_repetidos += 1
                aux = muestra[i - cant_repetidos]
        else:
            numero_anterior = muestra[i]
            altura += 1
            saltos[i] = altura
            funcion_acumulada[i] = (saltos[i])/total_datos

    return funcion_acumulada



def DosTres():

    muestra = []
    empirica = generarEmpirica(sorted(muestra))
    variables = sorted(set(muestra))
    #Borra las variables repetidas
    empirica_limpia = sorted(set(empirica))

    for i in range(0, len(muestra)):
        print(muestra[i])

    for i in range(0,len(empirica_limpia)):
       
        print ("Para x > ", variables[i])
        print ("F(x) es: ",empirica_limpia[i])
    

 
# 2-4 A partir de la función de distribución empírica del punto anterior, generar una nueva muestra de números aleatorios utilizando
# el método de simulación de la primera parte. Computar la media y varianza muestral y graficar el histograma

def CalcularMedia(muestra):
    media = 0
    for i in range(0,50):
        muestra.append(generarBinomial(10, 0.3))
        media = media + muestra[i]
    media = media/50

    return media

def CalcularVarianza(muestra):
    media = CalcularMedia(muestra)
    varianza = 0
    for i in range(0,50):        
        a = (muestra[i]-media)        
        varianza = varianza + (a**2)
    varianza = varianza/50

    return varianza

def DosCuatro(muestra):

    media = CalcularMedia(muestra)
    varianza = CalcularVarianza(muestra)

    desviacion_estandar = math.sqrt(varianza)

    print("La media de la muestra 1 de numeros aleatorios es:", float(round(media,2)))
    print("La varianza de la muestra 1 de numeros aleatorios es:", float(round(varianza,2)))
    print("La desviacion estandar de la muestra 1 de numeros aleatorios es:", float(round(desviacion_estandar,2)))
  
    #grafico
    grafico_histograma(muestra,10,0.8,"Muestra binomial","Rango","Cantidad Muestras")


# 3-1 Generar cuatro muestras de números aleatorios de tamaño 100, todas con distribución binomial con p = 0,40 y n = 10, n = 20,
# n = 50 y n = 100 respectivamente. Graficar sus histogramas. ¿Qué observa?

def Tres_Uno(n):


    media = 0
    varianza = 0
    desviacion = 0
    # Creo la muestras como array
    muestraAleatoria1 = []

    # Les asigno 0.000 en todas las posiciones
    for i in range(n):
        muestraAleatoria1.append(0.0000)

    # Luego asigno la distribucion binomial en todas las posiciones
    for i in range(0,n):
        muestraAleatoria1[i] = generarBinomial(n,0.4)
        print ("muestra binomial",muestraAleatoria1[i])
        media = media + muestraAleatoria1[i]

    media = float(round((media/n),4))

    for i in range(0,n):
        
        a = (muestraAleatoria1[i]-media)
        
        varianza = varianza + (a**2)

    varianza = float(round((varianza/n),4))
    desviacion = float(round(math.sqrt(varianza),4))
    
    print("La media de la muestra de numeros aleatorios es:", media)
    print("La desviacion de la muestra de numeros aleatorios es:", desviacion)
    print("La varianza de la muestra de numeros aleatorios es:", varianza)

    #grafico histogramas
    grafico_histograma(muestraAleatoria1,n,0.8,"Muestra Aleatoria Binomial","Rango","Cantidad de muestras")


def Tres_Dos():

    muestraAleatoria1 = []
    for i in range(100):
        muestraAleatoria1.append(0.0000)
    for i in range(0,100):
        muestraAleatoria1[i] = float(round(generarBinomial(200,0.4), 4))
    

    print("La media de la muestra de numeros aleatorios es:", media1)
    print("La varianza de la muestra de numeros aleatorios es:", varianza1)

    graficar(muestraAleatoria1,n,0.8,"Muestra Aleatoria Binomial","Rango","Cantidad de muestras")

#3-3 Para cada una de las muestras anteriores, calcule la media muestral. Justifique lo que observa.

#4-1 Generar dos muestras N(100, 5), una de tamaño n = 10 y otra de tamaño n = 30. Obtener estimaciones puntuales de su media
#y varianza.
    
#4-2 Suponga que ya conoce el dato de que la distribución tiene varianza 5. Obtener intervalos de confianza del 95% y 98% para
#la media de ambas muestras.

#4-3 Repita el punto anterior pero usando la varianza estimada s^2, para la muestra de tamaño adecuado.

#4-4 Probar a nivel 0,99 la hipótesis de que la varianza sea σ^2 > 5. 
# Calcular la probabilidad de cometer error tipo II para la hipótesis alternativa σ^2 = 6.

#4-5 Agrupando los datos en subgrupos de longitud 0,5, probar a nivel 0,99 la hipótesis de que la muestra proviene de una distribución normal.

def Tests():

    #1--------------------------------

    #1-1
    #Testeo generar aleatorio   ---------------------------------------------ok
    #print ("Calculo Aleatorio 1: ",calcularAleatorio())
    #print ("Calculo Aleatorio 2: ",calcularAleatorio())
    #print ("Calculo Aleatorio 3: ",calcularAleatorio())
    #print ("Calculo Aleatorio 4: ",calcularAleatorio())
    #print ("Calculo Aleatorio 5: ",calcularAleatorio())

    #Testeo generar bernoulli   ----------------------------------------------ok
    #habilitar el print de la función para ver el aleatorio generado
    #print("Genero función bernoulli", generarBernoulli(0.3))

    #1-2 ---------------------------------------------------------------------ok
    #Testeo generar binomial    
    #habilitar el print de la función bernoulli para ver el aleatorio generado
    #print("Genero función binomial: ", generarBinomial(2,0.4))

    #1-3  ---------------------------------------------------------------------ok
    #Testeo generar inversa
    #lambdaExp = 0.5
    #print("Genero función exponencial 1", generarInversa(lambdaExp))
    #print("Genero función exponencial 2", generarInversa(lambdaExp))
    #print("Genero función exponencial 3", generarInversa(lambdaExp))
    #print("Genero función exponencial 4", generarInversa(lambdaExp))
    #print("Genero función exponencial 5", generarInversa(lambdaExp))

    #1-4  
    #Testeo generar normal
    #media = 0.4
    #varianza = 0.2
    #print ("Genero distribución Normal", generarNormal(media,varianza))

    
    #2--------------------------------

    

    #2-1 y 2-2     -------------------------------------------------------------ok - falta que los histogramas se muestren los 9 al mismo tiempo
    #genero numero aleatorio con funcion inversa de N 10
    #DosUno_Inversa(10,0.4,0.5)
    #DosUno_Inversa(10,0.2,0.5)
    #DosUno_Inversa(10,0.1,0.5)
   
    #genero lo mismo anterior pero con cambio de N 30 
    #DosUno_Inversa(30,0.4,0.5)
    #DosUno_Inversa(30,0.2,0.5)
    #DosUno_Inversa(30,0.1,0.5)

    #genero con cambio de N 200
    #DosUno_Inversa(200,0.4,0.5)
    #DosUno_Inversa(200,0.2,0.5)
    #DosUno_Inversa(200,0.1,0.5)


    #2-3
    #genero binomial n=10, p=0.3 - con 50 muestras
    DosTres()

    #2-4
    #Test del punto 2-4
    #DosCuatro()    

    #2-5
    #entiendo que llamando a l funcion anterior 2 veces mas, ya estaría...
    #DosTres() 
    #DosTres()


    #3---------------------------------

    #3-1 
    #Con N = 10  ------------ok
    #Tres_Uno(10)

    #Con N = 20  ------------ok
    #Tres_Uno(20)

    #Con N = 50 --------------agrandar eje x porque se va a 20 masomenos
    #Tres_Uno(50)

    #Con N = 100 -------------agrandar eje x tambien
    #Tres_Uno(100)

    #3-2
    #Con 100 muestras (son 100 muestras
    #Tres_Dos()
    #GenerarNormalEjemplo()

    #3-3


    #4---------------------------------

    #4-1

    #4-2

    #4-3

    #4-4

    #4-5

Tests()
