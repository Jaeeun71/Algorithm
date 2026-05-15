from collections import deque

def solution(n, edge):
    
    graph = [[] for _ in range(n + 1)]
    for a, b in edge:
        graph[a].append(b)
        graph[b].append(a)
    
    distances = [-1] * (n + 1)
    distances[1] = 0
    

    queue = deque([1])
    while queue:
        curr = queue.popleft()
        for neighbor in graph[curr]:
            if distances[neighbor] == -1: # 미방문 노드
                distances[neighbor] = distances[curr] + 1
                queue.append(neighbor)
                

    max_dist = max(distances)
    return distances.count(max_dist)