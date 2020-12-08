# Tp de estadistica
import random
import math
import matplotlib.pyplot as plt
import numpy as np # Importamos numpy como el alias np
from scipy.stats import chi2, norm

#1-1. Utilizando únicamente la función random de su lenguaje (la función que genera un número aleatorio uniforme entre 0 y 1),
def calcularAleatorio():
    numAleatorio = random.random()
    return float(round(numAleatorio,4))

#implemente una función que genere un número distribuido Bernoulli con probabilidad p.

#Esto genera un experimento de bernouli con probabilidad p.
def generarBernoulli(p):
    probabilidad_exito = p
    aleatorio = calcularAleatorio()
    #print("Numero aleatorio generado: ", aleatorio)
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
    #print("El numero aleatorio generado es: ", aleatorio)
    #return float(round(((-(math.log(1-aleatorio)))/lambdaExponencial),4))

    return float(round(((-(math.log(aleatorio)))/lambdaExponencial),4))

#1-4. Investigar como generar números aleatorios con distribución normal. Implementarlo.

#def generarNormal2(media, varianza):
#    aleatorio = calcularAleatorio()
#    #print("El numero aleatorio generado es: ", aleatorio)
#    return float(round(((1/(math.sqrt(2*(3.1415)*varianza)))*(2.7182)**((-(aleatorio-media)**2)/2*varianza)),4))

def GenerarNormal(media, varianza,n):

    u1 = calcularAleatorio()
    u2 = calcularAleatorio()
    #print("El numero aleatorio U1 generado es: ", u1)
    #print("El numero aleatorio U2 generado es: ", u2)

    #z = (math.sqrt(-2*(math.pi)*(u1)))*math.cos(math.radians(2*(math.pi)*(u2)))

    a = ((-2)*(math.log(u1)))
    b = math.cos(math.radians((2)*(math.pi)*(u2)))
    c = math.sin(math.radians((2)*(math.pi)*(u2)))


    #revisar si usamos seno o coseno
    
    if n % 2 == 0:
        
        z = ((math.sqrt(a))*(c))
        result = float(round((media + (varianza*z)),4))
        print ("resultado: ", result)
        return (media + (varianza*z))

    z = ((math.sqrt(a))*(b))
    result = float(round((media + (varianza*z)),4))
    print ("resultado: ", result)
    return (media + (varianza*z))

def normal_boxmuller(mu, sigma, size):
    sample=[]
    while size != 0:
        unif1 = random.random()
        unif2 = random.random()
        norm1 = math.sqrt(-2*math.log(unif1))*math.cos(2*math.pi*unif2) * sigma + mu
        norm2 = math.sqrt(-2*math.log(unif1))*math.sin(2*math.pi*unif2) * sigma + mu
        if size % 2 == 0:
            size -= 1
            sample.append(norm2)
        size -= 1
        sample.append(norm1)
    return sample

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
    
def estandarizar(muestra,n,media,desviacion):
    
    #   Z = (X - mu)/sigma
    
    b = []

    for i in range(0,n):
        b.append(0.0000)

    for i in range(0,n):
        b[i] = ((muestra[i] - media) / (desviacion))   

    return b

def CalcularMedia(muestra,n):

    #Media muestral: xn ’ = 1/n * sum_1ton (x_i)

    media = 0
    for i in range(0,n):
        media = media + muestra[i]
    media = media/n

    return float(round(media,4))

def CalcularVarianza(muestra,n):

    #Varianza muestral: s² = 1/(n) * sum_1ton (x_i - x’)²
    
    media = CalcularMedia(muestra,n)
    varianza = 0

    for i in range(0,n):        
        a = (muestra[i]-media)        
        varianza = varianza + (a**2)
        
    varianza = ((1/n)*(varianza))

    return float(round(varianza,4))

def CalcularVarianza2(muestra,n):

    #Varianza muestral: s² = 1/(n - 1) * sum_1ton (x_i - x’)²
    
    media = CalcularMedia(muestra,n)
    varianza = 0
    for i in range(0,n):        
        a = (muestra[i]-media)        
        varianza = varianza + (a**2)
        
    varianza = ((1/(n-1))*(varianza))

    return float(round(varianza,4))


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
            #print ("n = 10: ", b[i])

        if n == 20:
            b[i]=i/(n/4)
            #print ("n = 20: ", b[i])
            
        if n == 50:
            b[i]=i/(n/25)
            #print ("n = 30: ", b[i])

        if n == 100:
            b[i]=i/(n/100)
            #print ("n = 10: ", b[i])

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

def histograma(sample, gaps, relative=False):
    """
    Graficador de histogramas por ancho de bandas

    :param sample: muestra a graficar
    :type sample: List
    :param gaps: listado de anchos de banda para las clases
    :type gaps: List[float]
    :param relative: transforma los pesos en relativos, default to False
    :type relative: bool
    """
    weights = [1/len(sample) for a in sample] if relative else None
    #a, p = plt.subplots()
    a, p = plt.subplots(1, len(gaps))
    p = [p] if len(gaps) == 1 else p
    for i, gap in enumerate(gaps):
        p[i].hist(sample, \
                arange(min(sample), max(sample) + gap, gap), weights=weights)

    plot.figure(num=1, figsize=(8, 18))
    plot.subplots_adjust(wspace=0.5)
    plot.show()

def histograma2(muestra):
    
    fig, axs = plt.subplots(2, 2, sharey=True)

    axs[0][0].hist(muestra1prima, bins=[i for i in np.arange(-5,6,0.5)], weights=np.zeros_like(muestra1prima)+1./len(muestra1prima))
    axs[0][1].hist(muestra2prima, bins=[i for i in np.arange(-5,6,0.5)], weights=np.zeros_like(muestra2prima)+1./len(muestra2prima))
    axs[1][0].hist(muestra3prima, bins=[i for i in np.arange(-5,6,0.5)], weights=np.zeros_like(muestra3prima)+1./len(muestra3prima))
    axs[1][1].hist(muestra4prima, bins=[i for i in np.arange(-5,6,0.5)], weights=np.zeros_like(muestra4prima)+1./len(muestra4prima))

    axs[0][0].set_title("Muestra 1 Normalizada")
    axs[0][1].set_title("Muestra 2 Normalizada")
    axs[1][0].set_title("Muestra 3 Normalizada")
    axs[1][1].set_title("Muestra 4 Normalizada")
    plt.show()

#def DosUno_Inversa(n,ancho,exp):
def DosUno_Inversa(exp):
    
    muestra10 = []
    #inserto 0,0000 en los 10 lugares del array
    for i in range(10):
        muestra10.append(0.0000)
    #inserto el calculo generar inversa en cada posición y aprovecho para calcular la media 
    for i in range(0,10):
        aleatorio_con_formula_exponencial = generarInversa(exp)
        muestra10[i] = aleatorio_con_formula_exponencial
        
    print("")
    print ("Las muestras con 10: ", muestra10)
    print("")
    media10 = CalcularMedia(muestra10,10)

    varianza10 = CalcularVarianza(muestra10,10)

    print("La media de la muestra 10 de numeros aleatorios es:", media10)
    print("La varianza de la muestra 10 de numeros aleatorios es:", varianza10)
    print("")

    muestra30 = []
    #inserto 0,0000 en los 10 lugares del array
    for i in range(30):
        muestra30.append(0.0000)
    #inserto el calculo generar inversa en cada posición y aprovecho para calcular la media 
    for i in range(0,30):
        aleatorio_con_formula_exponencial = generarInversa(exp)
        muestra30[i] = aleatorio_con_formula_exponencial
        
    print("")
    print ("Las muestras con 30: ", muestra30)
    print("")
    media30 = CalcularMedia(muestra30,30)

    varianza30 = CalcularVarianza(muestra30,30)

    print("La media de la muestra 30 de numeros aleatorios es:", media30)
    print("La varianza de la muestra 30 de numeros aleatorios es:", varianza30)
    print("")

    muestra200 = []
    #inserto 0,0000 en los 10 lugares del array
    for i in range(200):
        muestra200.append(0.0000)
    #inserto el calculo generar inversa en cada posición y aprovecho para calcular la media 
    for i in range(0,200):
        aleatorio_con_formula_exponencial = generarInversa(exp)
        muestra200[i] = aleatorio_con_formula_exponencial
        
    print("")
    print ("Las muestras con 200: ", muestra200)
    print("")
    media200 = CalcularMedia(muestra200,200)

    varianza200 = CalcularVarianza(muestra200,200)

    print("La media de la muestra 200 de numeros aleatorios es:", media200)
    print("La varianza de la muestra 200 de numeros aleatorios es:", varianza200)
    print("")


    muestra1 = muestra10
    muestra2 = muestra30
    muestra3 = muestra200

    #Creacion del espacio de graficos y graficos
    fig, axs = plt.subplots(3, 3)

    # La funcion histograma se encarga de realizar la cuenta de frecuencias segun la cantidad de bins que se quieran declarar.
    # Posteriormente para que la cuenta sea relativa se usa el parametro weights el cual asigna a cada columna un peso relativo a 1
    # https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hist.html?highlight=hist#matplotlib.axes.Axes.hist

    axs[0][0].hist(muestra1, bins=[i for i in np.arange(0,10,0.4)], range=(0,10), weights=np.zeros_like(muestra1)+1./len(muestra1))
    axs[1][0].hist(muestra1, bins=[i for i in np.arange(0,10,0.2)], range=(0,10), weights=np.zeros_like(muestra1)+1./len(muestra1))
    axs[2][0].hist(muestra1, bins=[i for i in np.arange(0,10,0.1)], range=(0,10), weights=np.zeros_like(muestra1)+1./len(muestra1))

    axs[0][1].hist(muestra2, bins=[i for i in np.arange(0,10,0.4)], range=(0,10), weights=np.zeros_like(muestra2)+1./len(muestra2))
    axs[1][1].hist(muestra2, bins=[i for i in np.arange(0,10,0.2)], range=(0,10), weights=np.zeros_like(muestra2)+1./len(muestra2))
    axs[2][1].hist(muestra2, bins=[i for i in np.arange(0,10,0.1)], range=(0,10), weights=np.zeros_like(muestra2)+1./len(muestra2))

    axs[0][2].hist(muestra3, bins=[i for i in np.arange(0,15,0.4)], range=(0,10), weights=np.zeros_like(muestra3)+1./len(muestra3))
    axs[1][2].hist(muestra3, bins=[i for i in np.arange(0,15,0.2)], range=(0,10), weights=np.zeros_like(muestra3)+1./len(muestra3))
    axs[2][2].hist(muestra3, bins=[i for i in np.arange(0,15,0.1)], range=(0,10), weights=np.zeros_like(muestra3)+1./len(muestra3))

    plt.show()


# 2-3 Generar una muestra de números Bin(n=10, p=0,3) de tamaño de la muestra = 50. Construir la función de
# distribución empírica de dicha muestra.
def generarEmpirica(muestra):

    print("")
    print("Muestra ordenada : ", muestra)
    print("")
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
    empirica = []

    #Bin(10,0,3) de tamaño n Æ 50.
    
    for i in range(0,50):
        muestra.append(generarBinomial(10, 0.3))

    print("")
    print("la muestra binomial es: ",muestra)
    print("")
    empirica = generarEmpirica(sorted(muestra))
    variables = sorted(set(muestra))

    #Borra las variables repetidas
    empirica_limpia = sorted(set(empirica))

    print("Función de distribución empirica:")
    print("")
    print(empirica_limpia)
    print("")
          
    for i in range(0,len(empirica_limpia)):
       
        print ("Para x > ", variables[i])
        print ("F(x) es: ",empirica_limpia[i])
    
 
# 2-4 A partir de la función de distribución empírica del punto anterior, generar una nueva muestra de números aleatorios utilizando
# el método de simulación de la primera parte. Computar la media y varianza muestral y graficar el histograma

def DosCuatro(muestra):

    media = CalcularMedia(muestra,n)
    varianza = CalcularVarianza(muestra,n)

    desviacion_estandar = math.sqrt(varianza)

    print("La media de la muestra 1 de numeros aleatorios es:", float(round(media,2)))
    print("La varianza de la muestra 1 de numeros aleatorios es:", float(round(varianza,2)))
    print("La desviacion estandar de la muestra 1 de numeros aleatorios es:", float(round(desviacion_estandar,2)))
  
    #grafico
    grafico_histograma(muestra,10,0.8,"Muestra binomial","Rango","Cantidad Muestras")


# 3-1 Generar cuatro muestras de números aleatorios de tamaño 100, todas con distribución binomial con p = 0,40 y n = 10, n = 20,
# n = 50 y n = 100 respectivamente. Graficar sus histogramas. ¿Qué observa?

def Tres_Uno():

    # Creo la muestras como array
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
        muestraAleatoria1[i] = generarBinomial(10,0.4)
    for i in range(0,100):
        muestraAleatoria2[i] = generarBinomial(20,0.4)
    for i in range(0,100):
        muestraAleatoria3[i] = generarBinomial(50,0.4)
    for i in range(0,100):
        muestraAleatoria4[i] = generarBinomial(100,0.4)

    print ("")
    print ("muestra binomial 10",muestraAleatoria1)
    print ("")
    print ("")
    print ("muestra binomial 20",muestraAleatoria2)
    print ("")
    print ("")
    print ("muestra binomial 50",muestraAleatoria3)
    print ("")
    print ("")
    print ("muestra binomial 100",muestraAleatoria4)
    print ("")

    #grafico histogramas
    grafico_histograma(muestraAleatoria1,10,0.8,"Muestra Aleatoria Binomial 10","Rango","Cantidad de muestras")
    grafico_histograma(muestraAleatoria2,20,0.8,"Muestra Aleatoria Binomial 20","Rango","Cantidad de muestras")
    grafico_histograma(muestraAleatoria3,50,0.8,"Muestra Aleatoria Binomial 50","Rango","Cantidad de muestras")
    grafico_histograma(muestraAleatoria4,100,0.8,"Muestra Aleatoria Binomial 100","Rango","Cantidad de muestras")

    #Creacion del espacio de graficos y graficos
    fig, axs = plt.subplots(2, 2)

    # La funcion histograma se encarga de realizar la cuenta de frecuencias segun la cantidad de bins que se quieran declarar.
    # Posteriormente para que la cuenta sea relativa se usa el parametro weights el cual asigna a cada columna un peso relativo a 1
    # https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.hist.html?highlight=hist#matplotlib.axes.Axes.hist
    
    axs[0][0].hist(muestraAleatoria1, bins=[i for i in np.arange(0,10,0.4)], range=(0,10), weights=np.zeros_like(muestraAleatoria1)+1./len(muestraAleatoria1))
    axs[0][1].hist(muestraAleatoria2, bins=[i for i in np.arange(5,15,0.4)], range=(0,20), weights=np.zeros_like(muestraAleatoria2)+1./len(muestraAleatoria2))
    axs[1][0].hist(muestraAleatoria3, bins=[i for i in np.arange(0,40,0.4)], range=(0,50), weights=np.zeros_like(muestraAleatoria3)+1./len(muestraAleatoria3))
    axs[1][1].hist(muestraAleatoria4, bins=[i for i in np.arange(20,60,0.4)], range=(0,100), weights=np.zeros_like(muestraAleatoria4)+1./len(muestraAleatoria4))
    
    plt.show()


def Tres_Dos():

    muestraAleatoria1 = []
    for i in range(100):
        muestraAleatoria1.append(0.0000)
    for i in range(0,100):
        muestraAleatoria1[i] = float(round(generarBinomial(100,0.4), 4))

    print("Muestra Binomial 100: ",muestraAleatoria1)
    print("")
    media1 = CalcularMedia(muestraAleatoria1,100)
    varianza1 = CalcularVarianza(muestraAleatoria1,100)
    desviacion1 = float(round(math.sqrt(varianza1),4))

    
    print("La media de la muestra de numeros aleatorios es:", media1)
    print("La varianza de la muestra de numeros aleatorios es:", varianza1)
    print("La desviación estandar de la muestra de numeros aleatorios es:", desviacion1)

    normalizada = estandarizar(muestraAleatoria1,100,media1,desviacion1)
    print("")
    print("Muestra Normalizada 100: ",normalizada)
    print("")
    
    #Creacion del espacio de graficos y graficos
    fig, axs = plt.subplots(1, 1)
    axs.hist(normalizada, bins=[i for i in np.arange(-4,4,0.2)], weights=np.zeros_like(normalizada)+1./len(normalizada))
    plt.show()

#3-3 Para cada una de las muestras anteriores, calcule la media muestral. Justifique lo que observa.

def Tres_Tres():

    # Creo la muestras como array
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
        muestraAleatoria1[i] = generarBinomial(10,0.4)
    for i in range(0,100):
        muestraAleatoria2[i] = generarBinomial(20,0.4)
    for i in range(0,100):
        muestraAleatoria3[i] = generarBinomial(50,0.4)
    for i in range(0,100):
        muestraAleatoria4[i] = generarBinomial(100,0.4)

    print ("")
    print ("muestra binomial 10",muestraAleatoria1)
    print ("")
    print ("")
    print ("muestra binomial 20",muestraAleatoria2)
    print ("")
    print ("")
    print ("muestra binomial 50",muestraAleatoria3)
    print ("")
    print ("")
    print ("muestra binomial 100",muestraAleatoria4)
    print ("")

    media1 = CalcularMedia(muestraAleatoria1,10)
    varianza1 = CalcularVarianza(muestraAleatoria1,10)
    desviacion1 = float(round(math.sqrt(varianza1),4))
    media2 = CalcularMedia(muestraAleatoria2,20)
    varianza2 = CalcularVarianza(muestraAleatoria2,20)
    desviacion2 = float(round(math.sqrt(varianza2),4))
    media3 = CalcularMedia(muestraAleatoria3,50)
    varianza3 = CalcularVarianza(muestraAleatoria3,50)
    desviacion3 = float(round(math.sqrt(varianza3),4))
    media4 = CalcularMedia(muestraAleatoria4,100)
    varianza4 = CalcularVarianza(muestraAleatoria4,100)
    desviacion4 = float(round(math.sqrt(varianza4),4))
    
    print("La media de la muestra 10 de numeros aleatorios es:", media1)
    print("La desviacion de la muestra 10 de numeros aleatorios es:", desviacion1)
    print("La varianza de la muestra 10 de numeros aleatorios es:", varianza1)
    print("")
    print("La media de la muestra 20de numeros aleatorios es:", media2)
    print("La desviacion de la muestra 20 de numeros aleatorios es:", desviacion2)
    print("La varianza de la muestra 20 de numeros aleatorios es:", varianza2)
    print("")
    print("La media de la muestra 50 de numeros aleatorios es:", media3)
    print("La desviacion de la muestra 50 de numeros aleatorios es:", desviacion3)
    print("La varianza de la muestra 5de numeros aleatorios es:", varianza3)
    print("")
    print("La media de la muestra 100 de numeros aleatorios es:", media4)
    print("La desviacion de la muestra 100 de numeros aleatorios es:", desviacion4)
    print("La varianza de la muestra 100 de numeros aleatorios es:", varianza4)
    print("")

#4-1 Generar dos muestras N(100, 5), una de tamaño n = 10 y otra de tamaño n = 30. Obtener estimaciones puntuales de su media
#y varianza.

def Cuatro_Uno():

    muestra10 = []
    #for i in range(10):
    #    muestra10.append(0.0000)
    #for i in range(0,10):
    #    muestra10[i] = float(round(normal_boxmuller(100,math.sqrt(5),10), 4))
    muestra10 = normal_boxmuller(100,math.sqrt(5),10)

    media10 = CalcularMedia(muestra10,10)
    varianza10 = CalcularVarianza(muestra10,10)

    print("")
    print("Muestra N=10 ",muestra10)
    print("")
    print("la media muestral es un estimador insesgado de la media n=10:", media10)
    print("la varianza muestral es un estimador insesgado de la varianza n=10:", varianza10)

    muestra30 = []
    #for i in range(30):
    #    muestra30.append(0.0000)
    #for i in range(0,30):
    #    muestra30[i] = float(round(normal_boxmuller(100,math.sqrt(5),30), 4))
    muestra30 = normal_boxmuller(100,math.sqrt(5),30)

    print("")
    print("Muestra N=30 ",muestra30)
    print("")
    media30 = CalcularMedia(muestra30,30)
    varianza30 = CalcularVarianza(muestra30,30)
    
    print("la media muestral es un estimador insesgado de la media n=30 :", media30)
    print("la varianza muestral es un estimador insesgado de la varianza n=30:", varianza30)

    
    
#4-2 Suponga que ya conoce el dato de que la distribución tiene varianza 5. Obtener intervalos de confianza del 95% y 98% para
#la media de ambas muestras.

def Cuatro_Dos():   

    #varianza = 5
    #intervalo1 = 0.98
    #intervalo2 = 0.95

    muestra10 = []
    muestra10 = normal_boxmuller(100,math.sqrt(5),10)
    
    muestra30 = []
    muestra30 = normal_boxmuller(100,math.sqrt(5),30)

    media10 = CalcularMedia(muestra10,10)
    varianza10 = CalcularVarianza(muestra10,10)

    print("")
    print("Muestra N=10 ",muestra10)
    print("")
    print("la media muestral es un estimador insesgado de la media n=10:", media10)
    print("la varianza muestral es un estimador insesgado de la varianza n=10:", varianza10)

    media30 = CalcularMedia(muestra30,30)
    varianza30 = CalcularVarianza(muestra30,30)

    print("")
    print("Muestra N=30 ",muestra30)
    print("")
    print("la media muestral es un estimador insesgado de la media n=30 :", media30)
    print("la varianza muestral es un estimador insesgado de la varianza n=30:", varianza30)

    #resuelto
    print("")
    print("Calculo cotas con T de student a 95% -> ((media)+ -(ALPHA POR TABLA = 1.96)*(DESVIACION EST) / RAIZ(N) )")
    print("")
    print("Calculo cotas con T de student a 98% -> ((media)+ -(ALPHA POR TABLA = 2.33)*(DESVIACION EST) / RAIZ(N) )")
    print("")
    cota_inferior = ((media10)-(1.96)*(math.sqrt(5)/math.sqrt(10)))
    cota_superior = ((media10)+(1.96)*(math.sqrt(5)/math.sqrt(10)))
    print("")
    print("95% cota inferior de muestra 10:", cota_inferior)
    print("95% cota superior de muestra 10:", cota_superior)
    print("")
    
    cota_inferior = ((media10)-(2.33)*(math.sqrt(5)/math.sqrt(10)))
    cota_superior = ((media10)+(2.33)*(math.sqrt(5)/math.sqrt(10)))
    print("98% cota inferior de muestra 10:", cota_inferior)
    print("98% cota superior de muestra 10:", cota_superior)
    print("")
    
    cota_inferior = ((media30)-(1.96)*(math.sqrt(5)/math.sqrt(30)))
    cota_superior = ((media30)+(1.96)*(math.sqrt(5)/math.sqrt(30)))
    print("95% cota inferior de muestra 30:", cota_inferior)
    print("95% cota superior de muestra 30:", cota_superior)
    print("")
    
    cota_inferior = ((media30)-(2.33)*(math.sqrt(5)/math.sqrt(30)))
    cota_superior = ((media30)+(2.33)*(math.sqrt(5)/math.sqrt(30)))
    print("98% cota inferior de muestra 30:", cota_inferior)
    print("98% cota superior de muestra 30:", cota_superior)    
    print("")

#4-3 Repita el punto anterior pero usando la varianza estimada s^2, para la muestra de tamaño adecuado.

def Cuatro_Tres():

    muestra10 = []
    muestra10 = normal_boxmuller(100,math.sqrt(5),10)
    
    muestra30 = []
    muestra30 = normal_boxmuller(100,math.sqrt(5),30)

    #cuasi desviacion estandar tipica muestral = Raiz de la varianza2 (n-1)

    media10 = CalcularMedia(muestra10,10)
    varianza10 = CalcularVarianza2(muestra10,10)
    desviacion10 = math.sqrt(CalcularVarianza2(muestra10,10))

    print("")
    print("Muestra N=10 ",muestra10)
    print("")
    print("")
    print("la media muestral es un estimador insesgado de la media n=10:", media10)
    print("la varianza muestral es un estimador insesgado de la varianza n=30:", varianza10)
    print("la desviacion muestral es un estimador insesgado de la varianza n=10:", desviacion10)
    print("")

    media30 = CalcularMedia(muestra30,30)
    varianza30 = CalcularVarianza2(muestra30,30)
    desviacion30 = math.sqrt(CalcularVarianza2(muestra30,30))

    print("")
    print("Muestra N=30 ",muestra30)
    print("")
    print("la media muestral es un estimador insesgado de la media n=30 :", media30)
    print("la varianza muestral es un estimador insesgado de la varianza n=30:", varianza30)
    print("la desviacion muestral es un estimador insesgado de la varianza n=30:", desviacion30)

    #resuelto
    print("")
    print("Calculo cotas con CHI CUADRADO a 95% -> (media)+ -(ALPHA POR TABLA)*(RAIZ(desviacion)/RAIZ(N))")
    print("")
    print("Calculo cotas con CHI CUADRADO a 98% -> (media)+ -(ALPHA POR TABLA)*(RAIZ(desviacion)/RAIZ(N))")
    print("")
    
    cota_inferior = ((media10)-(2.262)*(math.sqrt(desviacion10)/math.sqrt(10)))
    cota_superior = ((media10)+(2.262)*(math.sqrt(desviacion10)/math.sqrt(10)))
    print("")
    print("95% cota inferior de muestra 10:", cota_inferior)
    print("95% cota superior de muestra 10:", cota_superior)
    print("")
    
    cota_inferior = ((media10)-(2.821)*(math.sqrt(desviacion30)/math.sqrt(10)))
    cota_superior = ((media10)+(2.821)*(math.sqrt(desviacion30)/math.sqrt(10)))
    print("98% cota inferior de muestra 10:", cota_inferior)
    print("98% cota superior de muestra 10:", cota_superior)
    print("")
    
    cota_inferior = ((media30)-(2.045)*(math.sqrt(5)/math.sqrt(30)))
    cota_superior = ((media30)+(2.045)*(math.sqrt(5)/math.sqrt(30)))
    print("95% cota inferior de muestra 30:", cota_inferior)
    print("95% cota superior de muestra 30:", cota_superior)
    print("")
    
    cota_inferior = ((media30)-(2.462)*(math.sqrt(5)/math.sqrt(30)))
    cota_superior = ((media30)+(2.462)*(math.sqrt(5)/math.sqrt(30)))
    print("98% cota inferior de muestra 30:", cota_inferior)
    print("98% cota superior de muestra 30:", cota_superior)    
    print("")
    

#4-4 Probar a nivel 0,99 la hipótesis de que la varianza sea σ^2 > 5. 
# Calcular la probabilidad de cometer error tipo II para la hipótesis alternativa σ^2 = 6.

#calulamos el limite inferior de la varianza con el estimador chi-cuadrado
#probar hipotesis

def Cuatro_Cuatro():

    muestra10 = []
    muestra10 = normal_boxmuller(100,math.sqrt(5),10)
    
    muestra30 = []
    muestra30 = normal_boxmuller(100,math.sqrt(5),30)

    media10 = CalcularMedia(muestra10,10)
    media30 = CalcularMedia(muestra30,30)

    varianza10 = CalcularVarianza2(muestra10,10)
    varianza30 = CalcularVarianza2(muestra30,30)

    print("")
    print("Muestra N=10 ",muestra10)
    print("")
    print("")
    print("Muestra N=30 ",muestra30)
    print("")

    #sumatoria = calcular_sumatoria_al_cuadrado(muestra, x_raya,30)
    #s = sumatoria /(len(muestra)-1)

#calculamos el limite inferior de la varianza con el estimador chi-cuadrado
   
    chi_cuadrado = float(round(chi2.ppf(0.99, len(muestra30)-1),4))
    
    print("CHI_CUADRADO",chi_cuadrado)

    #varianza = (len(muestra10) - 1 * s / chi_cuadrado)
    varianza = (29 * varianza30 / chi_cuadrado)
    #varianza = 
    print("VARIANZA",varianza)

    if (varianza) <= 5:
        print ("El valor de la varianza con el estimador es", float(round(varianza,4)))
        print ("")
        print ("Entonces la hipotesis de la varianza mayor a 5 es FALSA") #falsa hipotesis nula

    # a menos que esté mal el ejercicio, esto no se debería ejecutar nunca
    if (varianza) > 5:
        print ("El valor de la varianza con el estimador es", float(round(varianza,4)))
        print ("")
        print ("Entonces la hipotesis de la varianza mayor a 5 es VERDADERA") #verdadera hipotesis nula
           
#calcular la probabilidad de cometer error tipo 2
#calcular varianza muestral limite

    #formula original: Chi2 = (n-1)*(s)^2 / desviación^2
    print("")
    print("formula original: Chi2 = (n-1)*(s)^2 / desviación^2")
    print("")

    #(s)^2 = chi2 * desviación^2 / (n-1)
    varianza_muestral_limite = chi_cuadrado * 5 / (len(muestra30)-1)
    print ("Varianza muestral limite",varianza_muestral_limite)

    #calculo nuevo chi cuadrado con s^2 = 6  -> Chi2 = (n-1)*(s)^2 / desviación^2
    nuevo_chi_cuadrado = (len(muestra30) - 1) * varianza_muestral_limite / 6
    print ("Nuevo chi cuadrado con la varianza muestral limite, dividio desviacion = 6", nuevo_chi_cuadrado)

#calculo la probabilidad de que el estadistico de prueba chi-cuadrado sea mayor al nuevo chi-cuadrado
    nuevo = 1-chi2.cdf(nuevo_chi_cuadrado,29)
    print("nuevo chi cuadrado", nuevo)
    print("FALTA CALCULAR LA PROBAILIDAD DE ERROR TIPO 2")

    #yo busco P(X > 49.588 | v = 6) -> P(((n-1)S)/5 > 49.588)

    #entonces despejas S y te da S=8.55

    #te fijas el chi limite de ese 8.55

    #con la que asumis es la varianza real, 6, -> 29x8.55/6 = 41.325

    #significa que vos queres saber cual es la probabilidad de caer más allá de 49.588 si la varianza real es 6

    #   H0 V > 5, H1 V = 6

    #con esa varianza que me deja parado justo en el punto critico

    #si la varianza real en vez de 5 es 6

    #que chi corresponde? y que proba tengo de pasarla

    #el que chi corresponde es el 41.325

    #y la proba sería el 6.5

    #print ("La probabilidad de cometer el error de tipo 2 es",float(round(probabilidad,3)))       
        

#4-5 Agrupando los datos en subgrupos de longitud 0,5, probar a nivel 0,99 la hipótesis de que la muestra proviene de una distribución normal.
def Cuatro_Cinco():

    muestra30 = []
    muestra30 = normal_boxmuller(100,math.sqrt(5),30)
    print (muestra30)
    print("")

    #Ordena
    empirica_limpia = sorted(set(muestra30))
    print(empirica_limpia)
    print("")

    #Divide en intervalos de 0,5 a partir del primer valor (minimo)
    subgrupos = np.arange(min(muestra30), max(muestra30), 0.5)
    print (subgrupos)
    print("")

    #Es la cantidad de valores que entran en un rango de 0,5
    observados = [len([x for x in muestra30 if x >= l and x < l + 0.5]) for l in subgrupos]
    print("Observados: ",observados)
    print("")

    #Es la cantidad de valores esperados segun una distribución normal. No a partir de la teorica    
    esperados = [round((norm.cdf(x + 0.5, loc=100, scale=math.sqrt(5)) - norm.cdf(x, loc=100, scale=math.sqrt(5))) * 30) for x in subgrupos]
    print("")
    print("Esperados, calculados con distrubución normal: ",esperados)


    #Agrupo las muestras esperadas y observadas con frecuencias mayores o iguales a 5
    obs2 = []
    esp2 = []
    obsacm = 0
    espacm = 0

    for pos in range(len(observados)):
        obsacm += observados[pos]
        espacm += esperados[pos]

        if obsacm >= 5 and espacm >= 5:
            obs2.append(obsacm)
            esp2.append(espacm)
            obsacm = 0
            espacm = 0

    if obsacm or espacm:
        esp2[-1] += espacm
        obs2[-1] += obsacm

    print("")
    print("Frecuencias observadas en intervalos mayores a 5: ",obs2)
    print("Frecuencias esperadas en intervalos mayores a 5: ",esp2)


    #calcula el estimador como la sumatoria de los errores cuadrados relativos
    errores_cuadrados = sum([(obs2[pos] - val)**2/val for pos, val in enumerate(esp2)])

    #for pos, val in enumerate(esp2):
    #    sum([(obs2[pos] - val)**2 / val])
    #errores_cuadrados = sum        

    print("")
    print("Errores cuadrados: ",errores_cuadrados)
    print("")


    print("CHI CUADRADO: ", float(round(chi2.ppf(0.01, len(esp2)-1),3)))
    print("")

    #Si el estimador calculado es menor a chi-cuadrado con nivel 99% de LEN (ESPERADOS) es verdadero
    if (errores_cuadrados > chi2.ppf(0.01, len(esp2) - 1)):
        print("Como el error cuadratico medio es mayor al chi cuadrado con nivel 0.99, concluyo: VERDADERO")
    else:
        print("Como el error cuadratico medio es menor al chi cuadrado con nivel 0.99, concluyo: FALSO")

def Tests():

    #1

    #1-1
    print("Punto 1-1 - Generar aleatorio")
    print("")
    #Testeo generar aleatorio   

    print ("Calculo Aleatorio 1: ",calcularAleatorio())
    print ("Calculo Aleatorio 2: ",calcularAleatorio())
    print ("Calculo Aleatorio 3: ",calcularAleatorio())
    print ("Calculo Aleatorio 4: ",calcularAleatorio())
    print ("Calculo Aleatorio 5: ",calcularAleatorio())
    print("")
    print("Punto 1-1 - Generar bernoulli")
    print("")
    #Testeo generar bernoulli   
    #habilitar el print de la función para ver el aleatorio generado
    print("Genero función bernoulli con p= 0.3")
    print("")
    print(generarBernoulli(0.3))
    print("")
    
    #1-2
    print("")
    print("Punto 1-2 - Generar binomial")
    print("")
    #Testeo generar binomial    
    #habilitar el print de la función bernoulli para ver el aleatorio generado
    print("Genero función binomial: ", generarBinomial(2,0.4))

    #1-3
    print("")
    print("Punto 1-3 - Generar inversa")
    print("")
    #Testeo generar inversa
    #lambdaExp = 0.5
    print("Genero función exponencial 1", generarInversa(0.5))
    print("Genero función exponencial 2", generarInversa(0.5))
    print("Genero función exponencial 3", generarInversa(0.5))
    print("Genero función exponencial 4", generarInversa(0.5))
    print("Genero función exponencial 5", generarInversa(0.5))

    #1-4
    print("")
    print("Punto 1-4 - Generar normal")
    print("")
    #Testeo generar normal
    #media = 0.4
    #varianza = 0.2
    print ("Genero distribución Normal", normal_boxmuller(0.4, 0.2, 10))

    
    #2--------------------------------

    
    #2-1 y 2-2
    print("")
    print("Punto 2-1 y 2-2 - Generar funcion inversa n=10, n=30, n=200 con exp = 0.5")
    print("")
    #genero numero aleatorio con funcion inversa de N 10 con histogramas
    #DosUno_Inversa(0.5)

    #2-3
    print("")
    print("Punto 2-3 - Generar funcion binomial n=50, construyo distribución empírica")
    print("")
    #genero binomial n=10, p=0.3 - con 50 muestras
    #DosTres()

    #2-4
    print("")
    print("Punto 2-4 - A partir de la funcion empirica del punto anterior, generar una nueva muestra de numeros aleatorios, computar media y varianza")
    print("")
    #Test del punto 2-4
    #DosCuatro()    

    #2-5
    print("")
    print("Punto 2-5 - Generar funcion binomial nuevamente con de tamaño 50, repito empirica")
    print("")
    #entiendo que llamando a l funcion anterior 2 veces mas, ya estaría...
    #DosTres() 
    #DosCuatro()


    #3---------------------------------

    #3-1
    print("")
    print("Punto 3-1 - Generar 4 muestras binomial con n=10 , 20 , 50 y 100")
    print("")
    #Con N = 10 , N = 20 , N = 50, N = 100
    Tres_Uno()

    #3-2
    print("")
    print("Punto 3-2 - Generar nuevamente 100, Calcula media y varianza, luego normalizo")
    print("")
    #Con 100 muestras (son 100 muestras)
    Tres_Dos()
    
    #3-3
    print("")
    print("Punto 3-3 - Calcular media muestral de las 4 muestras binomiales con n=10 , 20 , 50 y 100")
    print("")
    #Media Muestral con N = 10, N=20, N=50, N=100 
    Tres_Tres()
    
    #4---------------------------------

    #4-1
    print("")
    print("Punto 4-1 - Genero normales(100,5) con n= 10 y n=30. Obtengo estimaciones puntuales")
    print("")
    Cuatro_Uno()

    #4-2
    print("")
    print("Punto 4-2 - Con varianza 5, obtengo intervalos de confianza con 95% y 98%")
    print("")
    Cuatro_Dos()

    #4-3
    print("")
    print("Punto 4-3 - Con varianza desconocida, obtengo intervalos de confianza con 95% y 98%")
    print("")
    Cuatro_Tres()    

    #4-4
    print("")
    print("Punto 4-4 - Probar con nivel 0,99 hipotesis de varianza > 5 - Luego caluclar error tipo 2, con alternativa varianza = 6")
    print("")
    Cuatro_Cuatro()

    #4-5
    print("")
    print("Punto 4-5 - Subgrupos de longitud 0,5 - pruebo nivel 0,99 de que la muestra es distrubición normal")
    print("")
    Cuatro_Cinco()

Tests()
