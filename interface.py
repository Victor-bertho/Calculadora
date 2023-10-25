from operacoes import adicionar, subtrair , multiplicar, dividir, potencia

def run_calculadora():
    while True:
        print("Opções:")
        print("Digite 'sair' para encerrar o programa")
        print("Digite '+' para adicionar dois números")
        print("Digite '-' para subtrair dois números")
        print("Digite '*' para multiplicar dois números")
        print("Digite '/' para dividir dois números")
        print("Digite '^' para potência de um número")
        
        user_input = input(": ")

        if user_input == "sair":
            break

        if user_input in ('+', '-', '*', '/', '^'):
            x = float(input("Digite o primeiro número: "))
            y = float(input("Digite o segundo número: "))

            if user_input == '+':
                print(adicionar(x, y))
            elif user_input == '-':
                print(subtrair(x, y))
            elif user_input == '*':
                print(multiplicar(x, y))
            elif user_input == '/':
                print(dividir(x, y))
            elif user_input == '^':
                print(potencia(x, y))

        else:
            print("Entrada inválida")
