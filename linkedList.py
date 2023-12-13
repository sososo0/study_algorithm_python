edges = [[0, 1], [0, 2], [1, 2], [2, 3], [2, 5], [3, 4], [3, 5]]
graph = [[] for _ in range(6)]

for a, b in edges:
    graph[a].append(b) 
    graph[b].append(a) 
    # 단 방향 graph 인 경우는 방향대로 1번만 append 한다.
    # 위의 경우는 양방향인 경우 
    
print(graph)