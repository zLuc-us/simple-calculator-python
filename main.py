# Função principal da calculadora
def calculadora():
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    # Ler a operação escolhida e os dois números
    option = input("Digite sua opção (1/2/3/4): ")
    number_one = float(input("Digite o primeiro número: "))
    number_two = float(input("Digite o segundo número: "))

    # Executar a operação escolhida
    if option == '1':
        result = number_one + number_two
    elif option == '2':
        result = number_one - number_two
    elif option == '3':
        result = number_one * number_two
    elif option == '4':
        result = number_one / number_two
    else:
        print("Opção inválida!")
        return

    # Imprimir o resultado
    print("Resultado: ", result)


# Executar a calculadora
calculadora()
