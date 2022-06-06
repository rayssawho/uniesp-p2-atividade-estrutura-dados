class RuaSemSaida:
    def __init__(self):
        self.carros = []
        
    def vazia(self):
        return self.carros == []
    
    def colocar(self, item):
        self.carros.append(item)
    
    def mostrar(self):
        print(self.carros) 
    
    def inverter(self):
        for i in self.carros[::-1]:
            if i > 0:
                print(i)
                
    def tirar(self, escolha2):
        tirarCarros = []
        for j in self.carros[::-1]:
            if j != escolha2:
                tirarCarros.append(j)
            elif j == escolha2:
                break;
        if tirarCarros == []:
            print("Este é o último carro estacionado na rua, não é preciso retirar nenhum outro.")
        else:
            print(f"É preciso retirar os carros {tirarCarros}")
                
            