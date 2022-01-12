from collections import deque
def bfs():
    q = deque([int(subin)])
    while q:
        cur_loc = q.popleft()
        if cur_loc == int(brother):
            print(time_check[cur_loc])
            break

        for nxt_loc in [cur_loc - 1, cur_loc + 1, cur_loc * 2]:
            if 0 <= nxt_loc <= 10 ** 5 and not time_check[nxt_loc]:
                time_check[nxt_loc] = time_check[cur_loc] + 1
                q.append(nxt_loc)

if __name__ == "__main__":
    cur_pt = input().split()
    subin, brother = cur_pt
    time_check = [0] * (10 ** 5 + 1)
    bfs()