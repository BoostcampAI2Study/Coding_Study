from collections import defaultdict, deque
def solution(n, path, order):
    graph = defaultdict(list)
    for n1, n2 in path:
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    # 단방향 그래프 생성
    dir_graph = defaultdict(list)
    indegree = [0] * n
    
    q = deque()
    q.append(0)
    visit = [False] * n
    visit[0] = True
    
    while q:
        node = q.popleft()
        for next_node in graph[node]:
            if not visit[next_node]:
                q.append(next_node)
                indegree[next_node] += 1
                dir_graph[node].append(next_node)
                visit[next_node] = True
    
    for n1, n2 in order:
        dir_graph[n1].append(n2)
        indegree[n2] += 1
    
    # 위상정렬
    cnt = 0
    q.append(0)
    while q:
        node = q.popleft()
        cnt += 1
        for next_node in dir_graph[node]:
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                q.append(next_node)
    
    return True if cnt == n else False
