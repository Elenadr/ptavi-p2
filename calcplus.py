#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:47:05 2018

@author: elenadr
"""

import sys
import calcoohija


if __name__ == "__main__":
    f = open("fichero", encoding='utf-8', mode="r")
    micalculadorahija = calcoohija.MiCalculadoraHija()
    for line in f:
        lista = line.split(',')
        listafull = list(map(int, lista[1:]))

        if lista[0] == 'suma':
            operando1 = 0
            for operando2 in listafull:
                operando1 = micalculadorahija.plus(operando1, operando2)
        elif lista[0] == 'resta':
            operando1 = listafull[0]
            for operando2 in listafull[1:]:
                operando1 = micalculadorahija.minus(operando1, operando2)
        elif lista[0] == 'multiplica':
            operando1 = listafull[0]
            for operando2 in listafull:
                operando1 = micalculadorahija.mult(operando1, operando2)
        elif lista[0] == 'divide':
            operando1 = listafull[0]
            for operando2 in listafull[1:]:
                operando1 = micalculadorahija.div(operando1, operando2)
        else:
            sys.exit('Operación sólo puede ser sumar o restar.')

        print(operando1)
