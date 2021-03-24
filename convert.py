import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
import readfile as read
import path as p
import re

def convert_AdjMatrix_toDict(m):

    graph = {}
    for idx, row in enumerate(m):
        res = []
        for r in range(len(row)):
            if row[r] != 0:
                res.append(r)
            graph[idx] = res
    return graph

def convert_AdjMatrix_EdgeLisT(m):
    A = read.read_graph(p.pathInput())
    m = np.matrix(A)
    graph = nx.from_numpy_matrix(m, create_using=nx.DiGraph)
    labels = nx.get_edge_attributes(graph, "weight")
    return labels
    
def regexString(m):
    delw = "{"
    dela = "}"
    replace = ''
    regex = r"[(//d, //d)://d]"
    result = re.sub(delw, replace ,str(m))
    result = re.sub(dela, replace, result)
    string = re.sub(regex, replace, result, 0, re.MULTILINE)
    return string

def devide(m):
    n = int(len(m) / 3)
    avg = len(m) / n
    out = []
    last = 0.0

    while last < len(m):
        out.append(m[int(last):int(last + avg)])
        last += avg

    return out


def convert_print_edge(m):
    graph = convert_AdjMatrix_EdgeLisT(m)
    string = regexString(graph)
    num_list = {int(x) for x in string}
    
    return num_list


def convert_print_edgeWeight(m):
    graph = convert_AdjMatrix_EdgeLisT(m)
    string = regexString(graph)
    edge_list = list(map(int, string))
    edgeWeight_list = devide(edge_list)
    return edgeWeight_list