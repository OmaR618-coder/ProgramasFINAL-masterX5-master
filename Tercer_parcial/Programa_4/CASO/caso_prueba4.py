"""import math 
import numpy as np
from Tercer_parcial.Programa_3.CASO.caso_prueba3 import Programa3

class Programa4():

    def __init__(self, dialog):
        self.x_t=0
        #REGRESION VARIABLES
        self.x = []
        self.y = []
        self.xavg=0
        self.sum_x=0
        self.contadorN=0
        self.yavg=0
        self.sum_y=0
        self.contador2N=0
        self.x2=0
        self.xy=0
        self.y2=0
        #SHOW
        self.B1=0
        self.rxy=0
        self.r2=0
        self.B0=0
        self.yk=0
        self.dialog = dialog
        self.caso=0

        self.xk = 386

        self.n = 10
        #INTEGRACION VARIABLES
        
        self.dof = self.n-2
        self.num_seg = 10
        p = self.calcularP(10)

        parte3 = Programa3(p, self.dof)
        parte3.calcularX()
        self.X = parte3.x

        #p3
        self.rang =0 
        self.upi = 0
        self.lpi = 0
        self.tailArea = 0

    def caso1(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]
        self.caso = 1
    
    def caso2(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]
        self.caso = 2

    def calcularRegresion(self):

        for i in self.x:
            self.xavg += i
            self.contadorN += 1
        self.xavg = self.xavg/self.contadorN

        #SACAMOS YAVG
        for i in self.y:
            self.yavg += i
            self.contador2N += 1
        self.yavg = self.yavg/self.contador2N
        print("yavg = ",self.yavg )

        #SACAMOS SUM_X
        self.sum_x= self.xavg * 10

        #SACAMOS SUM_Y
        self.sum_y = self.yavg *10 

        #sacamos x²
        for i in self.x:
            self.x2 += i**2
        print("x² =", self.x2)
       
        #sacamos xy
        for i in range(len(self.x)):
            self.xy += self.x[i]*self.y[i]
        print("x*y =", self.xy)

        #sacamos y²
        for i in self.y:
            self.y2 += i**2
        print("y² =", self.y2)

        #CALCULAMOS B1
        self.B1 = (self.xy-(self.contadorN*self.xavg*self.yavg))/((self.x2)-(self.contadorN*self.xavg**2))

        #CALCULAMOS Rxy
        numerador = (self.contador2N * self.xy) - (self.sum_x * self.sum_y)
        denominador = ((self.contador2N * self.x2) - (self.sum_x ** 2)) * ((self.contador2N * self.y2) - (self.sum_y ** 2))
        denominador = denominador ** 0.5
        self.rxy = numerador / denominador
        
        #CALCULAMOS R²
        self.r2 = self.rxy*self.rxy

        #CALCULAMOS B0
        self.B0 = self.yavg-self.xavg*self.B1

        #CALCULAMOS YK SABIENDO QUE XK ES 386
        self.yk  =self.B0+self.B1*386

        match self.caso:
            case 1:
                self.dialog.showB0.setText(self.B0) #VALOR TEST 1 B0
                self.dialog.showB1.setText(self.B1) #VALOR TEST 1 B1
                self.dialog.showRxy.setText(self.rxy) #VALOR TEST 1 RXY
                self.dialog.showR2.setText(self.r2)#VALOR TEST 1 R2
                self.dialog.showYk.setText(self.yk) #VALOR TEST 1 YK
                self.dialog.showTailArea(self.tailArea) #VALOR TEST 1 SIGNIFICANCIA
                self.dialog.showRango(self.rang) #VALOR TEST 1 RANGO
                self.dialog.showUPI(self.upi) #VALOR TEST 1 COLA DERECHA
                self.dialog.showLPI(self.lpi) #VALOR TEST 1 COLA IZQUIERDA

            case 2:
                self.dialog.showB0.setText(self.B0) #VALOR TEST 2 B0
                self.dialog.showB1.setText(self.B1) #VALOR TEST 2 B1
                self.dialog.showRxy.setText(self.rxy) #VALOR TEST 2 RXY
                self.dialog.showR2.setText(self.r2)#VALOR TEST 2 R2
                self.dialog.showYk.setText(self.yk) #VALOR TEST 2 YK
                self.dialog.showTailArea(self.tailArea) #VALOR TEST 2 SIGNIFICANCIA
                self.dialog.showRango(self.rang) #VALOR TEST 2 RANGO
                self.dialog.showUPI(self.upi) #VALOR TEST 2 COLA DERECHA
                self.dialog.showLPI(self.lpi) #VALOR TEST 2 COLA IZQUIERDA
    
    
    self.calcular_x_new()
    self.tail_area()
    self.rango()
    self.upi_lpi()

    def calcular_x_new(self):
        self.x_new = (abs(self.rxy)*(self.n-2)**0.5)/(1-self.rxy**2)**0.5
        self.x_new_abs = abs(self.x_new)

    def calcularF(self, x):
        numerador = math.gamma((self.dof + 1) / 2)
        denominador = ((self.dof * math.pi)**0.5) * math.gamma(self.dof / 2)
        numdem = numerador / denominador
        exp = -((self.dof + 1) / 2)
        return numdem * (1 + ((x**2) / self.dof))**exp

    def calcularP(self, num_seg):
        if num_seg % 2 != 0:
            num_seg += 1

        acum = 0
        w = self.x_t / num_seg

        for i in range(1, num_seg):
            if i % 2 == 0:
                acum += 2 * self.calcularF(i * w)
            else:
                acum += 4 * self.calcularF(i * w)

        return (w / 3) * (self.calcularF(0) + acum + self.calcularF(self.x))

    def iterar(self):
        tol = 1e-7
        n = self.num_seg
        p1 = self.calcularP(n)

        while True:
            n *= 2
            p2 = self.calcularP(n)
            error = abs(p2 - p1)

            if error < tol:
                return p2
            else:
                p1 = p2

    def tail_area(self):
        self.x = self.x_new_abs
        self.dof = self.n - 2
        p = self.iterar()

        self.tailArea = 1-2*p
        print(self.tailArea)
        
    def rango(self):
        s = np.sum((self.y-self.B0-self.B1*self.x)**2)
        sigma = (1/8*s)**0.5 #1/8 = 1/n-2
        r = 1+0.1+(self.xk-self.xavg)**2/np.sum((self.x-self.xavg)**2)#0.2 = 1/n osea 1/10
        self.rang = self.X *sigma*(r**0.5) #8 = n-2 y corresponde a dof

    def upi_lpi(self):
        self.upi = self.yk + 0.7*self.rang
        self.lpi = self.yk - 0.7*self.rang"""

import math
from Segundo_parcial.Integracion_Num.integracion import Integracion
from Tercer_parcial.Programa_3.CASO.caso_prueba3 import Programa3

class Programa4():

    def __init__(self, dialog):
        self.dialog = dialog

        # DATOS
        self.x = []
        self.y = []
        self.n = 10
        self.xk = 386

        # RESULTADOS
        self.B0 = 0
        self.B1 = 0
        self.rxy = 0
        self.r2 = 0
        self.yk = 0
        self.tailArea = 0
        self.rang = 0
        self.upi = 0
        self.lpi = 0

        self.dof = self.n - 2

    # ---------------- CASOS ----------------
    def caso1(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [186,699,132,272,291,331,199,1890,788,1601]

    def caso2(self):
        self.x = [130,650,99,150,128,302,95,945,368,961]
        self.y = [15,69.9,6.5,22.4,28.4,65.9,19.4,198.7,38.8,138.2]

    # ---------------- REGRESIÓN ----------------
    def calcularRegresion(self):

        sum_x = sum(self.x)
        sum_y = sum(self.y)
        sum_xy = sum(self.x[i]*self.y[i] for i in range(self.n))
        sum_x2 = sum(xi**2 for xi in self.x)
        sum_y2 = sum(yi**2 for yi in self.y)

        xavg = sum_x / self.n
        yavg = sum_y / self.n

        # B1
        self.B1 = (sum_xy - self.n*xavg*yavg) / (sum_x2 - self.n*xavg**2)

        # B0
        self.B0 = yavg - self.B1*xavg

        # r
        num = self.n*sum_xy - sum_x*sum_y
        den = math.sqrt((self.n*sum_x2 - sum_x**2)*(self.n*sum_y2 - sum_y**2))
        self.rxy = num / den

        self.r2 = self.rxy**2

        # yk
        self.yk = self.B0 + self.B1*self.xk

    # ---------------- SIGNIFICANCIA ----------------
    def calcularSignificancia(self):
        t = abs(self.rxy) * math.sqrt(self.n - 2) / math.sqrt(1 - self.r2)

        integ = Integracion(t, self.dof)
        p = integ.iterar()

        self.tailArea = 1 - 2*p

    # ---------------- RANGO ----------------
    def calcularRango(self):

        # desviación estándar
        s = sum((self.y[i] - (self.B0 + self.B1*self.x[i]))**2 for i in range(self.n))
        sigma = math.sqrt(s / (self.n - 2))

        xavg = sum(self.x)/self.n
        sum_x_diff = sum((xi - xavg)**2 for xi in self.x)

        # obtener t(0.35, dof) usando Programa 3
        p3 = Programa3(0.35, self.dof)
        p3.calcularX()
        t_range = p3.x

        self.rang = t_range * sigma * math.sqrt(
            1 + 1/self.n + ((self.xk - xavg)**2 / sum_x_diff)
        )

    # ---------------- UPI / LPI ----------------
    def calcularIntervalos(self):
        self.upi = self.yk + self.rang
        self.lpi = self.yk - self.rang

    # ---------------- EJECUTAR TODO ----------------
    def ejecutar(self):
        self.calcularRegresion()
        self.calcularSignificancia()
        self.calcularRango()
        self.calcularIntervalos()

        # MOSTRAR EN INTERFAZ
        self.dialog.showB0.setText(str(self.B0))
        self.dialog.showB1.setText(str(self.B1))
        self.dialog.showRxy.setText(str(self.rxy))
        self.dialog.showR2.setText(str(self.r2))
        self.dialog.showYK.setText(str(self.yk))
        self.dialog.showTailArea.setText(str(self.tailArea))
        self.dialog.showRango.setText(str(self.rang))
        self.dialog.showUPI.setText(str(self.upi))
        self.dialog.showLPI.setText(str(self.lpi))