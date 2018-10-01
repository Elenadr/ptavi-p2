#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 13:59:11 2018

@author: elenadr
"""
import sys
import calcoo


class MiCalculadoraHija(calcoo.Calculadora):
    def mult(self, op1, op2):
        """ Function to sum the operands. Ops have to be ints """
        return op1 * op2

    def div(self, op1, op2):
        """ Function to substract the operands """
        if op2 == 0:
            sys.exit('Division by zero is not allowed')
        else:
            return op1 / op2


if __name__ == "__main__":
    micalculadorahija = MiCalculadoraHija()
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
        cuenta1 = micalculadorahija.plus(operando1, operando2)
        cuenta2 = micalculadorahija.minus(operando1, operando2)
        cuenta3 = micalculadorahija.mult(operando1, operando2)
        cuenta4 = micalculadorahija.div(operando1, operando2)

    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = cuenta1
    elif sys.argv[2] == "resta":
        result = cuenta2
    elif sys.argv[2] == "multiplicacion":
        result = cuenta3
    elif sys.argv[2] == "division":
        result = cuenta4
    else:
        sys.exit('Operación sólo puede ser sumar o restar.')

    print(result)
