'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input("Digite seu nome completo: ")).strip()

print("Muito prazer em te conhecer!")


print(f'seu primeiro nome é {nome.split()[0]}')

print(f'Seu ultimo nome é {nome.split().pop()}')