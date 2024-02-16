def bfs2(visited, graph, node, friends_already): #function for BFS
    queue = []     #Initialize a queue
    
    visited.append(node)
    queue.append(node)

    while queue:          # Creating loop to visit each node
      m = queue.pop(0)
      #    print (m, end = " ")
      print ('Looking at ' + m, end = "...")
 #     if m not in friends_already:
      if (m not in friends_already)  :
          print (m + " is a friend suggestion for you!")
      else:
          print (" already your friend!")
      

      for neighbour in graph[m]:
          if neighbour not in visited:
              visited.append(neighbour)
              queue.append(neighbour)

