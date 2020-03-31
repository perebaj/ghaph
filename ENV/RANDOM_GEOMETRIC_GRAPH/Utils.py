#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np

def plot_graph(array):
    plt.xlabel("Grau")
    plt.ylabel("Frequência")
    plt.title("Distribuição de Graus")
    minvalue = np.min(array)
    maxvalue = np.max(array)
    bins = np.arange(minvalue, maxvalue + 2) #número de caixas que o histograma vai comportar
    # print(bins)
    plt.hist(array, bins,density=True, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.show()


def plot_free_scale_graph(array):
    number_of_connections, frequency = np.unique(array, return_counts=True)
    plt.style.use("ggplot")
    plt.xscale("log")
    # plt.yscale("log")
    plt.xlabel("Número de conexões log(x)")
    plt.ylabel("Frequência")
    plt.title("Distribuição de Graus - Scale Free Graph")
    plt.plot(number_of_connections, frequency, "^", color="C12", alpha=1)
    plt.grid(True)
    # regression_line(number_of_connections, frequency)
    plt.show()

def regression_line(x,y):
    coef_linear, coef_angu = np.polyfit(x,y,1)
    print(coef_linear,coef_angu)
    plt.plot(x, coef_angu*x + coef_linear)
    plt.show()