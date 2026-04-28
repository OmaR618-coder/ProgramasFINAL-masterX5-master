from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import os
from Proyecto.Programa_B.wronskiano import PadreB

class InterfazB(QDialog): #HEREDAS DE UN DIALOG
    def __init__(self):
        super().__init__()
         
        loadUi("GUI/interfazWronskiano.ui", self)

        self.pushButtonB.clicked.connect(self.calcularB)

    def calcularB(self):
            f1 = float(self.funcion1.text())
            f2 = self.funcion2.text()
            f3 = self.funcion3.text()
            

            modelo = PadreB(f1,f2,f3)
            res = modelo.esCero()
            self.resultadoDet.setText(str(res))
