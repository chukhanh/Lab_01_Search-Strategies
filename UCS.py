from queue import PriorityQueue

def create_graph_ucs(m):
    graph = {}
    for lines in range(len(m)):
        for line in range(len(m[lines])):
            node_A = m[lines][0]
            node_B = m[lines][1]
            weight = m[lines][2]
            graph.setdefault(node_A, []).append((node_B, weight))
            graph.setdefault(node_B, []).append((node_A, weight))


def UCS_search(graph, source, destination):
    visited = set()
    path = []
    queue = PriorityQueue()
    queue.put((0, [source]))

    while queue:
        # if no path is present beteween two nodes 	
        if queue.empty():
            print('distance: infinity\nroute: \nnone')
            return
        cost, path = queue.get()
        node = path[len(path)-1]
        if node not in visited:
            visited.add(node)
            if node == destination:
                path.append(cost)
                return path
            
            for n in neighbors(graph, node):
                if n not in visited:
                    t_cost = cost + int(find_cost(graph, node, n))
                    temp = path[:]
                    temp.append(n)
                    queue.put((t_cost, temp))

# function for finding neighbors in the graph
def neighbors(graph, node):
	points = graph[node]
	return [n[0] for n in points]

# function to calculate the cost of path beteween two nodes
def find_cost(graph, node_A, node_B):
	location = [n[0] for n in graph[node_A]].index(node_B)
	return graph[node_A][location][1]

# output the result of search
def display_path(graph, path):
	distance = path[-1]
	print('distance: '+ str(distance) + ' km')
	print('route: ')
	for p in path[:-2]:
		q = path.index(p)
		location = [r[0] for r in graph[p]].index(path[q+1])
		cost = graph[p][location][1]
		print(p + ' to ' + path[q+1] + ', ' + cost + ' km')
