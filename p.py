#1 - Cadastrar ocorrência ***
#2 - Listar todas as ocorrências  ***
#3 - Atender próxima ocorrência pela fila
#4 - Atender ocorrência de maior prioridade
#5 - Buscar ocorrência por ID ***
#6 - Buscar ocorrências por nome ou tipo
#7 - Ordenar ocorrências
#8 - Ver histórico de ações
#9 - Desfazer última ação
#0 - Sair ***

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

def atender_proxima_ocorrencia():
    pass

def atender_ocorrencia_de_maior_prioridade():
    pass


def buscar_ocorrencia_por_id(vetor, id_busca):
    print("\nBuscar ocorrência")
    id_busca = ocorrencia["ID"]
    print(vetor(ocorrencia[id_busca]))

def buscar_ocorrencia_por_nome_ou_tipo():
    pass

def ordenar_ocorrencia():
    pass

def menu():

    while True:
        print("MENU")
        print("1. Cadastrar ocorrencia")
        print("2. Listar todas as ocorrencias")
        print("3. Atender próxima ocorrência pela fila")
        print("4. Atender ocorrência de maior prioridade")
        print("5. Buscar ocorrência por ID")
        print("6. Buscar ocorrências por nome ou tipo")
        print("7. Ordenar ocorrências")
        print("8. Ver histórico de ações")
        print("9. Desfazer última ação")
        print("0. Sair")

        op = input("selecione a opcao: ")

        if op == "1":
            print("*"*20)
            print("===== CADASTRANDO OCORRENCIA =====")
            print("*"*20)


            ocorrencia["nome"] = input("digite o nome da ocorrência: ")
            nome = ocorrencia["nome"]
            ocorrencia["ID"] = gerar_id(nome)
            ocorrencia["prioridade"] = int(input("digite a prioridade: "))

            ocorrencia["ID"] = id
            ocorrencia["nome"] = nome
            ocorrencia["prioridade"] = prioridade

            ocorrencia[id]
            ocorrencia[nome]
            ocorrencia[prioridade]

            cadastra_ocorrencia(ocorrencia_lista, ocorrencia)
            print("Ocorrencia inserida!")

            c = input("Deseja continuar?")
            if c == "s":
                continue
            else:
                menu()
        if op == "2":
            print("*"*20)
            print("===== LISTANDO OCORRENCIA =====")
            print("*"*20)
            print(ocorrencia_lista)
        if op == "3":
            print("*"*20)
            print("===== BUSCAR POR ID =====")
            print("*"*20)
            id_busca = input("Digite o id desejado para busca: ")
            ocorrencia["ID"] = id_busca

            print("*"*20)
            print("===== ELEMENTO =====")
            print("*"*20)

            buscar_ocorrencia_por_id(ocorrencia_lista, id_busca)

            

while True:
    menu()



#while True:
#
#    print("MENU")
#    print("1. Cadastrar ocorrencia")
#    print("2. Listar todas as ocorrencias")
#    print("3. Buscar por ocorrência")
#
#    op = input("selecione a opcao: ")
#
#    if op == "1":
#        ocorrencia["ID"] = int(input("digite o id: "))
#        ocorrencia["nome"] = input("digite o nome: ")
#        ocorrencia["prioridade"] = int(input("digite a prioridade: "))
#
#        cadastra_ocorrencia(ocorrencia_lista, ocorrencia)
#        print("Ocorrencia inserida!")
#
#        c = input("Deseja continuar?")
#
#        if c == "sim":
#            continue
#        else:
#            return 
#    if op == "2":
#        print(ocorrencia_lista)
#    if op == "3":
#        buscar_ocorrencia()

        





