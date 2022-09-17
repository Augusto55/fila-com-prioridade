import heapq
import random
import names
from os import curdir

class Heap:
    def __init__(self):
        self.fila_prioridade = []
        self.fila = []
        self.lista_heap = []
        self.tamanho = 0
        self.fila_preparo = []
    
    def definir_tamanho(self, tamanho):
        self.fila_prioridade = [None] * tamanho
        self.tamanho = tamanho

    def inserir_grupo(self, grupo):
        for i in range(len(self.fila_prioridade)):
            if self.fila_prioridade[i] == None:
                self.fila_prioridade[i] = grupo
                break
            elif self.fila_prioridade.count(None) == 0:
                print("Numero de pedidos maximos excedidos.")
                break
    
    def gerar_lista(self):
        if self.fila_prioridade.count(None) == len(self.fila_prioridade):
            print("Nenhum pedido na fila.")
        else:
            for i in range(len(self.fila_prioridade)):
                heapq.heapify(self.fila_prioridade)
                y = self.fila_prioridade.pop(0)
                self.lista_heap.append(y)

    def mostrar_prox_pedido(self):
        self.gerar_lista()
        index = self.lista_heap[0]
        print("Quantidade de pessoas do pedido: " + str(index[0]) + " pessoas \nTempo de preparo: " + str(index[1]) +
        " minutos \nNome da reserva: " + str(index[2]))

    def preparar_prox_ref(self):
        self.gerar_lista()
        index = self.lista_heap[0]
        tempo = self.calcular_tempo_fila2() + index[1]
        print("Nome do pedido : " + index[2] + "\nTempo de espera estimado para o preparo: " + str(tempo))
        y = self.lista_heap.pop(0)
        self.fila_preparo.append(y)

    def calcular_tempo_fila2(self):
        tempo = 0
        for i in range(len(self.fila_preparo)):
            tempo += self.fila_preparo[i][1]
        return tempo

    def entregar_refeição(self):
        grupo = self.fila_preparo[0][2]
        self.fila_preparo.pop(0)
        print("Grupo: " + grupo + "\nSeu pedido está pronto!")

    def gerar_simulacao(self):
        integer = random.randint(1,10)
        self.definir_tamanho(integer)
        for i in range(integer):
            n_pessoas = random.randint(1, 10)
            tempo = random.randint(5, 50)
            nome = names.get_first_name()
            self.inserir_grupo((n_pessoas, tempo, nome))
        self.gerar_lista()
        print("Simulação gerada com sucesso!")






heap = Heap()


while True:    
    try:
        insertion = int(input('\n[1] Informar o número máximo de pedidos\n[2] Adicionar novo pedido\n[3] Mostrar próximo pedido a ser preparado\n[4] Preparar próximo pedido\n[5] Entregar refeição\n[6] Gerar simulação\n[7] Encerrar o programa\nDIGITE O NUMERO DA OPÇÃO: '))
        if insertion == 1:
            integer = int(input("Digite o número máximo de pedidos:"))
            heap.definir_tamanho(integer)
        elif insertion == 2:
            pessoas = int(input("Insira o número de pessoas do pedido: "))
            tempo = int(input("Insira o tempo para preparar o pedido: "))
            nome = input("Insira o nome do grupo: ")
            heap.inserir_grupo((pessoas, tempo, nome))
        elif insertion == 3:
            try:
                heap.mostrar_prox_pedido()
            except IndexError:
                print("Nenhum pedido na fila de preparo")
        elif insertion == 4:
            heap.preparar_prox_ref()
        elif insertion == 5:
            try:
                heap.entregar_refeição()
            except IndexError:
                print("Nenhum pedido para ser entregue")
        elif insertion == 6:
            heap.gerar_simulacao()
        elif insertion == 7:
            break
        else:
            print("Opção inválida!")
    except ValueError:
        print("Opção inválida")




