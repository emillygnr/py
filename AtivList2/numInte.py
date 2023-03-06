numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

media = (numero1 + numero2 + numero3) / 3

print("A média aritmética é:", media)

if media >= 7:
    print("Aprovado")
elif media >= 5 and media <= 6.9:
    print("Recuperação")
else:
    print("Reprovado")
