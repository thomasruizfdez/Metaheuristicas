#!/bin/python
# -*- coding: utf-8 -*-
# Metaheurísticas 20/21
# Author: Tomás Ruiz Fernández

import numpy as np

def GWO(function, dim, n_pob, max_evals, umbral_bajo, umbral_alto, seed, escalado):
    np.random.seed(seed)
    lobos = []

    # Inicializar la población
    for i in range(n_pob):
        lobos.append( np.random.uniform(-100, 100, dim))

    # Inicializamos lobos alfa, beta y delta
    alfa = beta = delta = -1
    coste_alfa = coste_beta = coste_delta = float("inf")

    for i in range(n_pob):
        coste = function(lobos[i], dim)

        if coste < coste_alfa:
            coste_alfa = coste
            alfa = i
        elif coste < coste_beta:
            coste_beta = coste
            beta = i
        elif coste < coste_delta:
            coste_delta = coste
            delta = i

    # Parámetro a (disminuirá para ir haciendo el radio de búsqueda más pequeño)
    a = 2

    # Bucle principal
    # Las evaluaciones son fijas por ende el número de iteraciones tiene que depender del número de la población
    iteraciones = int(max_evals/n_pob)
    it = 0
    while it < iteraciones:

        # Calcular nueva posición de cada lobo (menos alfa, beta y delta)
        for i in range(n_pob):
            if i != alfa and i != beta and i != delta:
                r1 = np.random.random(dim)
                r2 = np.random.random(dim)

                A = 2 * a * r1 - a
                C = 2 * r2

                D1 = abs(C*lobos[alfa] - lobos[i])
                X1 = lobos[alfa] - A * D1



                r1 = np.random.random(dim)
                r2 = np.random.random(dim)

                A = 2 * a * r1 - a
                C = 2 * r2

                D2 = abs(C*lobos[beta] - lobos[i])
                X2 = lobos[beta] - A * D2



                r1 = np.random.random(dim)
                r2 = np.random.random(dim)

                A = 2 * a * r1 - a
                C = 2 * r2

                D3 = abs(C*lobos[delta] - lobos[i])
                X3 = lobos[delta] - A * D3

                lobos[i] = (X1 + X2 + X3) / 3
                lobos[i] = np.clip(lobos[i], umbral_bajo, umbral_alto)

        # Encontrar alfa, beta y delta
        for i in range(n_pob):
            coste = function(lobos[i], dim)

            if coste < coste_alfa:
                coste_alfa = coste
                alfa = i
            elif coste < coste_beta:
                coste_beta = coste
                beta = i
            elif coste < coste_delta:
                coste_delta = coste
                delta = i

        # Actualizamos a
        a = a - (2/(iteraciones*escalado))

        it = it+1
    return lobos[alfa], coste_alfa
