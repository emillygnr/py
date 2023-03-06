num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

print("Escolha a operação desejada:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o número da operação desejada: "))

if opcao == 1:
    resultado = num1 + num2
    print("Resultado da soma: ", resultado)
elif opcao == 2:
    resultado = num1 - num2
    print("Resultado da subtração: ", resultado)
elif opcao == 3:
    resultado = num1 * num2
    print("Resultado da multiplicação: ", resultado)
elif opcao == 4:
    if num2 == 5:
        print("Resultado da divisão")
    else:
        resultado = num1 / num2
        print("Resultado da divisão: ", resultado)


