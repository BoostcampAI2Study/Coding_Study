import sys, heapq

N, M = map(int, sys.stdin.readline().strip().split())
BOARD = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
max_weights_sum = 0

# BF
for i in range(N):
    for j in range(M):
        heap = [(-BOARD[i][j], i, j)] # min heap -> max heap
        is_visited = set()
        weights_sum = 0

        # greedy
        while heap:
            weight, cur_i, cur_j = heapq.heappop(heap)
            weights_sum -= weight
            is_visited.add((cur_i, cur_j))

            # tetromino check
            if len(is_visited) == 4: break

            for new_i, new_j in ((cur_i, cur_j+1), (cur_i, cur_j-1), (cur_i+1, cur_j), (cur_i-1, cur_j)):
                if 0 <= new_i < N and 0 <= new_j < M and (new_i, new_j) not in is_visited:
                    heapq.heappush(heap, (-BOARD[new_i][new_j], new_i, new_j))

        max_weights_sum = max(max_weights_sum, weights_sum)

print(max_weights_sum)