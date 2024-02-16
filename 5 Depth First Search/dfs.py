#The sample network:

# Python builds tree using Dictionary and traverses DFS
# btw graph below is represented as an "adjacency" list (ie adjacent nodes)

graph = {
  '5' : ['3', '4', '7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : ['9'],
  '4' : ['8'],
  '8' : ['7'],
  '9' : []
}

visited = []

#Basic DFS code:

def dfs(visited, graph, node): #function for DFS
    if node not in visited:
        visited.append(node)
        for connected_node  in graph[node]:
            dfs(visited,graph, connected_node)
    return visited

print('Following a depth first search')
dfs(visited, graph, '5')
print(visited)
