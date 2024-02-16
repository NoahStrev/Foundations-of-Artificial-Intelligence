# MINOR REVISION TO SUIT THE APPLICATION -- CLOSEST ONE NON-FRIEND ALREADY

def bfs3(visited, graph, who, friends_already): #function for BFS
    queue = []     #Initialize a queue
    visited.append(who)
    queue.append(who)

    while queue:          # Creating loop to visit each node
      m = queue.pop(0)
      #    print (m, end = " ")
      # print ('Looking at ' + m, end = "...")
      if m != who:
          if (m not in friends_already)  :
              print (m + " is a friend suggestion for you!")
              break;  # FOUND ONE AND IT SHOULD BE AT THE CLOSEST LEVEL !!
        

      for neighbour in graph[m]:
          if neighbour not in visited:
              visited.append(neighbour)
              queue.append(neighbour)
