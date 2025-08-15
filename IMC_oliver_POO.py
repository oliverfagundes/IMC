#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 14 2025

@author: oliverfagundes
"""

# Programa que leia o peso e a altura de uma pessoa e calcule sua massa IMC
# DESSA VEZ USANDO PROGRAMAÇAO ORIENTADA A OBJETOS
# IMC = peso (em quilos) ÷ altura*2 (em metros)

class Pessoa():
    def __init__(self, peso, altura, idade):
        self.peso = peso
        self.altura = altura
        self.idade = idade

    def imc(self):
        IMC = self.peso / (self.altura)**2
        print(f"Seu IMC é {IMC}")
        return IMC

# Acima de 20 anos
# Menor que 18,5 - Abaixo do peso
# Entre 18,5 e 25,0 - Peso normal
# Entre 25,0 e 30,0 - Pré-obesidade
# Entre 30,0 e 35,0 - Obesidade Grau 1
# Entre 35,0 e 40,0 - Obesidade Grau 2
# Acima de 40 - Obesidade Grau 3

    def acima_20(self):
        if self.idade >= 20:
            if imc < 18.5:
                print('Abaixo do peso ideal')
            elif imc > 18.5 and imc < 25:
                print('Peso normal')
            elif imc > 25.0 and imc < 30.0:
                print("Pré-obesidade")
            elif imc > 30.0 and imc < 35.0:
                print('Obesidade Grau 1')
            elif imc > 35.0 and imc < 40.0:
                print('Obesidade Grau 2')
            else:
                print('Obesidade Grau 3')

# Divisões por sexo:
    def genero(self):
        sexo = str(input('Qual seu gênero? Digite F para feminino, M para masculino ou NB para não-binárie'))
        return sexo

# Entre 10 e 20 anos: 
    def entre10e20(self):  
        if self.idade < 20 and self.idade > 10 : 
            if self.genero() == 'F':
                if self.idade <= 10:
                    if imc < 14.23:
                        print('Baixo peso')
                    elif imc >= 14.23 and imc < 20.19:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 11:
                    if self.imc < 14.60:
                        print('Baixo peso')
                    elif imc >= 14.60 and imc < 21.18:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 12:
                    if imc < 14.98:
                        print('Baixo peso')
                    elif imc >= 14.98 and imc < 22.17:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 13:
                    if imc < 15.36:
                        print('Baixo peso')
                    elif imc >= 15.36 and imc < 23.08:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 14:
                    if imc < 15.67:
                        print('Baixo peso')
                    elif imc >= 15.67 and imc < 23.88:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 15:
                    if imc < 16.01:
                        print('Baixo peso')
                    elif imc >= 16.01 and imc < 24.29:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 16:
                    if imc < 16.37:
                        print('Baixo peso')
                    elif imc >= 16.37 and imc < 24.74:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 17:
                    if imc < 16.59:
                        print('Baixo peso')
                    elif imc >= 16.59 and imc < 25.23:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 18:
                    if imc < 16.71:
                        print('Baixo peso')
                    elif imc >= 16.71 and imc < 25.56:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 19:
                    if imc < 16.87:
                        print('Baixo peso')
                    elif imc >= 16.87 and imc < 25.85:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")

            elif self.genero() == 'M':
                if self.idade <= 10:
                    if imc < 14.42:
                        print('Baixo peso')
                    elif imc >= 14.42 and imc < 19.60:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 11:
                    if imc < 14.83:
                        print('Baixo peso')
                    elif imc >= 14.83 and imc < 20.35:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 12:
                    if imc < 15.24:
                        print('Baixo peso')
                    elif imc >= 15.24 and imc < 21.12:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 13:
                    if self.imc < 15.73:
                        print('Baixo peso')
                    elif imc >= 15.73 and imc < 21.93:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 14:
                    if imc < 16.18:
                        print('Baixo peso')
                    elif imc >= 16.18 and imc < 22.27:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 15:
                    if imc < 16.59:
                        print('Baixo peso')
                    elif imc >= 16.59 and imc < 23.63:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 16:
                    if imc < 17.01:
                        print('Baixo peso')
                    elif imc >= 17.01 and imc < 24.45:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 17:
                    if imc < 17.31:
                        print('Baixo peso')
                    elif imc >= 17.31 and imc < 25.28:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 18:
                    if imc < 17.54:
                        print('Baixo peso')
                    elif imc >= 17.54 and imc < 25.95:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif self.idade == 19:
                    if imc < 17.80:
                        print('Baixo peso')
                    elif imc >= 17.80 and imc < 26.36:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
            elif self.genero() == "NB":
                print('Infelizmente, ainda não há informações cinetíficas para o IMC de adolescentes não bináries.\nEspero que em breve possamos ter melhores infromações.')


peso = float(input('Informe seu peso em kg: '))
altura = float(input("Informe a sua altura em metros: "))
idade = int(input("Informe a sua idade: "))

pessoa1 = Pessoa(peso, altura, idade)
imc_pessoa1 = pessoa1.imc
print(f"Seu IMC é {imc_pessoa1}")
if idade >= 20:
    quadro = pessoa1.acima_20
    print(quadro)
else:
    quadro = pessoa1.entre10e20
    print(quadro)
