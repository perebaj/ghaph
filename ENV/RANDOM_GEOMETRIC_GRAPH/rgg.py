import networkx as nx
import statistics 
from Utils import plot_free_scale_graph, plot_graph

size = 10000
random_geometric = nx.random_geometric_graph(size, 0.199)

nd_view = random_geometric.degree()
# print(nd_view)

degrees = []
for iterator in range(size): degrees.append(nd_view[iterator])
# print(degrees)
print(statistics.mean(degrees))
plot_graph(degrees)