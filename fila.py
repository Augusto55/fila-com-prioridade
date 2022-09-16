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
            hp = []
            for e in self.fila_prioridade:
                hp.append((e[1], e[0], e[2]))

            heapq.heapify(hp)
            while hp:
                y = heapq.heappop(hp)
                self.lista_heap.append([y[1], y[0], e[2]])
            print(self.lista_heap)


heap = Heap()

heap.definir_tamanho(3)
heap.inserir_grupo([1, 2, "Augusto"])
heap.inserir_grupo([2, 2, "Arbusto"])
heap.inserir_grupo([1, 3, "Arbusto"])
heap.inserir_grupo([1, 3, "Asadusto"])
heap.gerar_lista()

#print(heap.fila_prioridade)
