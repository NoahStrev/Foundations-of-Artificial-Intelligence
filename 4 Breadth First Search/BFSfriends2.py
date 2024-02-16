# Friends Recommendation BFS
              
import basicBFS2

##############USE BFS##############
friends_already = ['Joe','Kathy', 'Dave', 'Mike', 'Tim', 'Sue', 'Linda']

graph = {
  'Jasper' : friends_already,
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

print('Looking for friends for', source)
basicBFS2.bfs2(visited, graph, source, friends_already)
