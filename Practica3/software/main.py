#!/usr/bin/python
# -*- coding: utf-8 -*-

# Práctica 1 MH
# Tomás Ruiz Fernández

import numpy as np
import sys
from time import time

import ES
import BMB
import ILS

# Captar parámetros (Semilla y caso)
if len(sys.argv) == 3:
    SEMILLA = int(sys.argv[1])
    fichero = sys.argv[2]
else:
    print("Uso: python3 main.py (SEMILLA) (CASO)")
    sys.exit("Parámetros incorrectos")


# Cargar caso
n = -1
m = -1
D = -1

cabecera = True
with open(fichero, 'r') as f:
    for linea in f:
        if cabecera:
            n,m = linea.split(" ")
            n = int(n)
            m = int(m)
            D = np.zeros((n,n))
            cabecera = False
        else:
            x,y,d = linea.split(" ")
            x = int(x)
            y = int(y)
            d = float(d)
            D[x,y] = d


#Ejecutar los algoritmos midiendo el tiempo
tiempo_ini = time()
resultado_ES = ES.ES(n, m, D, SEMILLA, 100000)
tiempo_ES = time() - tiempo_ini


tiempo_ini = time()
resultado_BMB = BMB.BMB(n, m, D, SEMILLA, 10, 10000)
tiempo_BMB = time() - tiempo_ini

tiempo_ini = time()
resultado_ILS = ILS.ILS(n, m, D, SEMILLA, 10, 10000)
tiempo_ILS = time() - tiempo_ini

tiempo_ini = time()
resultado_ILS_ES = ILS.ILS_ES(n, m, D, SEMILLA, 10, 10000)
tiempo_ILS_ES = time() - tiempo_ini


# Mostrar los resultados
print("Resultados caso %s"%fichero)
print("Distancia ES: %f Tiempo ES: %0.10f"%(resultado_ES, tiempo_ES))
print("Distancia BMB: %f Tiempo BMB: %0.10f"%(resultado_BMB, tiempo_BMB))
print("Distancia ILS: %f Tiempo ILS: %0.10f"%(resultado_ILS, tiempo_ILS))
print("Distancia ILS_ES: %f Tiempo ILS_ES: %0.10f"%(resultado_ILS_ES, tiempo_ILS_ES))
print("\n")
