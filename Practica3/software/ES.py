#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Tomás Ruiz Fernández

import numpy as np

def funcion_mdp(sel, D):
    D_aux = D[sel]
    D_aux = D_aux[:, sel]

    coste = D_aux.sum()

    return coste


def funcion_mdp_factorizada(coste, sel, viejo, nuevo, D):

    coste_viejo = D[sel, viejo].sum() + D[viejo, sel].sum()

    coste_nuevo = D[sel, nuevo].sum() + D[nuevo, sel].sum()
    coste_nuevo = coste_nuevo - (D[viejo, nuevo] + D[nuevo, viejo])

    coste_actual = coste - coste_viejo + coste_nuevo

    return coste_actual


def decision(dif_coste, t):
    prob_acep = np.exp(-dif_coste/t)

    u = np.random.uniform()

    resultado = u <= prob_acep

    return resultado


def enfriamiento(t_inicial, t, t_final, max_evaluaciones, max_vecinos):
    M = max_evaluaciones/max_vecinos

    beta = (t_inicial - t_final) / (M * t_inicial * t_final)

    t_siguiente = t / (1 + beta * t)

    return t_siguiente



def ES(n, m, D, SEMILLA, max_evaluaciones):

    # Utilizo listas para hacer más rápida la búsqueda aleatoria
    sel = list()
    no_sel = list()

    mu = fi = 0.3

    np.random.seed(SEMILLA)

    # Generación solución inicial (aleatoria)
    seleccionados = np.random.randint(0, n, m)

    for i in range(n):
        if i in seleccionados:
            sel.append(i)
        else:
            no_sel.append(i)

    # Cálculo coste
    coste = funcion_mdp(sel, D)

    #Inicialización temperatura
    t_inicial = (coste * mu) / (-np.log(fi))
    t = t_inicial
    t_final = 1e-3

    max_vecinos = 10 * m
    max_exitos = int(0.1 * max_vecinos)

    while(t > t_final):
        vecinos = 0
        exitos = 0

        while(vecinos < max_vecinos and exitos < max_exitos):
            # Generación nuevo vecino
            x = np.random.choice(sel)
            y = np.random.choice(no_sel)

            nuevo_coste = funcion_mdp_factorizada(coste, sel, x, y, D)

            dif_coste = coste - nuevo_coste

            vecinos = vecinos + 1

            if(dif_coste < 0 or decision(dif_coste, t)):
                sel.remove(x)
                sel.append(y)

                no_sel.remove(y)
                no_sel.append(x)

                coste = nuevo_coste

                exitos = exitos + 1

        if(exitos == 0):
            break

        t = enfriamiento (t_inicial, t, t_final, max_evaluaciones, max_vecinos)

    return coste



def ES_inicializado(sel, no_sel, n, m, D, SEMILLA, max_evaluaciones):

    mu = fi = 0.3

    np.random.seed(SEMILLA)

    # Cálculo coste
    coste = funcion_mdp(sel, D)

    #Inicialización temperatura
    t_inicial = (coste * mu) / (-np.log(fi))
    t = t_inicial
    t_final = 1e-3

    max_vecinos = 10 * m
    max_exitos = int(0.1 * max_vecinos)

    while(t > t_final):
        vecinos = 0
        exitos = 0

        while(vecinos < max_vecinos and exitos < max_exitos):
            # Generación nuevo vecino
            x = np.random.choice(sel)
            y = np.random.choice(no_sel)

            nuevo_coste = funcion_mdp_factorizada(coste, sel, x, y, D)

            dif_coste = coste - nuevo_coste

            vecinos = vecinos + 1

            if(dif_coste < 0 or decision(dif_coste, t)):
                sel.remove(x)
                sel.append(y)

                no_sel.remove(y)
                no_sel.append(x)

                coste = nuevo_coste

                exitos = exitos + 1

        if(exitos == 0):
            break

        t = enfriamiento (t_inicial, t, t_final, max_evaluaciones, max_vecinos)

    return sel, no_sel, coste
