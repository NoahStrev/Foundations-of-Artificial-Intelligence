def bfs(visited, graph, node): #function for BFS
    visited.append(node)
    queue.append(node)
    #For determining distance
    distance[node] = 0
    parent[node] = node

    while queue:          # Creating loop to visit each node
      m = queue.pop(0)
      print (m, end = " ")

      for neighbour in graph[m]:
          if neighbour not in visited:
              visited.append(neighbour)
              distance[neighbour] = distance[m] + 1
              parent[neighbour] = m
              queue.append(neighbour)
              


##############USE BFS##############

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
distance = {}
parent = {}

print('Following is the breadth first search for node 5')
bfs(visited, graph, '5')

#print the distances
print()
source = '5'
for d in distance :
    print('distance from ', source, 'to', d, 'is', distance[d], 'Immediate parent is ', parent[d])
