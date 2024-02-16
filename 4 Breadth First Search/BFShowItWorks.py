def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
      m = queue.pop(0)
      print (m, end = " ")

      for neighbour in graph[m]:
          if neighbour not in visited:
              visited.append(neighbour)
              queue.append(neighbour)


#USE BFS

graph = {
    '5' : ['3', '4', '7'],
    '3' : ['2'],
    '4' : ['8'],
    '7' : ['8'],
    '2' : ['9'],
    '8' : [],
    '9' : []
    }
visited = []
queue = []

print('Following is the breadth first search for node 5')
bfs(visited, graph, '5')
