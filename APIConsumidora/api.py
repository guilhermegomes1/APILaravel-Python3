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
def menu():
        print("--> Bem vindo ao apipy 1.0 <--")
        print( "(Menu)")
        print( ">> Use (1) Para Ver Filmes")
        print( ">> Use (2) Para Inserir Filmes")
        print( ">> Use (3) Para Atualizar Filmes")
        print( ">> Use (4) Para Deletar Filmes")
        print( ">> Use (0) Para Abortar :/")
menu()
valor = input('Resposta :')
if valor == '1':
    os.system('clear')
    x = 0
    print("\n-----Filmes encontrados-----\n")
    for item in output['data']:
        print('>> Id:',item['id'],'\n>> Nome: ', item['name'], '\n>> Descrição :', item['description'], '\n>> Categoria :', item['categorias']['name'])
elif valor == '2' :
    os.system('clear')
    print(" >> Use (1) Categoria Ação")
    print(" >> Use (2) Categoria Romance")
    categoria = input('Digite o Número da Categoria: ')
    nome = input("Digite o Nome do Filme :")
    desc = input("Digite a Descrição do Filme :")
    requests.post('http://localhost:8000/api/filmes', data = {'name':nome, 'description': desc, 'categoria_id':categoria})
elif valor == '4':
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
elif valor == '3':
    os.system('clear')
    print(" >> Use (1) Categoria Ação")
    print(" >> Use (2) Categoria Romance")
    identifier = input('Digite o ID do Filme Que Você Deseja Alterar : ')
    categoriaN = input('Nova Categoria: ')
    title = input('Novo Titulo : ')
    des = input('Nova Descrição : ')
    requests.put('http://localhost:8000/api/filmes/' + identifier , data = {'id': identifier, 'name':title, 'description': des, 'categoria_id':categoriaN})
else :
    print("By by :)")
#Percorrendo dados
