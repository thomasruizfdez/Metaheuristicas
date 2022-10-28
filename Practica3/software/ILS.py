#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Tomás Ruiz Fernández

import BL
import ES
import numpy as np


def mutacion(sel, no_sel, cambios):
    # Escoger los cambios aleatorios
    elegidos_sel = np.random.choice(sel, cambios, replace=False)
    elegidos_no_sel = np.random.choice(no_sel, cambios, replace=False)

    nuevo_sel = sel
    nuevo_no_sel = no_sel

    for elegido in elegidos_sel:
        nuevo_sel.remove(elegido)
        nuevo_no_sel.append(elegido)

    for elegido in elegidos_no_sel:
        nuevo_no_sel.remove(elegido)
        nuevo_sel.append(elegido)

    return nuevo_sel, nuevo_no_sel


def ILS(n, m, D, SEMILLA, iteraciones, evaluaciones):
    # Generación solución inicial (aleatoria)
    sel = list()
    no_sel = list()

    cambios = int(0.1 * m)

    np.random.seed(SEMILLA)

    # Generación solución inicial (aleatoria)
    seleccionados = np.random.randint(0, n, m)

    for i in range(n):
        if i in seleccionados:
            sel.append(i)
        else:
            no_sel.append(i)

    sel, no_sel, coste = BL.BLprimermejor_ini(sel, no_sel, D, evaluaciones)

    for i in range(iteraciones):
        # Mutacion
        nuevo_sel, nuevo_no_sel = mutacion(sel, no_sel, cambios)

        # Refinamos con la búsqueda local
        nuevo_sel, nuevo_no_sel, nuevo_coste = BL.BLprimermejor_ini(nuevo_sel, nuevo_no_sel, D, evaluaciones)

        # Actualizamos el mejor resultado y nos quedamos con el mejor
        if nuevo_coste > coste:
            sel = nuevo_sel
            no_sel = nuevo_no_sel
            coste = nuevo_coste

    return coste




def ILS_ES(n, m, D, SEMILLA, iteraciones, evaluaciones):
    sel = list()
    no_sel = list()

    cambios = int(0.1 * m)

    np.random.seed(SEMILLA)

    # Generación solución inicial (aleatoria)
    seleccionados = np.random.randint(0, n, m)

    for i in range(n):
        if i in seleccionados:
            sel.append(i)
        else:
            no_sel.append(i)

    sel, no_sel, coste = ES.ES_inicializado(sel, no_sel, n, m, D, SEMILLA, evaluaciones)

    for i in range(iteraciones):
        # Mutacion
        nuevo_sel, nuevo_no_sel = mutacion(sel, no_sel, cambios)

        # Refinamos con la búsqueda local
        nuevo_sel, nuevo_no_sel, nuevo_coste = ES.ES_inicializado(nuevo_sel, nuevo_no_sel, n, m, D, SEMILLA, evaluaciones)

        # Actualizamos el mejor resultado y nos quedamos con el mejor
        if nuevo_coste > coste:
            sel = nuevo_sel
            no_sel = nuevo_no_sel
            coste = nuevo_coste

    return coste
