class Pilha:
    def __init__(self):
        self.itens = []
        
    def vazia(self):
        return self.itens == []
    
    def colocar(self, item):
        self.itens.append(item)
    
    def tirar(self, item):
        return self.itens.pop(item)
    
    def mostrar(self):
        return self.itens
    
    def inverter(self):
        for i in self.itens[::-1]:
            if i > 0:
                print(i)