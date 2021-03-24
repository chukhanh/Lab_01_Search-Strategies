import readfile as read
import switchCase as switch
import path as p

# path = "./input.txt"

def main():
    # print("let the user to choose either of the following strategies: ")
    # print("===================================================================")
    # print("0: Breath-first search (BFS)")
    # print("1: Tree-search depth-first search (DFS)")
    # print("2: Uniform-cost search (UCS)")
    # print("3: Iterative deepening search (IDS)")
    # print("4: Greedy best first search (GBFS)")
    # print("5: Graph-search A* (AStar)")
    # print("6: Hill-climbing (HC)")
    # print("===================================================================")

    matrix = read.read_graph(p.pathInput())
    number = read.read_number_of_node(p.pathInput())
    if len(matrix) <= int(number):
        node = read.read_node(p.pathInput())
        option = node[2]
        switch.switchCase(option)
    else:
        print("The total numbers are too large!") 


if __name__ == "__main__":
    main()