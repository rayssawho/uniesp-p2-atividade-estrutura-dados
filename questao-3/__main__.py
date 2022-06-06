import random
from Circular import Circular

if __name__ == "__main__":
    
    soldados = Circular(6)
    
    for i in range(1, 6):
        soldados.enfileirar(i)
   
    aleatorio = random.randrange(1, 6)
        
    for i in range(1, aleatorio):
        eliminado = soldados.desenfileirar()
        if eliminado != aleatorio:
            soldados.enfileirar(eliminado)
    eliminado = soldados.desenfileirar()
    
    print(f"O número do chapéu restante é: {eliminado}")
    
    
