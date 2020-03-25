#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import matplotlib.pyplot as plt
import numpy as np
def binary_search(array, left, right, elem):
    if right <= left:
        return False
    mid =  (left + right) // 2
    if array[mid] == elem:
        return True
    elif array[mid] > elem:
        return binary_search(array, left, mid - 1, elem)
    else:
        return binary_search(array, mid + 1, right, elem)

def preferential_link(population, array_weight):
    """
    @BRIEF: Retorna o valor de uma população baseado em uma distribuição de probabilidade
    @param:   {array_weight}    lista com pesos/probabilidade de cada elemento da população
    @param:     {population}    Representa cada vértice da minha listaAdj
    @param:             {_k}            Número de valores que serão retornados
    @return valor escolhido de acordo com os pesos
    """
    link = random.choices(population, array_weight, k = 1)
    return link[0]

def plot_graph(array):
    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    plt.title("Distribuição de Graus")
    minvalue = np.min(array)
    maxvalue = np.max(array)
    bins = np.arange(minvalue, maxvalue + 2)
    plt.hist(array, bins,density=True, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()

def define_edges_link(population, weight, _k):
    edges = []
    edges.append(preferential_link(population, weight))
    for _ in range(_k -1):
        edge1 = preferential_link(population, weight)
        while edge1 in edges:
            edge1 = preferential_link(population, weight)
        edges.append(edge1)
    return edges

def plot_free_scale_graph(array):
    number_of_connections, frequency = np.unique(array, return_counts=True)
    plt.style.use("ggplot")
    plt.xscale("log")
    # plt.yscale("log")
    plt.xlabel("Número de conexões")
    plt.ylabel("Frequência log(x)")
    plt.title("Distribuição de Graus - scale-free-graph")
    plt.plot(number_of_connections, frequency, "^", color="C12", alpha=1)
    plt.grid(True)
    # regression_line(number_of_connections, frequency)
    plt.show()

def regression_line(x,y):
    coef_linear, coef_angu = np.polyfit(x,y,1)
    print(coef_linear,coef_angu)
    plt.plot(x, coef_angu*x + coef_linear)
    plt.show()