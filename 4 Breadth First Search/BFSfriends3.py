# Friends Recommendation BFS
              
import basicBFS3

##############USE BFS##############
friends_already = ['Joe','Kathy', 'Dave', 'Mike', 'John', 'Sue', 'Linda']

graph = {
  'Jasper' : friends_already,
  'Joe' : ['Mike', 'Sue'],
  'Kathy' : ['Linda', 'John', 'Dave'],
  'Dave' : ['John', 'Tim'],
  'Mike' : ['Dave'],
  'John' : ['Alice', 'Courtney'],
  'Tim' : [],
   'Linda' : [],
  'Alice': ['Henry', 'George', 'Steve'],
  'Courtney' : [],
  'Sue' : ['Larry']
}

visited = []
queue = []
distance = {}
parent = {}
source = 'Jasper'

print('Looking for friends for', source)
basicBFS3.bfs3(visited, graph, source, friends_already)
