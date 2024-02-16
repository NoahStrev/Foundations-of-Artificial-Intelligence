# Friends Recommendation BFS
              
import basicBFS

##############USE BFS##############

graph = {
  'Jasper' : ['Joe','Kathy', 'Dave', 'Mike', 'Tim', 'Sue', 'Linda'],
  'Joe' : ['Mike', 'Sue'],
  'Kathy' : ['Linda', 'John', 'Dave'],
  'Dave' : ['John', 'Tim'],
  'Mike' : ['Dave'],
  'John' : ['Alice', 'Courtney'],
  'Tim' : [],
   'Linda' : [],
  'Alice': [],
  'Courtney' : [],
  'Sue' : []
}

visited = []
queue = []
distance = {}
parent = {}
source = 'Jasper'

basicBFS.bfs(visited, graph, source)
