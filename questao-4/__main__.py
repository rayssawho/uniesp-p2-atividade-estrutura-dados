from Prioridade import FilaPrioridade

if __name__ == "__main__":
    
    fila = FilaPrioridade(5)
    fila.enfileirar(3)
    fila.enfileirar(5)
    fila.enfileirar(7)
    fila.enfileirar(2)
    fila.enfileirar(4)
         
    fila.desenfileirar()
    fila.desenfileirar()
    fila.desenfileirar()
    fila.desenfileirar()
    fila.desenfileirar()
    
    for i in fila.valores:
        print(f"Retirando o elemento {i}")
    
    
    
    
    