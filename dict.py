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
from collections import deque


ocorrencia_lista = []
historico_acoes = []
indice_atual = 0


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
    print("ATENDER PROXIMA OCORRENCIA (FIFO)")

    if not ocorrencia_lista:
        print("Nao ha proxima ocorrencia para atender")
        return

    at = input("Atender fila? (s ou n): ")
    if at == "s":
        oc = ocorrencia_lista.pop(0)
        historico_acoes.append({'acoes': 'atender_fila', 'ocorrencia': oc, 'index': 0})
        print("Ocorrencia atendida:")
        print(f"ID: {oc['id']} | {oc['nome']} | {oc['prioridade']}")
    else:
        menu()

def atender_ocorrencia_de_maior_prioridade():

    if not ocorrencia_lista:
        print("Nenhuma ocorrência cadastrada.")
        return

    maior_prioridade = max(
        int(item["prioridade"])
        for item in ocorrencia_lista
    )

    for i, item in enumerate(ocorrencia_lista):
        if int(item["prioridade"]) == maior_prioridade:

            oc = ocorrencia_lista.pop(i)

            historico_acoes.append({
                'acoes': 'atender_prioridade',
                'ocorrencia': oc,
                'index': i
            })

            print("Ocorrência atendida:")
            print(
                f"ID: {oc['id']} | "
                f"{oc['nome']} | "
                f"{oc['prioridade']}"
            )
            return
    
    
def encontrar_id(id_):
    for i, o in enumerate(ocorrencia_lista):
        if o['id'] == id_:
            return i
    return None

def buscar_ocorrencia_por_id():
    print("\nBuscando ocorrência por id")
    search = input("digite o ID: ")
    idx = encontrar_id(search)
    if idx is None:
        print("Ocorrencia nao encontrada.")
    else:
        o = ocorrencia_lista[idx]
        print("Ocorrencia encontrada:")
        print(f"ID: {o['id']} | nome: {o['nome']} | prioridade: {o['prioridade']}")

def buscar_ocorrencia_por_nome():
    nome = input("Insira o nome de busca para encontrar a ocorrencia: ")
    resultado = [o for o in ocorrencia_lista if (nome.lower() in o["nome"].lower() if nome else True)]
        
    if not resultado:
        return "Nenhuma ocorrencia encontrada"
    for o in resultado:
        print(f"ID: {o['id']} | nome: {o['nome']} | prioridade: {o['prioridade']}")

def ordenar_ocorrencia():
    prev_order = [o['id'] for o in ocorrencia_lista]
    ocorrencia_lista.sort(key=lambda x: int(x["prioridade"]), reverse=True)
    historico_acoes.append({'acoes': 'ordenar', 'prev_order': prev_order})
    print("Lista de ocorrencias em ordem ascendente:")

    for o in ocorrencia_lista:
        print(f"ID: {o['id']} | nome: {o['nome']} | prioridade: {o['prioridade']}")
        

def historico():
    print("\nHistorico de acoes")
    if not historico_acoes:
        print("Nenhuma acao no historico.")
        return
    
    for i, h in enumerate(historico_acoes, start=1):
        ac = h.get('acoes')
        if ac == "cadastrar":
            print(f"{i}. Cadastrar - ID {h['ocorrencia']['id']}")
        elif ac.startswith("atender"):
            print(f"{i}. Atender - ID {h['ocorrencia']['id']}")
        elif ac == "ordenar":
            print(f"{i}. ordenar - Ordem anterior: {h["prev_order"]}")
        else:
            print(f"{i}. {ac}")

def desfazer():
    print("\nDESFAZER ULTIMA ACAO")
    if not historico_acoes:
        print("Nenhuma acao para desfazer.")
        return

    h = historico_acoes.pop()
    ac = h.get('acoes')

    # Desfazer cadastro
    if ac == "cadastrar":
        id_remover = h["ocorrencia"]["id"]
        idx = encontrar_id(id_remover)
        if idx is not None:
            ocorrencia_lista.pop(idx)
            print(f"Desfeito cadastro da ocorrencia {id_remover}.")
        else:
            print("Ocorrencia ja removida.")

    # Desfazer atendimento (fila ou prioridade)
    elif ac in ('atender_fila', 'atender_prioridade'):
        oc = h["ocorrencia"]
        idx = h.get("index", 0)
        if idx is None or idx > len(ocorrencia_lista):
            ocorrencia_lista.append(oc)
        else:
            ocorrencia_lista.insert(idx, oc)
        print(f"Desfeito atendimento da ocorrencia {oc['id']}.")

    # Desfazer ordenação
    elif ac == "ordenar":
        prev = h["prev_order"]
        id_ao_objeto = {o['id']: o for o in ocorrencia_lista}
        nova_lista = []
        for _id in prev:
            if _id in id_ao_objeto:
                nova_lista.append(id_ao_objeto.pop(_id))
        for o in ocorrencia_lista:
            if o['id'] in id_ao_objeto:
                nova_lista.append(o)
        ocorrencia_lista.clear()
        ocorrencia_lista.extend(nova_lista)
        print("Ordem Restaurada.")

    # Desfazer busca (opcional, apenas informativo)
    elif ac == "buscar":
        termo = h.get("termo", "")
        print(f"Busca por '{termo}' desfeita (nenhuma alteração na lista).")

    else:
        print(f"Ação '{ac}' não reconhecida para desfazer.")  
    

def menu():

    while True:
        print("MENU")
        print("1. Cadastrar ocorrencia")
        print("2. Listar todas as ocorrencias")
        print("3. Atender próxima ocorrência pela fila")
        print("4. Atender ocorrência de maior prioridade")
        print("5. Buscar ocorrência por ID")
        print("6. Buscar ocorrências por nome")
        print("7. Ordenar ocorrências")
        print("8. Ver histórico de ações")
        print("9. Desfazer última ação")
        print("0. Sair")

        op = input("selecione a opcao: ")

        if op == "1":
            print("*"*20)
            print("===== CADASTRANDO OCORRENCIA =====")
            print("*"*20)


            nome = input("digite o nome da ocorrência: ")
            id_ = gerar_id(nome)
            prioridade = input("prioridade: ")

            ocorrencia = {
                'id': id_,
                'nome': nome,
                'prioridade': prioridade
            }
            cadastra_ocorrencia(ocorrencia_lista, ocorrencia)
            print("Ocorrencia inserida!")

            c = input("Deseja continuar?")
            if c == "s":
                continue
            else:
                menu()
        if op == "2":
            print("*"*20)
            print("===== LISTANDO OCORRENCIAS =====")
            print("*"*20)
            print(ocorrencia_lista)
        if op == "3":
            print("*"*20)
            print("===== ATENDENDO PROXIMA OCORRENCIA =====")
            print("*"*20)
            print(atender_proxima_ocorrencia())
        if op == "4":
            print("*"*20)
            print("===== LISTANDO OCORRENCIAS =====")
            print("*"*20)
            print(atender_ocorrencia_de_maior_prioridade())
        if op == "5":
            print("*"*20)
            print("===== BUSCA DE OCORRENCIA POR ID =====")
            print("*"*20)
            buscar_ocorrencia_por_id()
        if op == "6":
            print("*"*20)
            print("===== BUSCAR POR NOME =====")
            print("*"*20)
            buscar_ocorrencia_por_nome()
        if op == "7":
            print("*"*20)
            print("===== ORDENACAO DE OCORRENCIAS =====")
            print("*"*20)
            ordenar_ocorrencia()
        if op == "8":
            print("*"*20)
            print("===== VER HISTORICO DE ACOES =====")
            print("*"*20)
            historico()
        if op == "9":
            print("*"*20)
            print("===== DESFAZER ULTIMA ACAO DO")


            

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