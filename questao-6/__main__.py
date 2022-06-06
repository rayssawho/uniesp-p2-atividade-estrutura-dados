from Lista import Lista

if __name__ == "__main__":
    
    lista = Lista(5)
    lista.inserir(3)
    lista.inserir(7)
    lista.inserir(8)
    
    while True:
        escolha = int(input("Digita a opção desejada:\n\
        1 - Verificar se um número está na lista\n\
        2 - Inserir um novo elemento na lista\n\
        3 - Remover um elemento da lista\n\
        4 - Imprimir os valores da lista\n\
        0 - Sair.\n"))
        
        if escolha == 1:
            valor = int(input("Digite o número que deseja verificar: "))
            lista.pesquisar(valor)
        
        elif escolha == 2:
            valor = int(input("Digite o número que deseja adicionar na lista: "))
            lista.inserir(valor)
        
        elif escolha == 3:
            valor = int(input("Digite o número que deseja excluir: "))
            lista.excluir(valor)
        
        elif escolha == 4:
            lista.imprimir()
        
        elif escolha == 0:
            break 
        else:
            print("Opção inválida! Tente novamente: ")    
