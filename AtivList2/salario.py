nome = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))

if salario <= 1500:
    aumento = salario * 0.1
else:
    aumento = salario * 0.05

novo_salario = salario + aumento
diferenca = novo_salario - salario

print("O novo salário de", nome, "é: R$", novo_salario)
print("A diferença salarial é: R$", diferenca)
