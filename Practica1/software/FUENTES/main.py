#!/usr/bin/python
# -*- coding: utf-8 -*-

# Práctica 1 MH
# Tomás Ruiz Fernández

import Greedy as gr
import BL as bl
import numpy as np
import sys
from time import time

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

# Ejecutar los algoritmos midiendo el tiempo
tiempo_ini = time()
distancia_greedy = gr.Greedy(n, m, D)
tiempo_greedy = time() - tiempo_ini

tiempo_ini = time()
distancia_bl = bl.BLprimermejor(n, m, D, SEMILLA)
tiempo_bl = time() - tiempo_ini

# Mostrar los resultados
print("Resultados caso %s"%fichero)
print("Distancia Greedy: %f Tiempo Greedy: %0.10f"%(distancia_greedy, tiempo_greedy))
print("Distancia BL: %f Tiempo BL: %0.10f"%(distancia_bl, tiempo_bl))
print("\n")
