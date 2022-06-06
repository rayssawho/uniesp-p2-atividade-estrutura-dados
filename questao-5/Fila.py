import queue

class Fila:
    def __init__(self, capacidade):
        self.avioes = queue.Queue(capacidade)
        self.espera = queue.Queue()
        
    def adicionar(self, aviao):
        if self.avioes.full() == False:
            self.avioes.put(aviao)
        else:
            self.espera.put(aviao)
            print("A pista está cheia, o avião irá para a fila de espera")
    
    def decolar(self):
        if self.avioes.empty():
            print("A pista está vazia!")
        else:
            primeiro = self.avioes.get()
            print(f"O avião {primeiro} decolou!")
            if self.espera.empty():
                print("Nenhum avião na fila de espera! ")
            else:
                proximo = self.espera.get()
                self.avioes.put(proximo)
                
    def mostrarFilaPista(self):
        if self.avioes.empty():
            print("Nenhum avião na pista! ")
        else:
            numero = self.avioes.qsize()
            if numero == 1:
                print(f"{numero} avião na pista para decolar.")
                print(self.avioes.queue[0])
                
            else:
                print(f"{numero} aviões na pista para decolar.")
                for i in range(numero):
                    print(self.avioes.queue[i])
                
    def mostrarFilaEspera(self):
        if self.espera.empty():
            print("Nenhum avião na fila de Espera. ")
        else:
            numeroEspera = self.espera.qsize()
            if numeroEspera == 1:
                print(f"{numeroEspera} avião na fila de espera.")
                print(self.espera.queue[0])
            else:
                print(f"{numeroEspera} aviões na fila de espera")
                for e in range(numeroEspera):
                    print(self.espera.queue[e])
        
    def mostrarMenu(self):
        escolha = int(input("\nTorre de controle - Aeroporto\n\
        Escolha a opção desejada: \n\
        1 - Número de aviões aguardando na fila de decolagem\n\
        2 - Autorizar a decolagem do primeiro avião\n\
        3 - Adicionar avião na fila\n\
        4 - Listar aviões na fila de espera\n\
        5 - Listar características do primeiro avião da fila\n\
        0 - Sair!\n"))
        return escolha
    