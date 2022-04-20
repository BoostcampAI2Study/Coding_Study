from collections import defaultdict


def solution(info, edges):
    answer = 0

    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
    max_cnt = -1

    def dfs(sheep: int, wolf: int, node: int, basket: set):
        nonlocal max_cnt
        if sheep == wolf:
            max_cnt = max(max_cnt, sheep)
            return
        basket |= set(graph[node])
        for n in basket:
            if info[n]:
                dfs(sheep, wolf + 1, n, basket - set([n]))
            else:
                dfs(sheep + 1, wolf, n, basket - set([n]))
        max_cnt = max(max_cnt, sheep)

    dfs(1, 0, 0, set())

    print(max_cnt)
    return max_cnt
