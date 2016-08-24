# -*- coding: utf-8 -*-
import random
perf = [1,1,1,1,1]
n_gen = len(perf)
n_ind = 10
Pcruce = 0.95
Pmutacion = 0.1
total = list()

def individuo():
    return[random.randint(0, 1) for i in range(n_gen)]

def Poblacion():
    return[individuo() for i in range(n_ind)]

def init():
    poblado = Poblacion()
    acom = 0
    suma = 0
    for i in range(0,n_ind):
    	fitness = 300*poblado[i][0] + 270*poblado[i][1] + 100*poblado[i][2] + 320*poblado[i][3] + 250*poblado[i][4]
    	total.append([poblado[i],fitness])
    	suma = float(suma) + fitness    	
    for i in range(0,n_ind):
        total[i].append(float(format(total[i][1]/suma, '.4f')))
        acom = acom + total[i][2]
        total[i].append(format(acom, '.3f'))
        print('Sujeto: {} con puntaje: {}, probabilidad: {} y acomulada {}'.format(total[i][0],total[i][1],total[i][2],total[i][3]))
init()      	
raw_input('\nPresione Enter para salir.')
