#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from time import time

def Greedy(n, m, D):
    sel = set()
    no_sel = set()

    distancia = 0

    # Inicializar el conjunto de no seleccionados
    for i in range(n):
        no_sel.add(i)

    # Escoger elemento más alejado de los demás
    mejor_elem = -1
    mejor_dist = -1

    for x in no_sel:
        dist = sum(D[x, x+1:]) + sum(D[:x, x])

        if dist > mejor_dist:
            mejor_dist = dist
            mejor_elem = x

    sel.add(mejor_elem)
    no_sel.discard(mejor_elem)

    # Iterar completando SEL con los elementos más alejados al grupo
    while(len(sel) < m):
        mejor_elem = -1
        mejor_dist = -1

        for x in no_sel:
            distancia_minima = 10000000
            for y in sel:
                if x < y:
                    if D[x,y] < distancia_minima:
                        distancia_minima = D[x,y]
                else:
                    if D[y,x] < distancia_minima:
                        distancia_minima = D[y,x]

            if distancia_minima > mejor_dist:
                mejor_elem = x
                mejor_dist = distancia_minima

        for x in sel:
            if x < mejor_elem:
                distancia += D[x, mejor_elem]
            else:
                distancia += D[mejor_elem, x]

        sel.add(mejor_elem)
        no_sel.discard(mejor_elem)

    return distancia
