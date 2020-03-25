#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import random
import statistics
from Utils import plot_graph

class Grafo:
    matriz_Adj = []
    def __init__(self, _num_Vertices, _prob, random=False, _orientado=False):
        self.num_Vertices = _num_Vertices
        self.orientado = _orientado
        self.zeros_Matriz(self.num_Vertices)
        if random:
                self.random_Graph(_prob)
        else:
            pass
    def zeros_Matriz(self, _num_Vertices):
        """
        @Brief:     Inicializa a matriz de acordo com o número de vértices passados
        @param:     {_num_Vertices} Números de vértices da matriz
        """
        for _ in range(_num_Vertices):
            linha = []
            for _ in range(_num_Vertices):
                linha.append(0)
            self.matriz_Adj.append(linha)

    def insert_Aresta(self, _start, _end):
        """
        @Brief:     Iseri uma aresta na matriz de adjacência
        @param:     {_start} Posição incial da aresta
        @param:     {_end} Posição final da 
        """
        if _start == _end:
            pass
        else:
            self.matriz_Adj[_start][_end] = 1
            if not self.orientado:
                self.matriz_Adj[_end][_start] = 1

    def remove_Aresta(self, _start, _end):
        """
        @Brief:     Remove uma aresta da matriz de adjacências
        @param:     {_start} Posição inicial da remoção
        @param:     {_end} Posição final da remoção
        """
        self.matriz_Adj[_start][_end] = 0
        if not self.orientado:
            self.matriz_Adj[_end][_start] = 0

    def print_MatrizAdj(self):
        """
        @Brief:     Printa a matriz de adjacência
        """
        for i in range(self.num_Vertices):
            print(self.matriz_Adj[i])

    def random_Graph(self, _prob):
        """
        @Brief:     Gera um grafo aleatório
        @param:     {_prob} Probabilidade de conexão entre nós
        """
        for iterator1 in range(self.num_Vertices):
            for iterator2 in range(self.num_Vertices):
                if iterator1 < iterator2:
                    randomNumber = random.random()
                    # print(randomNumber)
                    if randomNumber <= _prob:
                        self.insert_Aresta(iterator1, iterator2)
            
    def sum_Matriz(self):
        """
        @Brief:     Soma as linhas da matriz de adjacêcia, retornando um vetor com o grau de cada nó
        """
        array = [0]*self.num_Vertices
        for iterator1 in range(self.num_Vertices):
            for iterator2 in range(self.num_Vertices):
                if self.matriz_Adj[iterator1][iterator2] == 1:
                    array[iterator1] += 1
        return array

g1 = Grafo(10000, 0.1, random=True)
# g1.print_MatrizAdj()
array = g1.sum_Matriz()
print(statistics.mean(array))
plot_graph(array)
# print(array)
# print(statistics.mean(array))

