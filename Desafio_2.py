# Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor:
# Exemplo:
# Você digitou o número : 10
# O sucessor dele é o número : 11
# O antecessor dele é o número : 9


numero = int(input("Digite um número: "))

antecessor = numero - 1
sucessor = numero + 1

# Exibe os resultados na tela
print(f"O antecessor de {numero} é {antecessor}")
print(f"O sucessor de {numero} é {sucessor}")
