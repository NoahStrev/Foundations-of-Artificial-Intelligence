#The sample network:

# Python builds tree using Dictionary and traverses DFS
# btw graph below is represented as an "adjacency" list (ie adjacent nodes)

import courses_and_prereqs

graph = courses_and_prereqs.graph.copy()

schedule = [] #application is calling for a scheduele

visited = []

#Basic DFS code:

def dfs(visited, graph, node, schedule): #function for DFS
    if node not in visited:
        visited.append(node)
        for connected_node  in graph[node]:
            dfs(visited,graph, connected_node, schedule)
            if connected_node not in schedule :
                schedule.append(connected_node)
    return visited

#Graduate is the goal so Complete the Major is top node
dfs(visited, graph, 'Complete Major', schedule)
print('Schedule is :', schedule)
print()
print('As an FYI nodes were visited in this order:', visited)
