#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 29 18:10:26 2024

@author: oliver
"""

# Programa que leia o peso e a altura de uma pessoa e calcule seu massa IMC
# IMC = peso (em quilos) ÷ altura2 (em metros)

peso = float(input('Informe seu peso em kg: '))
altura = float(input("Informe a sua altura em metros: "))
idade = int(input("Informe a sua idade: "))

# calculo do imc
IMC = peso / (altura**2)

print('')
print("Seu IMC é ", IMC)

# Acima de 20 anos
# Menor que 18,5 - Abaixo do peso
# Entre 18,5 e 25,0 - Peso normal
# Entre 25,0 e 30,0 - Pré-obesidade
# Entre 30,0 e 35,0 - Obesidade Grau 1
# Entre 35,0 e 40,0 - Obesidade Grau 2
# Acima de 40 - Obesidade Grau 3

if idade >= 20: 
    if IMC < 18.5:
        print('Abaixo do peso ideal')
    elif IMC > 18.5 and IMC < 25:
        print('Peso normal')
    elif IMC > 25.0 and IMC < 30.0:
        print("Pré-obesidade")
    elif IMC > 30.0 and IMC < 35.0:
        print('Obesidade Grau 1')
    elif IMC > 35.0 and IMC < 40.0:
        print('Obesidade Grau 2')
    else:
        print('Obesidade Grau 3')
        
# Entre 10 e 20 anos: 
# Divisões por sexo
        
elif idade < 20 and idade > 10 : 
    sexo = str(input('Qual seu sexo? Digite F para feminino e M para masculino '))
    if sexo == 'F':
        if idade <= 10:
            if IMC < 14.23:
                print('Baixo peso')
            elif IMC >= 14.23 and IMC < 20.19:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 11:
            if IMC < 14.60:
                print('Baixo peso')
            elif IMC >= 14.60 and IMC < 21.18:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 12:
            if IMC < 14.98:
                print('Baixo peso')
            elif IMC >= 14.98 and IMC < 22.17:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 13:
            if IMC < 15.36:
                print('Baixo peso')
            elif IMC >= 15.36 and IMC < 23.08:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 14:
            if IMC < 15.67:
                print('Baixo peso')
            elif IMC >= 15.67 and IMC < 23.88:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 15:
            if IMC < 16.01:
                print('Baixo peso')
            elif IMC >= 16.01 and IMC < 24.29:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 16:
            if IMC < 16.37:
                print('Baixo peso')
            elif IMC >= 16.37 and IMC < 24.74:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 17:
            if IMC < 16.59:
                print('Baixo peso')
            elif IMC >= 16.59 and IMC < 25.23:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 18:
            if IMC < 16.71:
                print('Baixo peso')
            elif IMC >= 16.71 and IMC < 25.56:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 19:
            if IMC < 16.87:
                print('Baixo peso')
            elif IMC >= 16.87 and IMC < 25.85:
                print('Peso adequado')
            else:
                print("Sobrepeso")
    elif sexo == 'M':
        #AQUI TA OS MESMOS VALORES PARA O FEMININO, É SÓ OLHAR A TABELA E SUBSTITUIR
        if idade <= 10:
            if IMC < 14.23:
                print('Baixo peso')
            elif IMC >= 14.23 and IMC < 20.19:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 11:
            if IMC < 14.60:
                print('Baixo peso')
            elif IMC >= 14.60 and IMC < 21.18:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 12:
            if IMC < 14.98:
                print('Baixo peso')
            elif IMC >= 14.98 and IMC < 22.17:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 13:
            if IMC < 15.36:
                print('Baixo peso')
            elif IMC >= 15.36 and IMC < 23.08:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 14:
            if IMC < 15.67:
                print('Baixo peso')
            elif IMC >= 15.67 and IMC < 23.88:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 15:
            if IMC < 16.01:
                print('Baixo peso')
            elif IMC >= 16.01 and IMC < 24.29:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 16:
            if IMC < 16.37:
                print('Baixo peso')
            elif IMC >= 16.37 and IMC < 24.74:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 17:
            if IMC < 16.59:
                print('Baixo peso')
            elif IMC >= 16.59 and IMC < 25.23:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 18:
            if IMC < 16.71:
                print('Baixo peso')
            elif IMC >= 16.71 and IMC < 25.56:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        elif idade == 19:
            if IMC < 16.87:
                print('Baixo peso')
            elif IMC >= 16.87 and IMC < 25.85:
                print('Peso adequado')
            else:
                print("Sobrepeso")
        
