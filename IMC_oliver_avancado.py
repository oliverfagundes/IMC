#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 14 2025

@author: oliverfagundes
"""

# Programa que leia o peso e a altura de uma pessoa e calcule sua massa IMC
# DESSA VEZ USANDO PROGRAMAÇAO ORIENTADA A OBJETOS
# IMC = peso (em quilos) ÷ altura2 (em metros)

class Pessoa():
    def __innit__(self, peso, altura, idade, sexo = NB):
        peso = float(input('Informe seu peso em kg: '))
        altura = float(input("Informe a sua altura em metros: "))
        idade = int(input("Informe a sua idade: "))

    def imc(self, peso, altura):
        IMC = peso / (altura**2)
        print(f"\Seu IMC é {IMC}")
        return IMC

# Acima de 20 anos
# Menor que 18,5 - Abaixo do peso
# Entre 18,5 e 25,0 - Peso normal
# Entre 25,0 e 30,0 - Pré-obesidade
# Entre 30,0 e 35,0 - Obesidade Grau 1
# Entre 35,0 e 40,0 - Obesidade Grau 2
# Acima de 40 - Obesidade Grau 3

    def acima_20(self, imc, idade):
        if idade >= 20:
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
        
# Entre 10 e 20 anos: 
# Divisões por sexo
    def entre10e20(self, idade, imc, sexo):  
        if idade < 20 and idade > 10 : 
            sexo = str(input('Qual seu sexo? Digite F para feminino, M para masculino ou NB para não-binárie'))
            if sexo == 'F':
                if idade <= 10:
                    if imc < 14.23:
                        print('Baixo peso')
                    elif imc >= 14.23 and imc < 20.19:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 11:
                    if imc < 14.60:
                        print('Baixo peso')
                    elif imc >= 14.60 and imc < 21.18:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 12:
                    if imc < 14.98:
                        print('Baixo peso')
                    elif imc >= 14.98 and imc < 22.17:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 13:
                    if imc < 15.36:
                        print('Baixo peso')
                    elif imc >= 15.36 and imc < 23.08:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 14:
                    if imc < 15.67:
                        print('Baixo peso')
                    elif imc >= 15.67 and imc < 23.88:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 15:
                    if imc < 16.01:
                        print('Baixo peso')
                    elif imc >= 16.01 and imc < 24.29:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 16:
                    if imc < 16.37:
                        print('Baixo peso')
                    elif imc >= 16.37 and imc < 24.74:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 17:
                    if imc < 16.59:
                        print('Baixo peso')
                    elif imc >= 16.59 and imc < 25.23:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 18:
                    if imc < 16.71:
                        print('Baixo peso')
                    elif imc >= 16.71 and imc < 25.56:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 19:
                    if imc < 16.87:
                        print('Baixo peso')
                    elif imc >= 16.87 and imc < 25.85:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
            elif sexo == 'M':
                #AQUI TA OS MESMOS VALORES PARA O FEMININO, É SÓ OLHAR A TABELA E SUBSTITUIR
                if idade <= 10:
                    if imc < 14.23:
                        print('Baixo peso')
                    elif imc >= 14.23 and imc < 20.19:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 11:
                    if imc < 14.60:
                        print('Baixo peso')
                    elif imc >= 14.60 and imc < 21.18:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 12:
                    if imc < 14.98:
                        print('Baixo peso')
                    elif imc >= 14.98 and imc < 22.17:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 13:
                    if imc < 15.36:
                        print('Baixo peso')
                    elif imc >= 15.36 and imc < 23.08:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 14:
                    if imc < 15.67:
                        print('Baixo peso')
                    elif imc >= 15.67 and imc < 23.88:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 15:
                    if imc < 16.01:
                        print('Baixo peso')
                    elif imc >= 16.01 and imc < 24.29:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 16:
                    if imc < 16.37:
                        print('Baixo peso')
                    elif imc >= 16.37 and imc < 24.74:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 17:
                    if imc < 16.59:
                        print('Baixo peso')
                    elif imc >= 16.59 and imc < 25.23:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 18:
                    if imc < 16.71:
                        print('Baixo peso')
                    elif imc >= 16.71 and imc < 25.56:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")
                elif idade == 19:
                    if imc < 16.87:
                        print('Baixo peso')
                    elif imc >= 16.87 and imc < 25.85:
                        print('Peso adequado')
                    else:
                        print("Sobrepeso")