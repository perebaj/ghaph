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
"""
@brief
@param 
@param
@param
@return
"""


class graph:
    def __init__(self, _num_Nodes):
        """
        @brief      Inicia o grafo com as variáveis essenciais para o seu funcionamento
        @param      {_num_Nodes} números de nós que a estrutura do grafo ira suportar
        """
        self.listaAdj = []  # lista de adjacência
        self.num_Nodes = _num_Nodes
        # lista com os vértices adicionados para verificação de combinações repitidas
        self.lista_Adicionados = []
        # vetor com tamanho de número de nós do grafo
        self.population = [0]*_num_Nodes
        for iterator in range(self.num_Nodes):
            self.population[iterator] = iterator

    def init_Graph(self):
        """
        @Brief:     Inicia lista de adjacência do grafo com tamanho correto, e determina que cada posição
        seja um lista encadeada
        """
        self.lista_Adicionados = [[] for _ in range(self.num_Nodes)]
        self.listaAdj = [None]*self.num_Nodes
        for iterator1 in range(self.num_Nodes):
            self.listaAdj[iterator1] = LinkedList()

    def add_Aresta(self, vertice1, vertice2):
        """
        @brief  verifica a validade da ligação das duas arestas e as adicionana estrutura do grafo
        @param  {vertice1}, {vertice2} vertices que vão ser ligados
        """
        if self.verify(vertice1, vertice2):
            bisect.insort(self.lista_Adicionados[vertice1], vertice2)
            bisect.insort(self.lista_Adicionados[vertice2], vertice1)
            self.listaAdj[vertice1].adiciona_Elemento_Inicio(vertice2)
            self.listaAdj[vertice2].adiciona_Elemento_Inicio(vertice1)

    def print_grapf(self):
        # Imprime o Grafo, cada linha é um elemento da lista encadeada, e os elementos são suas ligações
        #          _________    _________     _________     _________
        # head --> | 2 | --|--> | 1 | --|-->  | 5 | --|-->  | 3 | --|--> None
        #          ---------    ---------     ---------     ---------
        for iterator1 in range(self.num_Nodes):
            print(self.listaAdj[iterator1])

    def verify(self, vertice1, vertice2):
        """
        @brief  Verifica a validade da ligação dos vértices com busca binária na lista de adicionados
        @param {vertice1},{vertice2}:   
        """
        if vertice1 == vertice2:
            return False
        # se vertice1 ou vertice2 estiverem na lista de adicionados, a aresta não é válida. Retornar Falso
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
            array[iterator] = len(self.lista_Adicionados[iterator])
            # array[iterator] = self.listaAdj[iterator]._size
        return array

    def scale_free_graph(self, n, k):
        self.full_graph(n)
        edges = []
        for iterator in range(n, self.num_Nodes):
            edges = define_edges_link(self.population, self.grau_nodes(), k)
            self.add_Aresta(iterator, edges[0])
            self.add_Aresta(iterator, edges[1])

    def full_graph(self, _N):
        """
        @Brief: Dada certa quantidade de nós, N, preecher de 0-N de forma que todos os nós se liguem
        """
        for iterator1 in range(_N):
            for iterator2 in range(_N):
                if iterator1 < iterator2:
                    self.add_Aresta(iterator1, iterator2)


Grafo = graph(10000)
Grafo.init_Graph()
Grafo.random_Graph(0.1)
# Grafo.print_grapf()
# Grafo.scale_free_graph(6, 3)
array = Grafo.grau_nodes()
# print(array)
print(statistics.mean(array))
plot_graph(array)
# plot_free_scale_graph(array)



