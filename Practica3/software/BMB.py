#!/usr/bin/python
# -*- coding: utf-8 -*-

# Author: Tomás Ruiz Fernández

import BL

def BMB(n, m, D, SEMILLA, iteraciones, evaluaciones):
    resultado = 0

    for i in range(iteraciones):
        nuevo_resultado = BL.BLprimermejor(n, m, D, SEMILLA, evaluaciones)

        if nuevo_resultado > resultado:
            resultado = nuevo_resultado

    return resultado
