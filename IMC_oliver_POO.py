#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Aug 14 2025

@author: oliverfagundes
"""

# Programa que leia o peso e a altura de uma pessoa e calcule sua massa IMC
# DESSA VEZ USANDO PROGRAMAÇAO ORIENTADA A OBJETOS
# IMC = peso (em quilos) ÷ altura*2 (em metros)

class Pessoa:
    def __init__(self, peso, altura, idade):
        self.peso = peso
        self.altura = altura
        self.idade = idade

    def imc(self):
        IMC = self.peso / (self.altura**2)
        return IMC

# Acima de 20 anos
# Menor que 18,5 - Abaixo do peso
# Entre 18,5 e 25,0 - Peso normal
# Entre 25,0 e 30,0 - Pré-obesidade
# Entre 30,0 e 35,0 - Obesidade Grau 1
# Entre 35,0 e 40,0 - Obesidade Grau 2
# Acima de 40 - Obesidade Grau 3

    def acima_20(self, imc):
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
        self.sexo = str(input('Qual seu gênero? Digite F para feminino, M para masculino ou NB para não-binárie: ')).strip().upper()
        return self.sexo

# Dicionário com idades: 
    dic = {'F': {10: [14.23, 20.19], 11: [14.60, 21.18], 12: [14.98, 22.17], 13: [15.36, 23.08], 14: [15.67, 23.88],
            15: [16.01, 24.29], 16: [16.37, 24.74], 17: [16.59, 25.23], 18: [16.71, 25.56], 19: [16.87, 25.85]},
            
            'M': {10: [14.42, 19.60], 11: [14.83, 20.35], 12: [15.24, 21.12], 13: [15.73, 21.93], 14: [16.18, 22.27],
            15: [16.59, 23.63], 16: [17.01, 24.45], 17: [17.31, 25.28], 18: [17.54, 25.95], 19: [17.80, 26.36]}}

# Entre 10 e 20 anos: 
    def entre10e20(self, genero, imc):  
        if 10 <= self.idade < 20 and genero in self.dic: 
            limites = self.dic[genero].get(self.idade)
            if limites:
                baixo, normal = limites
                if imc < baixo:
                    print("Baixo peso")
                elif baixo <= imc < normal:
                    print("Peso adequado")
                else:
                    print("Sobrepeso")
            else:
                print("Idade não encontrada na tabela.")        
        elif genero == "NB":
            print('Infelizmente, ainda não há informações científicas para o IMC de adolescentes não bináries.\nEspero que em breve possamos ter melhores informações.')

peso = float(input('Informe seu peso em kg: '))
altura = float(input("Informe a sua altura em metros: "))
idade = int(input("Informe a sua idade: "))

pessoa1 = Pessoa(peso, altura, idade)
imc_pessoa1 = pessoa1.imc()
print(f"Seu IMC é {imc_pessoa1}")
if idade >= 20:
    quadro = pessoa1.acima_20(imc_pessoa1)
    print(quadro)
else:
    genero = pessoa1.genero()
    quadro = pessoa1.entre10e20(genero, imc_pessoa1)
    print(quadro)
