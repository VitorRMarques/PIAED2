import json


oc = {}

def add(id, nome, prioridade):
    oc["id"] = id,
    oc["nome"] = nome
    oc["prioridade"] = prioridade







while True:
    print("MENU")
    print("1. Cadastrar ocorrencia")
    print("2. Listar todas as ocorrencias")

    op = input("selecione a opcao: ")

    if op == "1":
        i = input("cadastrar? ")
        if i == "sim":
            ocorrencia = input("digite a ocorrencia: ")
            oc.append(ocorrencia)
            print("Ocorrencia inserida!")
        else:
            break
    if op == "2":
        print(oc)



