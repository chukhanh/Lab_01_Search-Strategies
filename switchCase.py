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

matrix = read.read_graph(p.path())
number = read.read_number_of_node(p.path())
node = read.read_node(p.path())
startNode = node[0]
goalNode = node[1]
option = node[2]

def switchCase(number):
    if number == 0:
        print("You use Breath-first search (BFS)")
        graph = convert.convert_AdjMatrix_toDict(matrix)
        print(graph)
        output =  bfs.breadthFirst(graph, startNode, goalNode)
        print(output)
        Note = "The list of expanded nodes: \n"
        outputListOfNode = str(graph) + "\n"
        outputNote = "Find a path from node " + str(startNode) + " to node " + str(goalNode) + " using BFS" + "\n"
        outputFile = open("./output.txt", "w")
        # outputFile.write(output)
        outputFile.writelines("Note: " + outputNote)
        outputFile.writelines(Note + outputListOfNode)
        outputFile.writelines("Result: " + str(output))
        outputFile.close()
        # print(bfs.breadthFirst(graph, startNode , goalNode))
        # draw.drawGraph()
        print("End use Breath-first search (BFS)")
    if number == 1:
        print("You use Tree-search depth-first search (DFS):")
        graph = convert.convert_AdjMatrix_toDict(matrix)
        print(graph)
        output =  dfs.DepthFirst(graph, startNode, goalNode)
        print(output)
        Note = "The list of expanded nodes: \n"
        outputListOfNode = str(graph) + "\n"
        outputNote = "Find a path from node " + str(startNode) + " to node " + str(goalNode) + " using BFS" + "\n"
        outputFile = open("./output.txt", "w")
        # outputFile.write(output)
        outputFile.writelines("Note: " + outputNote)
        outputFile.writelines(Note + outputListOfNode)
        outputFile.writelines("Result: " + str(output))
        outputFile.close()
        # print(bfs.breadthFirst(graph, startNode , goalNode))
        # draw.drawGraph()
        print("End use Tree-search depth-first search (DFS):")