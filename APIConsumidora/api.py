#Script para consumir API
#Linguagem utilizada : Python3
#Created by Jhonatas Rodrigues
#

import requests
import json
import os

# Request Area
data = requests.get('http://localhost:8000/api/filmes')
binary = data.content
output = json.loads(binary)
# Menu Area
os.system('clear')
def Menu():
        print("--> Bem vindo ao apipy 1.0 <--")
        print( "(Menu)")
        print( ">> Use (1) Para Ver Filmes")
        print( ">> Use (2) Para Inserir Filmes")
        print( ">> Use (3) Para Deletar Filmes")
        print( ">> Use (0) Para Abortar :/")
Menu()
valor = input('Resposta :')
if valor == '1':
    os.system('clear')
    x = 0
    print("\n-----Filmes encontrados-----\n")
    for item in output['data']:
        print('>> Id:',item['id'],'\n>> Nome: ', item['name'], '\n>> Descrição :', item['description'], '\n')
elif valor == '2' :
    os.system('clear')
    nome = input("Digite o Nome do Filme :")
    desc = input("Digite a Descrição do Filme :")
    requests.post('http://localhost:8000/api/filmes', data = {'name':nome, 'description': desc})
elif valor == '3':
    os.system('clear')
    print(" >> Use (1) Deletar Apenas Um Filme")
    print(" >> Use (2) Para Deletar Todos os Filmes")
    print(" >> Use (0) Para Retornar ao Menu")
    resposta = input("Resposta :")
    if resposta == '1':
        filmeId = input('Digite o Id do Filme :')
        requests.delete('http://localhost:8000/api/filmes/' + filmeId)
    elif resposta == '2':
        requests.delete('http://localhost:8000/api/filmes')
    else :
        Menu()
else :
    print("By by :)")
#Percorrendo dados
