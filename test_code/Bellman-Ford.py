graph = {
    'A':{'B':-1, 'C':4},
    'B':{'C':3, 'D':2, 'E':2},
    'C':{},
    'D':{'B':1, 'C':5},
    'E':{'D':-3}
}

def bellman_ford(graph, start):
    distance = dict()
    for node in graph:
        distance[node] = float('inf')
    distance[start]=0

    for i in range(len(graph)-1):
        for node in graph:
            for neighbor in graph[node]:
                 if distance[neighbor] > distance[node] + graph[node][neighbor]:
                     distance[neighbor] = distance[node] + graph[node][neighbor]

    for node in graph:
        for neighbor in graph[node]:
            if distance[neighbor] > distance[node] + graph[node][neighbor]:
                return -1
    return distance

print(bellman_ford(graph, 'A'))