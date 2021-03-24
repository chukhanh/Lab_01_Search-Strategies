import networkx as nx 
import numpy as np
import matplotlib.pyplot as plt
from collections import deque, defaultdict
import BFS as bfs
import DFS as dfs
import readfile as read
import drawGraph as draw
import convert as convert
import path as p
import re
import array as arr

matrix = read.read_graph(p.pathInput())
number = read.read_number_of_node(p.pathInput())
node = read.read_node(p.pathInput())
startNode = node[0]
goalNode = node[1]
option = node[2]

def switchCase(number):
    if number == 0:
        print("You use Breath-first search (BFS)")
        graph = convert.convert_AdjMatrix_toDict(matrix)
        print(graph)
        outputEdge = convert.convert_print_edge(matrix)
        print(outputEdge)
        output =  bfs.breadthFirst(graph, startNode, goalNode)
        print(output)

        Note = "The list of expanded nodes: \n"
        outputListOfNode = str(graph) + "\n"
        outputNote = "Find a path from node " + str(startNode) + " to node " + str(goalNode) + " using BFS" + "\n"
        outputFile = open(p.pathOutput(), "w")
        # outputFile.write(output)
        outputFile.writelines("Note: " + outputNote)
        outputFile.writelines("Edge: " + str(outputEdge) + "\n")
        outputFile.writelines(Note + outputListOfNode)
        outputFile.writelines("Result: " + str(output))
        outputFile.close()
        # print(bfs.breadthFirst(graph, startNode , goalNode))
        draw.drawGraph()
        print("End use Breath-first search (BFS)")

    if number == 1:
        print("You use Tree-search depth-first search (DFS):")
        print(matrix)
        outputEdge = convert.convert_print_edge(matrix)
        print(outputEdge)
        graph = convert.convert_AdjMatrix_toDict(matrix)
        print(graph)
        edge = convert.convert_AdjMatrix_EdgeLisT(matrix)
        print(edge)
        output =  dfs.DepthFirst(graph, startNode, goalNode)
        print(output)
        Note = "The list of expanded nodes: \n"
        outputListOfNode = str(graph) + "\n"
        outputNote = "Find a path from node " + str(startNode) + " to node " + str(goalNode) + " using BFS" + "\n"
        outputFile = open(p.pathOutput(), "w")
        # outputFile.write(output)
        outputFile.writelines("Note: " + outputNote)
        outputFile.writelines("Edge: " + str(outputEdge) + "\n")
        outputFile.writelines(Note + outputListOfNode)
        outputFile.writelines("Result: " + str(output))
        outputFile.close()
        # print(bfs.breadthFirst(graph, startNode , goalNode))
        draw.drawGraph()
        print("End use Tree-search depth-first search (DFS):")
    
    if number == 2:
        # graph = convert.convert_AdjMatrix_EdgeLisT(matrix)
        graph = convert.convert_print_edgeWeight(matrix)
        print(graph)


        
        
        