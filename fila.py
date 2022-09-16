import heapq

class Heap:
    def __init__(self):
        self.fila_prioridade = []
        self.fila = []
        self.lista_heap = []
        self.tamanho = 0
    
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
        print(self.lista_heap)

    def mostrar_prox_pedido(self):
        index = self.lista_heap[0]
        print("Quantidade de pessoas do pedido: " + str(index[0]) + " pessoas \nTempo de preparo: " + str(index[1]) +
        " minutos \nNome da reserva: " + str(index[2]))

    

heap = Heap()

heap.definir_tamanho(5)
heap.inserir_grupo((1, 20, "Augusto"))
heap.inserir_grupo((2, 30, "Arbusto"))
heap.inserir_grupo((1, 45, "Arbusto"))
heap.inserir_grupo((2, 15, "SAAAD"))
heap.inserir_grupo((3, 10, "UAAAAU"))
heap.gerar_lista()
heap.mostrar_prox_pedido()


