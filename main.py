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
    
def estandarizar(muestra,n,media,varianza):
    
    #   Z = (X - mu)/sigma
    
    b = []

    for i in range(0,n):
        b.append(0.0000)

    for i in range(0,n):
        b[i] = ((muestra[i] - media) / (varianza))   

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
    a, p = plot.subplots(1, len(gaps))
    p = [p] if len(gaps) == 1 else p
    for i, gap in enumerate(gaps):
        p[i].hist(sample, \
                arange(min(sample), max(sample) + gap, gap), weights=weights)
    plot.figure(num=1, figsize=(8, 18))
    plot.subplots_adjust(wspace=0.5)
    plot.show()

def DosUno_Inversa(n,ancho,exp):

    muestra = []
    #inserto 0,0000 en los 10 lugares del array
    for i in range(n):
        muestra.append(0.0000)

    #inserto el calculo generar inversa en cada posición y aprovecho para calcular la media 
    for i in range(0,n):
        aleatorio_con_formula_exponencial = generarInversa(exp)
        muestra[i] = aleatorio_con_formula_exponencial
        
        print ("Las muestras son:", muestra[i])
    
    media = CalcularMedia(muestra,n)

    varianza = CalcularVarianza(muestra,n)

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

def Tres_Uno(n):

    # Creo la muestras como array
    muestraAleatoria1 = []

    # Les asigno 0.000 en todas las posiciones
    for i in range(n):
        muestraAleatoria1.append(0.0000)

    # Luego asigno la distribucion binomial en todas las posiciones
    for i in range(0,n):
        muestraAleatoria1[i] = generarBinomial(n,0.4)
        print ("muestra binomial",muestraAleatoria1[i])

    media = CalcularMedia(muestraAleatoria1,n)

    varianza = CalcularVarianza(muestraAleatoria1,n)

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

def Cuatro_Uno():

    muestra10 = []
    #for i in range(10):
    #    muestra10.append(0.0000)
    #for i in range(0,10):
    #    muestra10[i] = float(round(normal_boxmuller(100,math.sqrt(5),10), 4))
    muestra10 = normal_boxmuller(100,math.sqrt(5),10)

    media10 = CalcularMedia(muestra10,10)
    varianza10 = CalcularVarianza(muestra10,10)
    
    print("la media muestral (o ¯ x) es un estimador insesgado de la media n=10:", media10)
    print("la varianza muestral (o s2) es un estimador insesgado de la varianza n=10:", varianza10)

    muestra30 = []
    #for i in range(30):
    #    muestra30.append(0.0000)
    #for i in range(0,30):
    #    muestra30[i] = float(round(normal_boxmuller(100,math.sqrt(5),30), 4))
    muestra30 = normal_boxmuller(100,math.sqrt(5),30)

    media30 = CalcularMedia(muestra30,30)
    varianza30 = CalcularVarianza(muestra30,30)
    
    print("la media muestral (o ¯ x) es un estimador insesgado de la media n=30 :", media30)
    print("la varianza muestral (o s2) es un estimador insesgado de la varianza n=30:", varianza30)

    
    
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
    
    print("la media muestral (o ¯ x) es un estimador insesgado de la media n=10:", media10)
    print("la varianza muestral (o s2) es un estimador insesgado de la varianza n=10:", varianza10)

    media30 = CalcularMedia(muestra30,30)
    varianza30 = CalcularVarianza(muestra30,30)
    
    print("la media muestral (o ¯ x) es un estimador insesgado de la media n=30 :", media30)
    print("la varianza muestral (o s2) es un estimador insesgado de la varianza n=30:", varianza30)

    #resuelto
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
    print("la media muestral (o ¯ x) es un estimador insesgado de la media n=10:", media10)
    print("la varianza muestral (o s2) es un estimador insesgado de la varianza n=30:", varianza10)
    print("la desviacion muestral (o s2) es un estimador insesgado de la varianza n=10:", desviacion10)
    print("")

    media30 = CalcularMedia(muestra30,30)
    varianza30 = CalcularVarianza2(muestra30,30)
    desviacion30 = math.sqrt(CalcularVarianza2(muestra30,30))
    
    print("la media muestral (o ¯ x) es un estimador insesgado de la media n=30 :", media30)
    print("la varianza muestral (o s2) es un estimador insesgado de la varianza n=30:", varianza30)
    print("la desviacion muestral (o s2) es un estimador insesgado de la varianza n=30:", desviacion30)
    
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

    #sumatoria = calcular_sumatoria_al_cuadrado(muestra, x_raya,30)
    #s = sumatoria /(len(muestra)-1)

#calculamos el limite inferior de la varianza con el estimador chi-cuadrado
   
    chi_cuadrado = float(round(chi2.ppf(0.99, len(muestra30)-1),4))
    
    print("CHI_CUADRADO",chi_cuadrado)

    #varianza = (len(muestra10) - 1 * s / chi_cuadrado)
    varianza = (29 * varianza30 / chi_cuadrado)
    print("VARIANZA",varianza)

    if (varianza) =< 5:
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

    #(s)^2 = chi2 * desviación^2 / (n-1)
    varianza_muestral_limite = chi_cuadrado * 5 / (len(muestra30)-1)

    #calculo nuevo chi cuadrado con s^2 = 6  -> Chi2 = (n-1)*(s)^2 / desviación^2
    nuevo_chi_cuadrado = (len(muestra30) - 1) * varianza_muestral_limite / 6


#calculo la probabilidad de que el estadistico de prueba chi-cuadrado sea mayor al nuevo chi-cuadrado
    nuevo = 1-chi2.cdf(nuevo_chi_cuadrado,29)
    print("nuevo chi cuadrado", nuevo)
    
    

    print ("La probabilidad de cometer el error de tipo 2 es",float(round(probabilidad,3)))       
        

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
    print("Esperados: ",esperados)


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
        print("VERDADERO")

def Tests():

    #1

    #1-1
    #Testeo generar aleatorio   
    #print ("Calculo Aleatorio 1: ",calcularAleatorio())
    #print ("Calculo Aleatorio 2: ",calcularAleatorio())
    #print ("Calculo Aleatorio 3: ",calcularAleatorio())
    #print ("Calculo Aleatorio 4: ",calcularAleatorio())
    #print ("Calculo Aleatorio 5: ",calcularAleatorio())

    #Testeo generar bernoulli   
    #habilitar el print de la función para ver el aleatorio generado
    #print("Genero función bernoulli", generarBernoulli(0.3))

    #1-2 
    #Testeo generar binomial    
    #habilitar el print de la función bernoulli para ver el aleatorio generado
    #print("Genero función binomial: ", generarBinomial(2,0.4))

    #1-3  
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

    

    #2-1 y 2-2     
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
    #DosTres()

    #2-4
    #Test del punto 2-4
    #DosCuatro()    

    #2-5
    #entiendo que llamando a l funcion anterior 2 veces mas, ya estaría...
    #DosTres() 
    #DosTres()


    #3---------------------------------

    #3-1 
    #Con N = 10 
    #Tres_Uno(10)

    #Con N = 20  
    #Tres_Uno(20)

    #Con N = 50 
    #Tres_Uno(50)

    #Con N = 100 
    #Tres_Uno(100)

    #3-2
    #Con 100 muestras (son 100 muestras
    #Tres_Dos()
    #GenerarNormalEjemplo()

    #3-3


    #4---------------------------------

    #4-1
    #Cuatro_Uno()

    #4-2
    #Cuatro_Dos()

    #4-3
    #Cuatro_Tres()    

    #4-4
    #Cuatro_Cuatro()

    #4-5
    Cuatro_Cinco()

Tests()
