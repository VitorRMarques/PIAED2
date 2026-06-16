import json


ocorrencia = {}
ocorrencia_lista = []

def add(vetor, novaInsercao):
    for i in range(len(ocorrencia_lista)):
        vetor.append(novaInsercao)
        print(vetor)

while True:

    print("MENU")
    print("1. Cadastrar ocorrencia")
    print("2. Listar todas as ocorrencias")
    print("3. Buscar por ocorrência")

    op = input("selecione a opcao: ")

    if op == "1":
        i = input("cadastrar? ")

        if i == "s":
            ocorrencia["ID"] = int(input("digite o id: "))
            ocorrencia["nome"] = input("digite o nome: ")
            ocorrencia["prioridade"] = int(input("digite a prioridade: "))

            add(ocorrencia_lista, ocorrencia)
            print("Ocorrencia inserida!")
        else:
            break
    if op == "2":
        print(ocorrencia_lista)
        





