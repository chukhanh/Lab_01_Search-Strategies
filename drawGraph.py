import readfile as read
import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import path as p



def drawGraph():
    plt.figure(figsize=(5, 5))
    A = read.read_graph(p.path())
    adjacencyMatrix = np.matrix(A)
    graph = nx.from_numpy_matrix(adjacencyMatrix, create_using=nx.MultiDiGraph())
    graph.edges(data=True)
    pos = nx.shell_layout(graph)
    nx.draw(graph, with_labels=True)
    plt.show()
