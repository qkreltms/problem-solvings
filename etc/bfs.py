# sample graph implemented as a dictionary
# graph = {'A': ['B', 'C', 'E'],
#          'B': ['A','D', 'E'],
#          'C': ['A', 'F', 'G'],
#          'D': ['B'],
#          'E': ['A', 'B','D'],
#          'F': ['C'],
#          'G': ['C']}
graph = {'A': ['C'],
         'B': ['D', 'E'],
         'C': ['A', 'F'],
         'D': ['B'],
         'E': ['B', 'F'],
         'F': ['C', 'E']}

# visits all the nodes of a graph (connected component) using BFS
def bfs_connected_component(graph, start):
    # keep track of all visited nodes
    explored = []
    # keep track of nodes to be checked
    queue = [start]

    levels = {}         # this dict keeps track of levels
    levels[start]= 0    # depth of start node is 0

    visited= [start]     # to avoid inserting the same node twice into the queue

    # keep looping until there are nodes still to be checked
    while queue:
       # pop shallowest node (first node) from queue
        node = queue.pop(0)
        explored.append(node)
        neighbours = graph[node]

        # add neighbours of node to queue
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

                levels[neighbour]= levels[node]+1
                print(neighbour, ">>", levels[neighbour])

    print(levels)

    return explored

ans = bfs_connected_component(graph,'A') # returns ['A', 'B', 'C', 'E', 'D', 'F', 'G']
print(ans)