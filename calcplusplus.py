#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 16:29:55 2018

@author: elenadr
"""

import sys
import csv
import calcoohija


if __name__ == "__main__":
    with open("fichero", "r") as f:
        csvreader = list(csv.reader(f, delimiter=','))
        micalculadorahija = calcoohija.MiCalculadoraHija()

        for line in csvreader:
            listafull = list(map(int, line[1:]))

            if line[0] == 'suma':
                operando1 = 0
                for operando2 in listafull:
                    operando1 = micalculadorahija.plus(operando1, operando2)
            elif line[0] == 'resta':
                operando1 = listafull[0]
                for operando2 in listafull[1:]:
                    operando1 = micalculadorahija.minus(operando1, operando2)
            elif line[0] == 'multiplica':
                operando1 = listafull[0]
                for operando2 in listafull:
                    operando1 = micalculadorahija.mult(operando1, operando2)
            elif line[0] == 'divide':
                operando1 = listafull[0]
                for operando2 in listafull[1:]:
                    operando1 = micalculadorahija.div(operando1, operando2)
            else:
                sys.exit('Operación sólo puede ser sumar o restar.')

            print(operando1)
