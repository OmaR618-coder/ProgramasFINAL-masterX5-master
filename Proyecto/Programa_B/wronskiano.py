import sympy as sp

class PadreB:
    def __init__(self, f1, f2, f3):
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.x = sp.symbols('x')
        self.wronskiano = 0
        self.det = 0

    def calcularWronskiano(self):
        M = sp.Matrix([
            [self.f1, self.f2, self.f3],
            [sp.diff(self.f1, self.x), sp.diff(self.f2, self.x), sp.diff(self.f3, self.x)],
            [sp.diff(self.f1, self.x, 2), sp.diff(self.f2, self.x, 2), sp.diff(self.f3, self.x, 2)]
        ])

        self.wronskiano = M.toList()
        return self.wronskiano

    def determinante(self, matriz):
        #Aplicamos Sarrus con diagonal [0][0]
        sarrus1 = (
        matriz[0][0]*matriz[1][1]*matriz[2][2] +
        matriz[0][1]*matriz[1][2]*matriz[2][0] +
        matriz[0][2]*matriz[1][0]*matriz[2][1] 
        )

        #Aplicamos Sarrus con diagonal [0][2]
        sarrus2 = (
        matriz[0][2]*matriz[1][1]*matriz[2][0] + 
        matriz[0][0]*matriz[1][2]*matriz[2][1] + 
        matriz[0][1]*matriz[1][0]*matriz[2][2]
        )

        self.det = sarrus1 - sarrus2
        return self.det
    
    #ESTA FUNCION VA A CONVERTIR NUESTRO DETERMINANTE EN UN NUMERO EVALUANDO EN X=0
    def evaluarDeterminante(self, valor):
        x = self.x
        detEvaluado = self.det
        return detEvaluado.subs(x, valor)

    def esCero(self, valor):
        detEvaluado = self.evaluarDeterminante(valor)

        if detEvaluado == 0:
            return "El sistema de funciones ES linealmente dependiente"
        else:
            return "El sistema de funciones NO ES linealmente dependiente ES INDIE"
