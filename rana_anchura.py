from collections import deque
import sys, os
import copy
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

class ranitas:
    estado_final = [nodo_estado([2,2,2,0,1,1,1],None,"Final",None)]
    def __init__(self, EI):
        self.estado_inicial = nodo_estado(EI, None, "Origen", 1)
        self.estado_actual = None
        self.historial = ([])
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
        print("Estado Actual:"+ str(self.estado_actual.get_estado()))

    def mostrar_estado(self, e):
        print("Estado es:\n" + str(e.get_estado()))

    def buscar_padre(self, e):
        if e.get_padre() == None:
            print("\n" + e.get_accion() + "\n Nivel: 1")
            self.mostrar_estado(e)
        else:
            self.buscar_padre(e.get_padre())
            print("\n" + e.get_accion() + "\n Nivel: " + str(e.get_nivel()))
            self.mostrar_estado(e)

    def mover(self, direccion):
        index = self.estado_actual.get_estado().index(0)

        if direccion == "L1":
            if index < 1:
                return "illegal"
            else:
               aux = self.estado_actual.get_estado()[index-1]
               pos = index-1
                
        if direccion == "R1":
            if index > 5:
                return "illegal"
            else:
                 aux = self.estado_actual.get_estado()[index+1]
                 pos = index+1

        if direccion == "L2":
            if index < 2:
                return "illegal"
            else:
                 aux = self.estado_actual.get_estado()[index-2]
                 pos = index-2
        if direccion == "R2":
            if index > 4:
                return "illegal"
            else:
                 aux = self.estado_actual.get_estado()[index+2]
                 pos = index+2
        
        nuevo_estado = copy.copy(self.estado_actual.get_estado())
        for i in nuevo_estado:
            nuevo_estado[index] = aux
            nuevo_estado[pos] = 0

        return nuevo_estado



    def algoritmo_anchura(self, EI):
        iteracion = 0
        self.estado_actual = EI
        movimientos = ["L1","R1","L2","R2"]
        while(not self.es_final()):
            print("Iteracion: " + str(iteracion) + "\n")
            self.mostrar_estado_actual()
            for movimiento in movimientos:
                estado_temporal = nodo_estado(self.mover(movimiento), self.estado_actual,movimiento, self.estado_actual.get_nivel() + 1)
                if not self.esta_en_historial(estado_temporal) and not estado_temporal.get_estado() == "illegal":
                    self.add(estado_temporal)

            print("\nElementos en Historial: " + str(len(self.historial)))
            print("\nElementos en Cola Estados: " + str(len(self.cola_estados)))

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

    juego = ranitas([1,1,1,0,2,2,2])
    juego.busqueda()
