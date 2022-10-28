#!/bin/python
# -*- coding: utf-8 -*-
# Metaheurísticas 20/21
# Author: Tomás Ruiz Fernández

import GWO
import solis
import numpy as np

# Parámetros:
# porcentaje_gwo -> Porcentaje de iteraciones que le corresponde al algoritmo GWO
# porcentaje_soli -> Porcentaje de iteraciones que le corresponde al algoritmo Solis Wets
# escalado -> Multiplicador que hace el decremento de la variable a del algoritmo GWO menor. Tiene que tener un valor menor a 2.

def GWO_Solis(function, dim, n_pob, max_iteraciones, umbral_bajo, umbral_alto, seed, porcentaje_gwo, porcentaje_solis, escalado, delta):

    # Ejecutamos GWO
    iteraciones_gwo = int(max_iteraciones * porcentaje_gwo)
    sol, fitness = GWO.GWO(function, dim, n_pob, iteraciones_gwo, umbral_bajo, umbral_alto, seed, escalado)

    # Ejecutamos Solis Wets
    iteraciones_solis = int(max_iteraciones * porcentaje_solis)
    sol, fitness = solis.soliswets(function, sol, dim, fitness, umbral_bajo, umbral_alto, iteraciones_solis, delta)

    return sol, fitness
