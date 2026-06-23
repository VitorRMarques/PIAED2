import json


ocorrencia = {}
ocorrencia_lista = []

def gerar_id(nome):
    soma = 0
    for letra in nome:
        soma = soma + ord(letra)
    
    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)


def cadastra_ocorrencia(vetor, novaInsercao):
    vetor.append(novaInsercao)

def listar_ocorrencias():
    print("\nListar ocorrencias")
    print(ocorrencia_lista)

def buscar_ocorrencia():
    print("\nBuscar ocorrência")
    id_busca = input("Digite o ID de busca")

while True:

    print("MENU")
    print("1. Cadastrar ocorrencia")
    print("2. Listar todas as ocorrencias")
    print("3. Buscar por ocorrência")

    op = input("selecione a opcao: ")

    if op == "1":
        ocorrencia["ID"] = int(input("digite o id: "))
        ocorrencia["nome"] = input("digite o nome: ")
        ocorrencia["prioridade"] = int(input("digite a prioridade: "))

        cadastra_ocorrencia(ocorrencia_lista, ocorrencia)
        print("Ocorrencia inserida!")

        c = input("Deseja continuar?")

        if c == "sim":
            continue
        else:
            break
    if op == "2":
        print(ocorrencia_lista)
        





