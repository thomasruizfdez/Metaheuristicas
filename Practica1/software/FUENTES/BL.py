#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import operator

MAX_EVALUACIONES = 100000

# Función que calcula la distancia total acumulada
def sum_distancias(D, sel, n):
    distancia = 0

    for i in range(n):
        if i in sel:
            for j in range(i+1, n):
                if j in sel:
                    distancia += D[i,j]

    return distancia


# Función que calcula la distancia de todos los elementos al resto de los elementos de Sel y la almacena en un diccionario
def calc_contribucion(sel, D):
    contr = dict()

    for x in sel:
        distancia = 0

        for y in sel:
            if y != x:
                distancia += D[x,y] + D[y,x]

        contr[x] = distancia

    return contr


# Función que calcula la distancia de un elemento al conjunto Sel.
def calc_dist_individual(sel, D, viejo, nuevo):
    distancia = 0

    for x in sel:
        if(x != viejo):
            distancia += D[x, nuevo] + D[nuevo, x]  # Al ser D diagonal superior y no saber qué número es más grande sumo los dos ya que en uno estará el 0

    return distancia


# Función que actualiza la contribucion
def actualiza_contribucion(contr_actual, D, viejo, nuevo, dist_nuevo):
    contr_nuevo = dict()
    for x in contr_actual.keys():
        contr_nuevo[x] = contr_actual[x] - (D[x, viejo] + D[viejo, x]) + (D[x, nuevo] + D[nuevo,x])

    contr_nuevo[nuevo] = dist_nuevo

    return contr_nuevo


def BLprimermejor(n, m, D, SEMILLA):

    # Inicialización de parámetros y variables
    sel = set()
    no_sel = set()

    evaluacion = 0
    mejora = True

    # Selección de puntos inicial (aleatoria)
    np.random.seed(SEMILLA)
    aleatorios = np.random.randint(0, n, m)

    for i in range(n):
        if i in aleatorios:
            sel.add(i)
        else:
            no_sel.add(i)

    #Calculo sumatoria de distancias
    distancia = sum_distancias(D, sel, n)

    #Calculo contribuciones individuales (Ordenadas de orden ascendente)
    contribucion = calc_contribucion(sel, D)
    contribucion_ord = sorted(contribucion.items(), key=operator.itemgetter(1))  #Lista ordenada de parejas Punto/contribucion

    # Bucle hasta que no mejore la solución al explorar todo el vecindario o hasta realizar 100000 evalucaiones
    while(mejora and evaluacion < MAX_EVALUACIONES):
        mejora = False
        evaluacion += 1

        # bucle de elementos ordenador por contribucion
        for x in contribucion_ord:

            # bucle por cada vecino intercambiando con el elemento menos contribuyente (hasta que haya mejora)
            for y in no_sel:
                #Calcular nueva distancia
                dist_nuevo = calc_dist_individual(sel, D, x[0], y)
                posible_dist = distancia - x[1] + dist_nuevo

                # Si la distancia calculada es mayor hacemos los cambios correspondientes
                if(posible_dist > distancia):
                    mejora = True
                    sel.discard(x[0])
                    sel.add(y)

                    no_sel.discard(y)
                    no_sel.add(x[0])

                    del contribucion[x[0]]
                    contribucion = actualiza_contribucion(contribucion, D, x[0], y, dist_nuevo)
                    contribucion_ord = sorted(contribucion.items(), key=operator.itemgetter(1)) #Ordenamos el diccionario según las distancias en orden ascendente

                    distancia = posible_dist

                    break

            if(mejora):
                break

    return distancia
