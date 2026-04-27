"""
class PadreC(object):
    def __init__(self, y2,y1,y0):
        self.a = y2
        self.b = y1
        self.c = y0
        self.m1 = 0
        self.m2 = 0
        self.radicando = 0

    def formulaGeneral(self):
        self.radicando = self.b**2-4*self.a*self.c
        self.m1 = (-self.b+(self.radicando**0.5))/(2*self.a)
        self.m2 = (-self.b-(self.radicando**0.5))/(2*self.a)
    
    def caso(self):
        if self.radicando > 0:
            return("y(x) = c1 e**",self.m1,"x +c2 e**",self.m2,"x")
            
        elif self.radicando < 0:
            return ("y(x) = c1 e**",self.m1,"x +c2 Xe**",self.m2,"x") 
        
        else:
            return 
"""
import math

class PadreC(object):
    def __init__(self, y2,y1,y0):
        self.a = y2
        self.b = y1
        self.c = y0
        self.m1 = 0
        self.m2 = 0
        self.radicando = 0

    def formulaGeneral(self):
        self.radicando = (self.b**2)-(4*self.a*self.c)
        
        if self.radicando >= 0:
            self.m1 = (-self.b + math.sqrt(self.radicando)) / (2*self.a)
            self.m2 = (-self.b - math.sqrt(self.radicando)) / (2*self.a)

    def caso(self):
        self.formulaGeneral()

        if self.radicando > 0:
            return f"y(x) = C1 e^({self.m1}x) + C2 e^({self.m2}x)"

        elif self.radicando == 0:
            return f"y(x) = (C1 + C2 x)e^({self.m1}x)"

        else:
            alfa = -self.b / (2*self.a)
            beta = math.sqrt(-self.radicando) / (2*self.a)
            return f"y(x) = e^({alfa}x)[C1 cos({beta}x) + C2 sin({beta}x)]"