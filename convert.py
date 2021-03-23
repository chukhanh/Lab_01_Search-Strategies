
def convert_AdjMatrix_toDict(m):

    graph = {}
    for idx, row in enumerate(m):
        res = []
        for r in range(len(row)):
            if row[r] != 0:
                res.append(r)
            graph[idx] = res
    return graph

