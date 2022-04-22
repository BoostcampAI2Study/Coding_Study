from collections import defaultdict


def solution(board):
    min_cost = float("inf")
    mapping = {(1, 0): "d", (-1, 0): "u", (0, 1): "r", (0, -1): "l"}

    def init_list():
        return [[float("inf") for _ in range(len(board))] for _ in range(len(board))]

    cost_table = defaultdict(init_list)
    visited = [[0 for _ in range(len(board))] for _ in range(len(board))]
    
    def dfs(pos, prev, cost, cnt):
        nonlocal min_cost,visited
        if cost_table[cnt][pos[0]][pos[1]] >= cost:
            cost_table[cnt][pos[0]][pos[1]] = cost
        else:
            return
        if cost >= min_cost:
            return

        if pos == (len(board) - 1, len(board) - 1):
            min_cost = min(min_cost, cost_table[cnt][len(board) - 1][len(board) - 1])
            return

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            x, y = pos[0] + dx, pos[1] + dy
            if 0 <= x < len(board) and 0 <= y < len(board):
                if not board[x][y] and not visited[x][y]:
                    visited[x][y] = 1
                    if mapping[(dx, dy)] == prev or prev == None:
                        dfs((x, y),mapping[(dx, dy)],cost + 100, cnt + 1)
                    else:
                        dfs((x, y),mapping[(dx, dy)], cost + 600, cnt + 1)
                    visited[x][y] = 0

    dfs((0, 0), None, 0, 0)

    print(min_cost)
    return min_cost
