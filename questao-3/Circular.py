import numpy as np

class Circular:
    def __init__(self,capacidade):
        self.capacidade = capacidade 
        self.fila = [None for i in range(capacidade)]
        self.inicio = self.final = -1    
    
    def __fila_vazio(self):
        return self.numero_elementos == 0

    def __fila_cheia(self):
        return self.numero_elementos == self.capacidade -1
    
    def enfileirar(self, elemento):
        if ((self.final + 1) % self.capacidade == self.inicio):
            print("\nFila está cheia\n")
             
        elif (self.inicio == -1):
            self.inicio = 0
            self.final = 0
            self.fila[self.final] = elemento
        else:
            self.final = (self.final + 1) % self.capacidade
            self.fila[self.final] = elemento
    
    def desenfileirar(self):
        if (self.inicio == -1):
            print("\nA fila está vazia.\n")
             
        elif (self.inicio == self.final):
            temp = self.fila[self.inicio]
            self.inicio = -1
            self.final = -1
            return temp
        else:
            temp = self.fila[self.inicio]
            self.inicio = (self.inicio + 1) % self.capacidade
            return temp
    
    def primeiro(self):
        if self.__fila_vazio():
            return -1
        return self.valores[self.inicio]
        
    
  

   