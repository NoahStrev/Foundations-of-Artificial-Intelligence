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
  'The Commons' : ['PG Building', 'Alumni Hall', 'The Eates'],
  'PG Building' : ['Astra Building', 'Alumni Hall'],
  'The Eates' : ['Howe Hall'],
  'Astra Building' : ['Sports Center'],
  'Alumni Hall' : ['Howe Hall'],
  'Howe Hall' : [],
  'Sports Center' : []
}

visited = []
queue = []
distance = {}
parent = {}
source = 'The Commons'

print('Following is the breadth first search for node 5')
bfs(visited, graph, source)

#print the distances
print()
for d in distance :
    print('distance from ', source, 'to', d, 'is', distance[d], 'Immediate parent is ', parent[d])

print()
dest = 'Howe Hall'
print('Get to',dest)

while True:
    dest = parent[dest]
    print('from',dest)
    if dest == source:
        break
