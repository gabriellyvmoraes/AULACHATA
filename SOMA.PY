idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print("Você já pode tirar a carteira de motorista!")
else:
    anos_restantes = 18 - idade
    print(f"Ainda não pode dirigir. Faltam {anos_restantes} anos.")