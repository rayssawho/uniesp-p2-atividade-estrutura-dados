from RuaPilha import RuaSemSaida

if __name__ == "__main__":
    
    rua = RuaSemSaida()
    rua.colocar(1111)
    rua.colocar(2222)
    rua.colocar(3333)
    rua.colocar(4444)
    rua.colocar(5555)
    
    rua.mostrar()
    
    escolha = int(input("> Rua sem Saída!! <\n1 - Retirar carro estacionado\n0 - Sair! \n"))
    
    if escolha == 1:
        carroEstacionado = False
        escolha2 = int(input("Digite a placa do carro que deseja retirar: "))
        for i in rua.carros:
            if i == escolha2:
                carroEstacionado = True
                rua.tirar(escolha2)
             