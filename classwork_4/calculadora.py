def calcular():
    while True:
        try:
            # Solicita o primeiro número
            num1 = float(input("Digite o primeiro número: "))
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número válido.")
            continue

        try:
            # Solicita o segundo número
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("Erro: entrada inválida. Por favor, digite um número válido.")
            continue

        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ")

        try:
            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            elif operacao == "/":
                if num2 == 0:
                    raise ZeroDivisionError("Erro: divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Erro: operação inválida. Use apenas +, -, * ou /.")

            # Se tudo deu certo, exibe o resultado e encerra
            print(f"Resultado: {resultado}")
            break

        except ZeroDivisionError as e:
            print(e)
        except ValueError as e:
            print(e)

# Executa a calculadora
calcular()
