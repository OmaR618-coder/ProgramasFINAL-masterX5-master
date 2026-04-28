from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import os
from Proyecto.Programa_B.wronskiano import PadreB
import sympy as sp

class InterfazB(QDialog): #HEREDAS DE UN DIALOG
    def __init__(self):
        super().__init__()
         
        loadUi("GUI/interfazWronskiano.ui", self)

        self.pushButtonB.clicked.connect(self.calcularB)

    def calcularB(self):
            """
            f1 = float(self.funcion1.text())
            f2 = self.funcion2.text()
            f3 = self.funcion3.text()
            valor = self.valor.text()
            """
            x = sp.symbols('x')
            f1 = sp.sympify(self.funcion1.text())
            f2 = sp.sympify(self.funcion2.text())
            f3 = sp.sympify(self.funcion3.text())
            valor = float(self.valor.text())

            modelo = PadreB(f1,f2,f3,valor)
            modelo.calcularWronskiano()
            modelo.determinante()
            res = modelo.esCero()
            self.resultadoDet.setText(str(res))

            """
            modelo = PadreB(f1,f2,f3,valor)
            res = modelo.esCero()
            self.resultadoDet.setText(str(res))
            """