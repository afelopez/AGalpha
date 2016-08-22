<<<<<<< HEAD
# -*- coding: utf-8 -*-
import random
modelo = [1,2,3,4,5]                                                # Objetivo
largo = 5                                                           # longitud del material genetico de cada individuo
num = 10                                                            # Cantidad de individuos de cada generación
progenitores = 3                                                    # Individuos para reproduccion > 2
mutacion = 0.2                                                      # Probabilidad de mutación
generaciones = 1000
print '\nModelo: \n' , modelo                              
  
def individuo(min, max):
    return[random.randint(min, max) for i in range(largo)]

def crearPoblacion():
    return[individuo(1,9) for i in range(num)]
  
def calcularFitness(individuo):
    fitness = 0
    for i in range(len(individuo)):
        if individuo[i] == modelo[i]:
            fitness += 1  
    return fitness
  
def seleccion_reproduccion(poblacion):
    puntuados = [(calcularFitness(i), i) for i in poblacion]        # Calcula el fitness de cada individuo, y lo guarda en pares
    puntuados = [i[1] for i in sorted(puntuados)]                   # Ordena los pares de menor a mayor
    poblacion = puntuados
    seleccionados = puntuados[(len(puntuados)-progenitores):]       # Selección de los individuos con mayor fitness
    for i in range(len(poblacion)-progenitores):                    # No se tocan a los mejores fitness                 
        punto = random.randint(1,largo-1)                           # One-Point
        padre = random.sample(seleccionados, 2)                     # Se eligen dos padres al azar
        poblacion[i][:punto] = padre[0][:punto]                     # Se mezcla el material genetico de los padres, reemplazando la poblacion anterior
        poblacion[i][punto:] = padre[1][punto:]
    return poblacion                                               
 
def mutation(poblacion):
    for i in range(len(poblacion)-progenitores):
        if random.random() <= mutacion:                             # Cada individuo de la poblacion menos los padres tienen una probabilidad de mutar
            punto = random.randint(1,largo-1)                       # Se elgie un punto al azar
            nuevo_valor = random.randint(1,9)                       # Se determina un nuevo valor
            while nuevo_valor == poblacion[i][punto]:               # Que no sea el anterior valor
                nuevo_valor = random.randint(1,9)                   # Se insiste
            poblacion[i][punto] = nuevo_valor                       
    return poblacion

poblacion = crearPoblacion()                                        # Se crea poblacion Inicial
print '\nPoblacion inicial:\n', poblacion
for i in range(generaciones):                                       # Se evoluciona la poblacion la cantidad de generaciones deseadas
    poblacion = seleccion_reproduccion(poblacion)                   # Proceso de selección natural
    poblacion = mutation(poblacion) 
print '\nPoblacion final:\n', poblacion                             # Se muestra la poblacion final
input('Presione Enter para salir.')
=======
# -*- coding: utf-8 -*-
import random
modelo = [1,2,3,4,5]                                                # Objetivo
largo = 5                                                           # longitud del material genetico de cada individuo
num = 10                                                            # Cantidad de individuos de cada generación
progenitores = 3                                                    # Individuos para reproduccion > 2
mutacion = 0.2                                                      # Probabilidad de mutación
generaciones = 1000
print '\nModelo: \n' , modelo                              
  
def individuo(min, max):
    return[random.randint(min, max) for i in range(largo)]

def crearPoblacion():
    return[individuo(1,9) for i in range(num)]
  
def calcularFitness(individuo):
    fitness = 0
    for i in range(len(individuo)):
        if individuo[i] == modelo[i]:
            fitness += 1  
    return fitness
  
def seleccion_reproduccion(poblacion):
    puntuados = [(calcularFitness(i), i) for i in poblacion]        # Calcula el fitness de cada individuo, y lo guarda en pares
    puntuados = [i[1] for i in sorted(puntuados)]                   # Ordena los pares de menor a mayor
    poblacion = puntuados
    seleccionados = puntuados[(len(puntuados)-progenitores):]       # Selección de los individuos con mayor fitness
    for i in range(len(poblacion)-progenitores):                    # No se tocan a los mejores fitness                 
        punto = random.randint(1,largo-1)                           # One-Point
        padre = random.sample(seleccionados, 2)                     # Se eligen dos padres al azar
        poblacion[i][:punto] = padre[0][:punto]                     # Se mezcla el material genetico de los padres, reemplazando la poblacion anterior
        poblacion[i][punto:] = padre[1][punto:]
    return poblacion                                               
 
def mutation(poblacion):
    for i in range(len(poblacion)-progenitores):
        if random.random() <= mutacion:                             # Cada individuo de la poblacion menos los padres tienen una probabilidad de mutar
            punto = random.randint(1,largo-1)                       # Se elgie un punto al azar
            nuevo_valor = random.randint(1,9)                       # Se determina un nuevo valor
            while nuevo_valor == poblacion[i][punto]:               # Que no sea el anterior valor
                nuevo_valor = random.randint(1,9)                   # Se insiste
            poblacion[i][punto] = nuevo_valor                       
    return poblacion

poblacion = crearPoblacion()                                        # Se crea poblacion Inicial
print '\nPoblacion inicial:\n', poblacion
for i in range(generaciones):                                       # Se evoluciona la poblacion la cantidad de generaciones deseadas
    poblacion = seleccion_reproduccion(poblacion)                   # Proceso de selección natural
    poblacion = mutation(poblacion) 
print '\nPoblacion final:\n', poblacion                             # Se muestra la poblacion final
input('Presione Enter para salir.')
>>>>>>> 17f006b9d6e4c6d276474b87ab9bf1fefb7be565
