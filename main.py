import json

ocorrencia_lista = []
historico_acoes = []

def gerar_id(nome):
    soma = 0

    for letra in nome:
        soma += ord(letra)

    codigo = soma % 10000
    prefixo = nome[:3].upper()

    return prefixo + "-" + str(codigo)


def cadastra_ocorrencia(vetor, novaInsercao):
    vetor.append(novaInsercao)

    historico_acoes.append({
        'acoes': 'cadastrar',
        'ocorrencia': novaInsercao.copy()
    })


def listar_ocorrencias():
    print("\n===== LISTA DE OCORRÊNCIAS =====")

    if not ocorrencia_lista:
        print("Nenhuma ocorrência cadastrada.")
        return

    for o in ocorrencia_lista:
        print(
            f"ID: {o['id']} | "
            f"Nome: {o['nome']} | "
            f"Prioridade: {o['prioridade']}"
        )


def encontrar_id(id_):
    for i, o in enumerate(ocorrencia_lista):
        if o['id'] == id_:
            return i

    return None


def atender_proxima_ocorrencia():
    print("ATENDER PRÓXIMA OCORRÊNCIA (FIFO)")

    if not ocorrencia_lista:
        print("Não há ocorrência para atender.")
        return

    at = input("Atender fila? (s ou n): ").lower()

    if at == "s":
        oc = ocorrencia_lista.pop(0)

        historico_acoes.append({
            'acoes': 'atender_fila',
            'ocorrencia': oc,
            'index': 0
        })

        print("Ocorrência atendida:")
        print(
            f"ID: {oc['id']} | "
            f"{oc['nome']} | "
            f"{oc['prioridade']}"
        )


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


def buscar_ocorrencia_por_id():

    print("\nBuscando ocorrência por ID")

    search = input("Digite o ID: ")

    idx = encontrar_id(search)

    historico_acoes.append({
        'acoes': 'buscar_id',
        'termo': search
    })

    if idx is None:
        print("Ocorrência não encontrada.")
    else:
        o = ocorrencia_lista[idx]

        print("Ocorrência encontrada:")
        print(
            f"ID: {o['id']} | "
            f"Nome: {o['nome']} | "
            f"Prioridade: {o['prioridade']}"
        )


def buscar_ocorrencia_por_nome():

    nome = input(
        "Insira o nome para encontrar a ocorrência: "
    )

    historico_acoes.append({
        'acoes': 'buscar_nome',
        'termo': nome
    })

    resultado = [
        o for o in ocorrencia_lista
        if nome.lower() in o["nome"].lower()
    ]

    if not resultado:
        print("Nenhuma ocorrência encontrada.")
        return

    for o in resultado:
        print(
            f"ID: {o['id']} | "
            f"Nome: {o['nome']} | "
            f"Prioridade: {o['prioridade']}"
        )


def ordenar_ocorrencia():

    prev_order = [o['id'] for o in ocorrencia_lista]

    ocorrencia_lista.sort(
        key=lambda x: int(x["prioridade"]),
        reverse=True
    )

    historico_acoes.append({
        'acoes': 'ordenar',
        'prev_order': prev_order
    })

    print("Ocorrências ordenadas por prioridade.")


def historico():

    print("\n===== HISTÓRICO =====")

    if not historico_acoes:
        print("Nenhuma ação registrada.")
        return

    for i, h in enumerate(historico_acoes, start=1):

        ac = h.get('acoes')

        if ac == "cadastrar":
            print(
                f"{i}. Cadastro - "
                f"{h['ocorrencia']['id']}"
            )

        elif ac in ("atender_fila", "atender_prioridade"):
            print(
                f"{i}. Atendimento - "
                f"{h['ocorrencia']['id']}"
            )

        elif ac == "ordenar":
            print(
                f"{i}. Ordenação"
            )

        elif ac == "buscar_id":
            print(
                f"{i}. Busca por ID - "
                f"{h['termo']}"
            )

        elif ac == "buscar_nome":
            print(
                f"{i}. Busca por nome - "
                f"{h['termo']}"
            )


def desfazer():

    print("\n===== DESFAZER =====")

    if not historico_acoes:
        print("Nenhuma ação para desfazer.")
        return

    h = historico_acoes.pop()

    ac = h.get('acoes')

    if ac == "cadastrar":

        id_remover = h["ocorrencia"]["id"]

        idx = encontrar_id(id_remover)

        if idx is not None:
            ocorrencia_lista.pop(idx)

        print(
            f"Cadastro da ocorrência "
            f"{id_remover} desfeito."
        )

    elif ac in (
        "atender_fila",
        "atender_prioridade"
    ):

        oc = h["ocorrencia"]
        idx = h["index"]

        ocorrencia_lista.insert(idx, oc)

        print(
            f"Atendimento da ocorrência "
            f"{oc['id']} desfeito."
        )

    elif ac == "ordenar":

        prev = h["prev_order"]

        mapa = {
            o['id']: o
            for o in ocorrencia_lista
        }

        restaurada = []

        for id_ in prev:
            if id_ in mapa:
                restaurada.append(mapa[id_])

        ocorrencia_lista.clear()
        ocorrencia_lista.extend(restaurada)

        print("Ordenação desfeita.")

    elif ac == "buscar_id":

        print(
            f"Busca por ID "
            f"{h['termo']} desfeita."
        )

    elif ac == "buscar_nome":

        print(
            f"Busca por nome "
            f"{h['termo']} desfeita."
        )


def menu():

    while True:

        print("\nMENU")
        print("1. Cadastrar ocorrência")
        print("2. Listar todas as ocorrências")
        print("3. Atender próxima ocorrência pela fila")
        print("4. Atender ocorrência de maior prioridade")
        print("5. Buscar ocorrência por ID")
        print("6. Buscar ocorrências por nome")
        print("7. Ordenar ocorrências")
        print("8. Ver histórico de ações")
        print("9. Desfazer última ação")
        print("0. Sair")

        op = input("Selecione a opção: ")

        if op == "1":

            print("*" * 20)
            print("CADASTRAR OCORRÊNCIA")
            print("*" * 20)

            nome = input(
                "Digite o nome da ocorrência: "
            )

            prioridade = input(
                "Prioridade: "
            )

            ocorrencia = {
                'id': gerar_id(nome),
                'nome': nome,
                'prioridade': prioridade
            }

            cadastra_ocorrencia(
                ocorrencia_lista,
                ocorrencia
            )

            print("Ocorrência cadastrada!")

        elif op == "2":

            listar_ocorrencias()

        elif op == "3":

            atender_proxima_ocorrencia()

        elif op == "4":

            atender_ocorrencia_de_maior_prioridade()

        elif op == "5":

            buscar_ocorrencia_por_id()

        elif op == "6":

            buscar_ocorrencia_por_nome()

        elif op == "7":

            ordenar_ocorrencia()

        elif op == "8":

            historico()

        elif op == "9":

            desfazer()

        elif op == "0":

            print("Encerrando sistema...")
            break

        else:

            print("Opção inválida.")


menu()

