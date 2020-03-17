
from linkedlist import LinkedList
import random
class Grafo:
    matriz_Adj  = []
    lista_Adj   = []
    def __init__(self, _num_Vertices, _prob, random=False, _orientado=False, _lista = False):
        self.num_Vertices = _num_Vertices
        self.orientado = _orientado
        if not _lista:
            self.zeros_Matriz(self.num_Vertices)
            if random:
                self.random_Graph(_prob)
        else:
            self.graph_Lista()

    def zeros_Matriz(self, _num_Vertices):
        for _ in range(_num_Vertices):
            linha = []
            for _ in range(_num_Vertices):
                linha.append(0)
            self.matriz_Adj.append(linha)

    def insert_Aresta(self, _start, _end):
        if _start == _end:
            pass
        elif self.matriz_Adj[_start][_end] == 1 or self.matriz_Adj[_end][_start] == 1:
            print("ja existe")
        else:
            self.matriz_Adj[_start][_end] = 1
            if not self.orientado:
                self.matriz_Adj[_end][_start] = 1

    def remove_Aresta(self, _start, _end):
        self.matriz_Adj[_start][_end] = 0
        if not self.orientado:
            self.matriz_Adj[_end][_start] = 0

    def print_MatrizAdj(self):
        for i in range(self.num_Vertices):
            print(self.matriz_Adj[i])

    def random_Graph(self, _prob):
        for iterator1 in range(self.num_Vertices):
            for iterator2 in range(self.num_Vertices):
                ramdom = random.random()
            if ramdom <= _prob:
                self.insert_Aresta(iterator1, iterator2)

    def graph_Lista(self):
        lista_Adj = [None]*5
        for i in range(5):
            lista_Adj[i] = LinkedList()
    
    def inset_GraphList(self, _start, _end, _element):
        

# g1 = Grafo(5, 0.2, random=True)
# g1.insert_Aresta(0, 1)
# g1.print_MatrizAdj()
