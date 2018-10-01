#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:13:37 2018

@author: elenadr
"""

import sys


class Calculadora:
    def plus(self, op1, op2):
        """ Function to sum the operands. Ops have to be ints """
        return op1 + op2

    def minus(self, op1, op2):
        """ Function to substract the operands """
        return op1 - op2


if __name__ == "__main__":
    micalculadora = Calculadora()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        cuenta1 = micalculadora.plus(operando1, operando2)
        cuenta2 = micalculadora.minus(operando1, operando2)
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = cuenta1
    elif sys.argv[2] == "resta":
        result = cuenta2
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
