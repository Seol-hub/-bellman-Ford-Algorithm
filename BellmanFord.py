# bellman Ford Algorithm
from collections import deque

def bellman_Ford(graph, start):
    distances = {i: float('inf') for i in graph}
    distances[start] = 0

    from_node = {i: None for i in graph}

    # 정점의 개수 -1 만큼 반복함
    for _ in range(len(graph)-1):
        for current_node in graph:
            for new_node, new_distance in graph[current_node]:
                distance = new_distance + distances[current_node]
                if distances[new_node] > distance:
                    distances[new_node] = distance
                    from_node[new_node] = current_node
    
    # 음수 사이클 판별
    for current_node in graph:
        for new_node, new_distance in graph[current_node]:
            if distances[new_node] > distances[current_node] + new_distance:
                return -1
    
    return distances, from_node

def findPath(from_node, start, goal):
    res = deque()
    node = goal
    while node != start:
        res.appendleft(node)
        node = from_node[node]
    res.appendleft(start)
    return res

graph = {
    'A': [('B', -1), ('C', 4)],
    'B': [('C', 3), ('D', 2), ('E', 2)],
    'C': [],
    'D': [('B', 1), ('C', 5)],
    'E': [('D', -3)]
}

distances, from_node = bellman_Ford(graph, 'A')
print(distances, from_node, sep='\n', end='\n')

path = findPath(from_node, 'A', 'E')
print('A -> E road:', end=' ')
for i in path:
    print(i, end=' ')
print()