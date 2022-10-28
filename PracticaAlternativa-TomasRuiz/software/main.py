#!/bin/python
# -*- coding: utf-8 -*-
# Metaheurísticas 20/21
# Author: Tomás Ruiz Fernández

import GWO
import GWO_Solis
import cec17
# import numpy

dim = 10
T = 10
seeds = [22, 82, 128, 333, 505, 234, 5345, 4574, 707, 4543]

for funcid in range(1, 31):
    for i in range(T):

        #cec17.init("GWO", funcid, dim)
        cec17.init("GWO_Solis", funcid, dim)
        # cec17.print_output()

        #solucion, resultado = GWO.GWO(cec17.fitness, dim, 500, 10000*dim, -100, 100, seeds[i], 1)
        solucion, resultado = GWO_Solis.GWO_Solis(cec17.fitness, dim, 500, 10000*dim, -100, 100, seeds[i], 0.7, 0.3, 1.6, 10)

        # print("Resultado: ", cec17.error(resultado))
        #print("Solución: ", solucion)
