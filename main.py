import heapq

import uuid

from collections import deque

class No:
    def __init__(self, ocorrencia):
        self.ocorrencia = ocorrencia
        self.esquerda = None
        self.direita = None



class ArvoreID:

    def __init__(self):
        self.raiz = None

    def inserir(self, ocorrencia):

        novo = No(ocorrencia)

        if self.raiz is None:
            self.raiz = novo
            return

        atual = self.raiz

        while True:

            if ocorrencia['id'] < atual.ocorrencia['id']:

                if atual.esquerda is None:
                    atual.esquerda = novo
                    return

                atual = atual.esquerda

            else:

                if atual.direita is None:
                    atual.direita = novo
                    return

                atual = atual.direita
    def buscar(self, id_):

        atual = self.raiz

        while atual:

            if id_ == atual.ocorrencia['id']:
                return atual.ocorrencia

            elif id_ < atual.ocorrencia['id']:
                atual = atual.esquerda

            else:
                atual = atual.direita

        return None

heap_prioridades = []

fila_ocorrencias = deque()

ocorrencia_lista = []

ocorrencia_lista_abertas = []

ocorrencia_lista_fechadas = []

arvore_ids = ArvoreID()

historico_acoes = []

indice_nome = {}

indice_tipo = {}

ordem_chegada_counter = 0



def gerar_id():
  return str(uuid.uuid4())[:8]


def cadastra_ocorrencia(ocorrencias_list, ocorrencias_list_aberta, novaInsercao):
    ocorrencias_list.append(novaInsercao)
    ocorrencias_list_aberta.append(novaInsercao)

    arvore_ids.inserir(novaInsercao)

    historico_acoes.append({
        'acoes': 'cadastrar',
        'ocorrencia': novaInsercao.copy()
    })

def listar_ocorrencias():
  print("\n===== LISTA DE TODAS AS OCORRENCIAS ====")

  if not ocorrencia_lista:
    print("Nenhuma ocorrencia cadastrada.")
    return

  for o in ocorrencia_lista:
    print(f"ID: {o['id']} |"
          f"Nome: {o['nome']} |"
          f"Tipo: {o['tipo']} |"
          f"Descricao: {o['descricao']} |"
          f"Prioridade: {o['prioridade']} |"
          f"Ordem chegada: {o['ordem_chegada']} |"
          f"Status: {o['status']}")

def listar_ocorrencias_abertas():
    print("\n===== LISTA DE OCORRÊNCIAS ABERTAS =====")

    if not ocorrencia_lista_abertas:
        print("Nenhuma ocorrência aberta cadastrada.")
        return

    for o in ocorrencia_lista_abertas:
        print(
            f"ID: {o['id']} | "
            f"Nome: {o['nome']} | "
            f"Tipo: {o['tipo']} |"
            f"Descricao: {o['descricao']} |"
            f"Prioridade: {o['prioridade']} |"
            f"Ordem chegada: {o['ordem_chegada']} |"
            f"Status: {o['status']}"
        )

def listar_ocorrencias_fechadas():
    print("\n===== LISTA DE OCORRÊNCIAS FECHADAS =====")

    if not ocorrencia_lista_fechadas:
        print("Nenhuma ocorrência fechada.")
        return

    for o in ocorrencia_lista_fechadas:
        print(
            f"ID: {o['id']} | "
            f"Nome: {o['nome']} | "
            f"Tipo: {o['tipo']} |"
            f"Descricao: {o['descricao']} |"
            f"Prioridade: {o['prioridade']} |"
            f"Ordem chegada: {o['ordem_chegada']} |"
            f"Status: {o['status']}"
        )

def encontrar_id(id_):
    for i, o in enumerate(ocorrencia_lista):
        if o['id'] == id_:
            return i

    return None

def atender_proxima_ocorrencia():
    print("ATENDER PRÓXIMA OCORRÊNCIA (FIFO)")

    if not ocorrencia_lista_abertas:
        print("Não há ocorrência para atender.")
        return

    at = input("Atender fila? (s ou n): ").lower()

    if at == "s":
      fila_ocorrencias.append(ocorrencia_lista)
      oc = fila_ocorrencias.popleft()
      ocorrencia_lista_fechadas.append(oc)
      ocorrencia_lista_abertas.remove(oc)

      historico_acoes.append({
          'acoes': 'atender_fila',
          'ocorrencia': oc.copy(),
          'index': 0
      })

      print("ANTES --|.")

      print(
          f"ID: {oc['id']} | "
          f"{oc['nome']} | "
          f"{oc['tipo']} |"
          f"{oc['prioridade']} |"
          f"{oc['ordem_chegada']} |"
          f"{oc['status']}"
      )

      oc["status"] = "Fechada"

      print("DEPOIS --|.")
      print("Ocorrência atendida:")

      print(
          f"ID: {oc['id']} | "
          f"{oc['nome']} | "
          f"{oc['tipo']} |"
          f"{oc['prioridade']} |"
          f"{oc['ordem_chegada']} |"
          f"{oc['status']}"
      )

def atender_ocorrencia_de_maior_prioridade():

    if not heap_prioridades:
        print("Nenhuma ocorrência cadastrada.")
        return

    _, _, oc_from_heap = heapq.heappop(heap_prioridades)

    original_index = -1
    for i, item in enumerate(ocorrencia_lista_abertas):
        if item["id"] == oc_from_heap["id"]:
            original_index = i
            break

    if original_index != -1:
        oc = ocorrencia_lista_abertas.pop(original_index)
        ocorrencia_lista_fechadas.append(oc)

        print("ANTES --|.")

        print(
            f"ID: {oc['id']} | "
            f"Nome: {oc['nome']} | "
            f"Tipo: {oc['tipo']} | "
            f"Prioridade: {oc['prioridade']} |"
            f"Ordem chegada: {oc['ordem_chegada']} |"
            f"Status: {oc['status']}"
        )

        oc["status"] = "Fechada"

        historico_acoes.append({
            'acoes': 'atender_prioridade',
            'ocorrencia': oc.copy(),
            'index': original_index
        })

        print("DEPOIS --|.")

        print("Ocorrência atendida:")

        print(
            f"ID: {oc['id']} | "
            f"Nome: {oc['nome']} | "
            f"Tipo: {oc['tipo']} | "
            f"Prioridade: {oc['prioridade']} |"
            f"Ordem chegada: {oc['ordem_chegada']} |"
            f"Status: {oc['status']}"
        )
    else:
        print(f"Ocorrência com ID {oc_from_heap['id']} não encontrada na lista de abertas.")

def buscar_ocorrencia_por_id():

    print("\nBuscando ocorrência por ID")

    search = input("Digite o ID: ")

    resultado = arvore_ids.buscar(search)

    historico_acoes.append({
        'acoes': 'buscar_id',
        'termo': search
    })

    if resultado is None:
        print("Ocorrência não encontrada.")

    else:

        print("Ocorrência encontrada:")

        print(
            f"ID: {resultado['id']} | "
            f"Nome: {resultado['nome']} | "
            f"Tipo: {resultado['tipo']} | "
            f"Descrição: {resultado['descricao']} | "
            f"Prioridade: {resultado['prioridade']} | "
            f"Status: {resultado['status']}"
        )

def buscar_por_nome():
  nome = input("Nome: ").lower()
  resultado = indice_nome.get(nome, [])

  if not resultado:
    print("Nenhuma ocorrencia encontrada.")
    return

  for o in resultado:
    print(
        f"{o['id']} |"
        f"{o['nome']} |"
        f"{o['tipo']} |"
    )

def buscar_por_tipo():
  tipo = input("Tipo: ").lower()
  resultado = indice_tipo.get(tipo, [])

  if not resultado:
    print("Nenhuma ocorrencia encontrada.")
    return
  
  for o in resultado:
    print(
        f"{o['id']} |"
        f"{o['nome']} |"
        f"{o['tipo']}"
    )

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if int(arr[j]['prioridade']) < int(arr[j + 1]['prioridade']):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def ordenar_ocorrencia():
    prev_order = [o['id'] for o in ocorrencia_lista_abertas]

    bubble_sort(ocorrencia_lista_abertas)

    historico_acoes.append({
        'acoes': 'ordenar',
        'prev_order': prev_order
    })
    print("Ocorrências ordenadas por prioridade.")
    print(ocorrencia_lista)

def indexar_ocorrencia(ocorrencia):
  nome = ocorrencia["nome"].lower()

  if nome not in indice_nome:
      indice_nome[nome] = []
  indice_nome[nome].append(ocorrencia)

  tipo = ocorrencia["tipo"].lower()

  if tipo not in indice_tipo:
      indice_tipo[tipo] = []
  indice_tipo[tipo].append(ocorrencia)


def historico():

    print("\n===== HISTÓRICO =====")

    if not historico_acoes:
        print("Nenhuma ação registrada.")
        return

    for i, h in enumerate(historico_acoes, start=1):

        ac = h["acoes"]

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

        elif ac == "buscar_nome_tipo":
            print(
                f"{i}. Busca por nome ou tipo - "
                f"{h['termo']}"
            )

def desfazer():

    print("\n===== DESFAZER =====")

    if not historico_acoes:
        print("Nenhuma ação para desfazer.")
        return

    h = historico_acoes.pop()

    ac = h["acoes"]

    if ac == "cadastrar":

        id_remover = h["ocorrencia"]["id"]

        idx = encontrar_id(id_remover)

        if idx is not None:
            ocorrencia_lista_abertas.pop(idx)

        print(
            f"Cadastro da ocorrência "
            f"{id_remover} desfeito."
        )

    elif ac in (
        "atender_fila",
        "atender_prioridade"
    ):

        oc_original = h["ocorrencia"]

        for i, oc_fechada in enumerate(ocorrencia_lista_fechadas):
            if oc_fechada['id'] == oc_original['id']:
                removed_oc = ocorrencia_lista_fechadas.pop(i)
                removed_oc['status'] = 'Aberto'

                try:
                    ocorrencia_lista_abertas.insert(h['index'], removed_oc)
                except IndexError:
                    ocorrencia_lista_abertas.append(removed_oc)
                print(
                    f"Atendimento da ocorrência "
                    f"{oc_original['id']} desfeito."
                )
                return
        print(f"Não foi possível desfazer atendimento da ocorrência {oc_original['id']} (não encontrada na lista de fechadas).")


    elif ac == "ordenar":

        prev = h["prev_order"]

        mapa = {
            o['id']: o
            for o in ocorrencia_lista_abertas
        }

        restaurada = []

        for id_ in prev:
            if id_ in mapa:
                restaurada.append(mapa[id_])

        ocorrencia_lista_abertas.clear()
        ocorrencia_lista_abertas.extend(restaurada)

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
    global ordem_chegada_counter

    while True:

        print("\nMENU")
        print("1. Cadastrar ocorrencia")
        print("2. Listar ocorrencias")
        print("2.1. Listar ocorrencias abertas")
        print("2.2. Listar ocorrencias fechadas")
        print("3. Atender próxima ocorrencia pela fila")
        print("4. Atender ocorrencia de maior prioridade")
        print("5. Buscar ocorrencia por ID")
        print("6.1. Buscar ocorrencias por nome")
        print("6.2. Buscar ocorrencias por tipo")
        print("7. Ordenar ocorrencias")
        print("8. Ver historico de acoes")
        print("9. Desfazer ultima acao")
        print("0. Sair")

        op = input("Selecione a opcao: ")

        if op == "1":

            print("*" * 20)
            print("CADASTRAR OCORRÊNCIA")
            print("*" * 20)

            nome = input(
                "Nome: "
            )

            tipo = input(
                "Tipo: "
            )

            descricao = input(
                "Descricao: "
            )

            prioridade = input(
                "Prioridade: "
            )

            ordem_chegada_counter += 1

            status = "Aberto"

            ocorrencia = {
                'id': gerar_id(),
                'nome': nome,
                'tipo': tipo,
                'descricao': descricao,
                'prioridade': prioridade,
                'ordem_chegada': ordem_chegada_counter,
                'status': status
            }


            cadastra_ocorrencia(
                ocorrencia_lista,
                ocorrencia_lista_abertas,
                ocorrencia
            )

            indexar_ocorrencia(ocorrencia)

            heapq.heappush(
                heap_prioridades,
                (
                    -int(prioridade),
                    ordem_chegada_counter,
                    ocorrencia
                )
            )

            print("Ocorrência cadastrada!")

        elif op == "2":
          listar_ocorrencias()

        elif op == "2.1":

            listar_ocorrencias_abertas()

        elif op == "2.2":

            listar_ocorrencias_fechadas()

        elif op == "3":

            atender_proxima_ocorrencia()

        elif op == "4":

            atender_ocorrencia_de_maior_prioridade()

        elif op == "5":

            buscar_ocorrencia_por_id()

        elif op == "6.1":

            buscar_por_nome()

        elif op == "6.2":
            buscar_por_tipo()

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