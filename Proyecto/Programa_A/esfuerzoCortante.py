import math 

class Padre(object):

    def __init__(self, base,altura,distanciaR,espesor, fuerza):
        self.b = base/1000
        self.h = altura/1000
        self.r = distanciaR/1000
        self.esp = espesor/1000
        self.round_perimetro = 0.0
        self.round_area = 0.0
        self.f = fuerza*1000
        self.round_sigma = 0.0

    """
    def conversion_datosAmetros(self):
        self.b = self.b/1000
        self.h = self.h/1000
        self.r = self.r/1000
        self.f = self.f*1000
        self.esp = self.esp/1000
    """

    def perimetroFigura(self):
        print("calculando perimetro")
        
        perim_circulo = math.pi*(self.h) #Pi*Diametro 
        round_perim_circulo = round(perim_circulo,4) #4 decimales redondeado
        print(round_perim_circulo)
        perimetro  = perim_circulo + 2*self.r
        self.round_perimetro = round(perimetro,4) #4 decimales redondeado
        return self.round_perimetro 
    
    def areaDeEsfuerzo(self):
        print("calculando ara esfuerzo")
        self.perimetroFigura()
        print(self.round_perimetro, self.esp)
        area = self.round_perimetro*self.esp
        self.round_area = round(area,7) #4 decimales redondeado
        return self.round_area

    def calcularEsfuerzoCortante(self):
        print('Calculando sigma...')
        
        area = self.areaDeEsfuerzo()
        sigma = self.f/area
        self.round_sigma = round(sigma,2)
        print(self.f,self.round_area)
        print(self.round_sigma)
        return self.round_sigma #VALOR DEL ESFUERZO CORTANTE
"""        
class Hijo(Padre):

    def __init__(self, base,altura,distanciaR,espesor, fuerza):
        super().__init__(base,altura,distanciaR,espesor)
        self.f = fuerza*1000 #Son kilo newtons
        self.sigma = 0.0

    def calcularEsfuerzoCortante(self):
        print('Calculando sigma...')
        
        area = self.areaDeEsfuerzo()
        self.sigma = self.f/area
        print(self.f,area)
        print(self.sigma)
        return self.sigma #VALOR DEL ESFUERZO CORTANTE"""
        


    