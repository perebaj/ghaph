#!/usr/bin/env python
# -*- coding: utf-8 -*-
from LinkedList import LinkedList
from Utils import binary_search, preferential_link, plot_graph, define_edges_link, plot_free_scale_graph
import random
import bisect
import matplotlib.pyplot as plt
import statistics
import math
import numpy as np
class graph:
    def __init__(self, _num_Nodes):
        self.listaAdj = []
        self.num_Nodes = _num_Nodes
        self.lista_Adicionados = []
        self.population = [0]*_num_Nodes
        for iterator in range(self.num_Nodes): self.population[iterator] = iterator        

    def init_Graph(self):
        self.lista_Adicionados = [[] for _ in range(self.num_Nodes)]
        self.listaAdj = [None]*self.num_Nodes
        for iterator1 in range(self.num_Nodes):
            self.listaAdj[iterator1] = LinkedList()

    def add_Aresta(self, vertice1, vertice2):
        if self.verify(vertice1, vertice2):
            bisect.insort(self.lista_Adicionados[vertice1], vertice2)
            bisect.insort(self.lista_Adicionados[vertice2], vertice1)
            self.listaAdj[vertice1].adiciona_Elemento_Inicio(vertice2)
            self.listaAdj[vertice2].adiciona_Elemento_Inicio(vertice1)
        # self.lista_Adicionados[vertice1].append(vertice2)
        # self.lista_Adicionados[vertice2].append(vertice1)


    def print_grapf(self):
        for iterator1 in range(self.num_Nodes):
            print(self.listaAdj[iterator1])

    def verify(self, vertice1, vertice2):
        if vertice1 == vertice2:
            return False
        #se vertice1 ou vertice2 estiverem na lista de adicionados, a aresta não é válida. Retornar Falso
        elif binary_search(self.lista_Adicionados[vertice1], 0, len(self.lista_Adicionados[vertice1]), vertice2) or binary_search(self.lista_Adicionados[vertice2], 0, len(self.lista_Adicionados[vertice2]), vertice1):
            return False
        return True

    def verify_Aresta(self, vertice1, vertice2):
      pointer = self.listaAdj[vertice1].head
      while(pointer):
          if pointer.data == vertice2:
              return False
          pointer = pointer.next
      return True 

    def random_Graph(self, _prob):
        for iterator1 in range(self.num_Nodes):
            for iterator2 in range(self.num_Nodes):
                if iterator1 < iterator2:
                    randomNumber = random.random()
                    if randomNumber <= _prob:
                        self.add_Aresta(iterator1, iterator2)

    def grau_nodes(self):
        array = [0]*self.num_Nodes
        for iterator in range(self.num_Nodes):
            # array[iterator] = len(self.lista_Adicionados[iterator])
            array[iterator]  = self.listaAdj[iterator]._size
        return array

    def scale_free_graph(self,n, k):
        self.full_graph(n)
        edges = []
        for iterator in range(n,self.num_Nodes):
            edges = define_edges_link(self.population, self.grau_nodes(), k)
            self.add_Aresta(iterator,edges[0])
            self.add_Aresta(iterator,edges[1])

    def full_graph(self, _N):
        """
        @Brief: Dada certa quantidade de nós, N, preecher de 0-N de forma que todos os nós se liguem
        """
        for iterator1 in range(_N):
            for iterator2 in range(_N):
                if iterator1 < iterator2:
                    self.add_Aresta(iterator1, iterator2)
        
            
  

Grafo = graph(1000)
Grafo.init_Graph()
Grafo.scale_free_graph(6,3)
array = Grafo.grau_nodes()
plot_free_scale_graph(array)




