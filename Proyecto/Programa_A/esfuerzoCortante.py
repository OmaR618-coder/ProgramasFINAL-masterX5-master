import math 

class Padre(object):

    def __init__(self, base,altura,distanciaR,espesor):
        self.b = base
        self.h = altura
        self.r = distanciaR
        self.esp = espesor
        self.perimetro = 0
        self.area = 0

    def conversion_datosAmetros(self):
        self.b = self.b/1000
        self.h = self.h/1000
        self.r = self.r/1000
        
    def perimetroFigura(self):
        perim_circulo = math.pi*(self.h) #Pi*Diametro 
        self.perimetro  = perim_circulo + self.b*2
        return self.perimetro 
    
    def areaDeEsfuerzo(self):
        self.area = self.perimetro*self.esp
        return self.area


class Hijo(Padre):

    def __init__(self, base,altura,distanciaR,espesor, fuerza):
        super().__init__(base,altura,distanciaR,espesor)
        self.f = fuerza*1000 #Son kilo newtons
        self.sigma = 0

    def calcularEsfuerzoCortante(self):
        self.sigma = self.f/self.area
        return self.sigma #VALOR DEL ESFUERZO CORTANTE
        


    