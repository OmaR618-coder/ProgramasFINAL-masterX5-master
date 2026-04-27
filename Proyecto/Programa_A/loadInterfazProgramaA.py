from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.uic import loadUi
import os
from Proyecto.Programa_A.esfuerzoCortante import Hijo

class InterfazA(QDialog): #HEREDAS DE UN DIALOG
    def __init__(self):
        super().__init__()
         
        loadUi("GUI/interfazEsfuerzoCortante.ui", self)

        self.pushButton.clicked.connect(self.calcularA)

    def calcularA(self):
        try:
            base = float(self.base.text())
            fuerza = float(self.fuerza.text())
            altura = float(self.altura.text())
            distanciaR = float(self.distanciaR.text())
            espesor = float(self.espesor.text())

            modelo = Hijo(base,altura,distanciaR,espesor, fuerza)
            modelo.calcularEsfuerzoCortante()
            self.resultadoEsfuerzoCortante.setText(str(self.sigma))

        except:
            QMessageBox.warning(self, "Error", "Entrada inválida")
