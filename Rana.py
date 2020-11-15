from collections import deque
import sys, os
sys.setrecursionlimit(100000)

class nodo_estado:
    def __init__(self, EA, EP, A, n):
        self.valor = EA
        self.padre = EP
        self.accion = A
        self.nivel = n

    def get_estado(self):
        return self.valor
    
    def get_padre(self):
        return self.padre

    def get_accion(self):
        return self.accion

    def get_nivel(self):
        return self.nivel

    def __eq__(self, e):
        return self.valor == e

"""
Estado inicial: 111H222   estado final: 222H111
"""
class ranitas:
    estado_final = [nodo_estado("222H111",None,"Final",None)]
    def __init__(self, EI):
        self.estado_inicial = nodo_estado(EI, None, "Origen", 1)
        self.estado_actual = None
        self.historial = []
        self.cola_estados = deque()

    def add(self, ET):
        self.cola_estados.append(ET)
        self.historial.append(ET)

    def pop(self):
        return self.cola_estados.popleft()

    def esta_en_historial(self, e):
        return e in self.historial

    def es_final(self):
        return self.estado_actual in self.estado_final

    def mostrar_estado_actual(self):
        print("Estado Actual [" + str(self.estado_actual.get_nivel()) + "] es:\n" + self.estado_actual.get_estado())

    def mostrar_estado(self, e):
        print("Estado es:\n" + e.get_estado())

    def buscar_padre(self, e):
        if e.get_padre() == None:
            print("\n" + e.get_accion() + "\n Nivel: 1")
            self.mostrar_estado(e)
        else:
            self.buscar_padre(e.get_padre())
            print("\n" + e.get_accion() + "\n Nivel: " + str(e.get_nivel()))
            self.mostrar_estado(e)

    def mover(self, direccion):
        index = self.estado_actual.get_estado().find("H")
        left1 = self.estado_actual.get_estado()[index-1]
        left2 = self.estado_actual.get_estado()[index-2]
        right1 = self.estado_actual.get_estado()[index+1]
        right2 = self.estado_actual.get_estado()[index+2]

        #Salto 1 hacia la izquierda
        if direccion == "LEFT1":
            if index < 0:
                return "illegal"
            if left1 == "1":
                aux = self.estado_actual.get_estado()[index-1]
            else:
                return "illegal"

        #Salto 1 hacia la derecha
        if direccion == "RIGHT1":
            if index > 6:
                return "illegal"
            if right1=="2":
                aux = self.estado_actual.get_estado()[index+1]
            else:
                return "illegal"

        #Salto 2 hacia la izquierda
        if direccion == "LEFT2":
            if index < 0:
                return "illegal"
            if left2=="1":
                aux = self.estado_actual.get_estado()[index-2]
            else:
                return "illegal"
        
        #Salto 2 hacia la derecha
        if direccion == "RIGHT2":
            if index > 6:
                return "illegal"
            if right2=="2":
                aux = self.estado_actual.get_estado()[index+2]
            else:
                return "illegal"


        
        nuevo_estado = self.estado_actual.get_estado().replace("H","#")
        nuevo_estado = nuevo_estado.replace(aux,"H")
        nuevo_estado = nuevo_estado.replace("#", aux)
        return nuevo_estado

    def algoritmo_anchura(self, EI):
        iteracion = 0
        self.estado_actual = EI
        movimientos = ["LEFT1","RIGHT1","LEFT2","RIGHT2"]

        while(not self.es_final()):
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()

            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual, "Mover a " + movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_en_historial(estado_temporal) and not estado_temporal.get_estado() == "illegal":
                    self.add(estado_temporal) # se incluye en historial y en la cola

            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))

            #Paso a siguiente iteracion
            self.estado_actual = self.pop()
            iteracion += 1


        print("Iteracion: " + str(iteracion) + "\n")
        self.mostrar_estado_actual()
        print("\n\n\nHa llegado a Solucion!!!")
        self.buscar_padre(self.estado_actual)
        print("\nElementos en Historial: " + str(len(self.historial)))
        print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))
        print("\nCantidad de Iteraciones: " + str(iteracion))

    def busqueda(self):
        self.add(self.estado_inicial)

        self.algoritmo_anchura(self.pop())


#MAIN
if __name__ == "__main__":
    puzzle = ranitas("111H222")

    puzzle.busqueda()
