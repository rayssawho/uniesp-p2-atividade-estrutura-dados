import numpy as np

class Lista:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = np.empty(self.capacidade, dtype=int)
    
    def imprimir(self):
        if self.ultima_posicao == -1:
            print('O vetor está vazio')
        else:
            for i in range(self.ultima_posicao + 1):
                print(i, ' - ', self.valores[i])
    
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print('Capacidade máxima atingida')
        else:
            self.ultima_posicao += 1 
            self.valores[self.ultima_posicao] = valor
    
    def pesquisar(self, valor):
        confere = 0
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                print(f"O valor {valor} está na posição de índice {i} da lista")
                return i
            else:
                confere += 1
                if confere >= (self.ultima_posicao + 1):
                    print(f"O valor {valor} não está na lista")
        return -1
    
    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            print(f"Excluíndo o valor {valor}")    
            self.ultima_posicao -= 1
    