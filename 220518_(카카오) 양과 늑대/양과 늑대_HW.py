from collections import defaultdict
answer = 1
def solution(info, edges):
    edge_info = defaultdict(list)
    for parent, child in edges:
        edge_info[parent].append(child)
        edge_info[child].append(parent)
    
    visited = [False] * len(info)
    def dfs(cur_node, cnt_sheep, cnt_wolf):
        global answer
        if cnt_wolf >= cnt_sheep:
            return
        answer = max(answer, cnt_sheep)
        
        for i in range(1, len(info)):
            if not visited[i]:
                if i in edge_info[cur_node]:
                    visited[i] = True
                    wolf = 1 if info[i] else 0
                    sheep = 1 if not info[i] else 0
                    dfs(i, cnt_sheep + sheep, cnt_wolf + wolf)
                    visited[i] = False
                else:
                    for j in range(len(visited)):
                        if visited[j] and i in edge_info[j]:
                            visited[i] = True
                            wolf = 1 if info[i] else 0
                            sheep = 1 if not info[i] else 0
                            dfs(i, cnt_sheep + sheep, cnt_wolf + wolf)
                            visited[i] = False

    visited[0] = True
    dfs(0, 1, 0)
    return answer
