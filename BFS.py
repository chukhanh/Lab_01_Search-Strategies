
def breadthFirst(graph, start, end):
    explored = []
    # keep track of all the paths to be checked
    queue = [[start]]
 
    # return path if start is end
    if start == end:
        return "That was easy! Start = end"
 
    # keeps looping until all possible paths have been checked
    while queue:
        # pop the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        if node not in explored:
            neighbours = graph[node]
            # go through all neighbour nodes, construct a new path and
            # push it into the queue
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # return path if neighbour is end
                if neighbour == end:
                    return new_path
 
            # mark node as explored
            explored.append(node)



