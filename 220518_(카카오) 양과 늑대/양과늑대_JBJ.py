import collections
def solution(info, edges):
    graph = collections.defaultdict(set)
    for a, b in edges:
        graph[a].add(b)
        graph[b].add(a)
    
    visited = [[-1]*(1<<17) for _ in range(17)] # contains # of sheeps.
    def dfs(cur_node, cur_graph):
        nonlocal graph, visited, info
        
        if visited[cur_node][cur_graph] != -1: # already made the graph and counted sheeps.
            return visited[cur_node][cur_graph]
        
        sheeps, wolves = 0, 0 # count sheeps and wolves.
        for node in range(17):
            if cur_graph & (1<<node): # the node is in the graph.
                if info[node] == 0: 
                    sheeps += 1
                else:
                    wolves += 1
        
        if sheeps <= wolves: # wolves eat sheeps -> no sheeps.
            return 0 
        else: # sheeps can survive -> count sheeps.
            visited[cur_node][cur_graph] = sheeps
        
        for adj_node in graph[cur_node]: # make new graphs.
            sheeps = max(sheeps, dfs(adj_node, cur_graph | (1 << adj_node)))
        
        return sheeps
        
    return dfs(0, 1)