# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
# print(num1 + num2)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero1 = int(input("Digite o primeiro número: "))
# resto = numero1 % 5
# print(f"O resto de {numero1} dividido por 5 é: {resto}")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# n1 = int(input("Digite o 1º número: "))
# n2 = int(input("Digite o 2º número: "))
# print(n1 * n2)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# n1 = int(input("Digite o 1º número: "))
# n2 = int(input("Digite o 2º número: "))
# print(n1 // n2)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# n1 = int(input("Digite um número: "))
# print(n1 **2)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# NUM1 = 1.7
# NUM2 = 3.6
# print(f"A soma de {NUM1} com {NUM2} é igual à {NUM1 + NUM2}")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# num1 = float(input("Digite um numero no formato 0.0: "))
# num2 = float(input("Digite outro numero no formato 0.0: "))
# print((num1 + num2) /2)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite um número: "))
# expoente = int(input("O número será elevado à: "))
# print(base ** expoente)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura em graus Celsius: "))
# print(f"{celsius} graus Celsius em Fahrenheit é: {(celsius * 1.8) + 32}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o Raio: "))
# print(3.14*(raio**2))

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# palavra = input("Digite uma palavra: ")
# print(f"A palavra que digitou foi: {palavra.upper()}")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Digite seu nome completo: ")
# print(f"Seu nome é: {nome.upper()}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase com espaços no início e final: ")
# frase_ok = frase.strip()
# print(f"A frase é:{frase_ok}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma data no formato 'dd/mm/aaa': ")
# data_splitada = data.split("/")
# print(f"Dia: {data_splitada[0]}")
# print(f"Mês: {data_splitada[1]}")
# print(f"Ano: {data_splitada[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
palavra1 = input("Digite uma palavra: ")
palavra2 = input("Digite mais uma palavra: ")

print(f"Você digitou as palavras: {palavra1+palavra2}")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
