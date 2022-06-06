import queue

from Aviao import Aviao
from Fila import Fila

if __name__ == "__main__":
    
    fila = Fila(3)
    aviao = Aviao("Boeing 737 ", "Gol ", "5314")
    aviao1 = (aviao.getModelo() + aviao.getCompanhia() + aviao.getNumeroVoo())
    fila.adicionar(aviao1)
    aviao = Aviao("airbus 320 ", "Azul ", "3540")
    aviao1 = (aviao.getModelo() + aviao.getCompanhia() + aviao.getNumeroVoo())
    fila.adicionar(aviao1)
    aviao = Aviao("Boeing 707 ", "Latam ", "6518 ")
    aviao1 = (aviao.getModelo() + aviao.getCompanhia() + aviao.getNumeroVoo())
    fila.adicionar(aviao1)
       
    while True:
                
       escolha = fila.mostrarMenu()
       
       if escolha == 1:
           fila.mostrarFilaPista()
         
       elif escolha == 2:
           fila.decolar()
           
       elif escolha == 3:
           modelo = input(str("Digite o modelo do avião: "))
           companhia = input(str("Digite a companhia do avião: "))
           numeroVoo = input(str("Digite o número do vôo: "))
           aviao = Aviao(modelo, companhia, numeroVoo)
           aviao1 = (aviao.getModelo()+ " " + aviao.getCompanhia()+ " " + aviao.getNumeroVoo())
           fila.adicionar(aviao1)
           
       elif escolha == 4:
           fila.mostrarFilaEspera()
           
       elif escolha == 5:
           if fila.avioes.empty():
               print("A Pista está vazia! ")
           else:
               print(fila.avioes.queue[0])
               
       elif escolha == 0:
           break
       else:
           print("Opção inválida! Tente novamente: ")
                
            
        
        
    
    

    