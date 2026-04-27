from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import os
from Proyecto.Programa_C.ecuacionHomogenea import PadreC


"""
    def calcularA(self):
        try:
            a = float(self.a.text())
            b = float(self.b.text())
            c = float(self.c.text())
            
            modelo = PadreC()
            modelo.caso()
            self.resultadoSolGen.setText(str(modelo))

        except:
            QMessageBox.warning(self, "Error", "Entrada inválida")
"""
class InterfazC(QDialog): #HEREDAS DE UN DIALOG
    def __init__(self):
        super().__init__()
         
        loadUi("GUI/interfazEcuacionHomo.ui", self)

        self.pushButtonC.clicked.connect(self.calcularC)

    def calcularC(self):
        try:
            a = float(self.a.text())
            b = float(self.b.text())
            c = float(self.c.text())
            
            modelo = PadreC(a, b, c)
            resultado = modelo.caso()
            
            self.resultadoSolGen.setText(resultado)

        except:
            QMessageBox.warning(self, "Error", "Entrada inválida")