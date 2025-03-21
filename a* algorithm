from heapq import heappop, heappush

def astar(graph, start, goal, h):
    pq, visited = [(h[start], 0, start, [])], set()
    
    while pq:
        _, cost, node, path = heappop(pq)
        if node in visited: continue
        path.append(node)
        if node == goal: return path, cost
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                heappush(pq, (cost + weight + h[neighbor], cost + weight, neighbor, path[:]))

graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1}}
h = {'A': 7, 'B': 6, 'C': 2, 'D': 0}
print(astar(graph, 'A', 'D', h))
