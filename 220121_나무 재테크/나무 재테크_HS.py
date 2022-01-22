from collections import defaultdict
import heapq as hq

input_t = lambda x: list(map(int, x.split()))
N, M, K = input_t(input())

A = [input_t(input()) for _ in range(N)]
# 나무들의 좌표와 나이 정보를 담는 dict
Tree_info = defaultdict(list)
for _ in range(M):
    x, y, z = input_t(input())
    # 0번이 늘 최소가 되게 heap 이용
    hq.heappush(Tree_info[(y-1)*5 + (x-1)], z)
board = [[5]*N for _ in range(N)]
# 봄
def spring(N):
    # 봄을 지내고 죽은 애들
    death_note = []
    # 봄을 지내고 살아남은 애들
    alive_note = []
    for i in range(N**2):
        # 좌표로 변환
        r, c = divmod(i, N)
        while Tree_info[i]:
            tree_age = hq.heappop(Tree_info[i])
            # 양분 소모 후 성장
            if board[r][c] >= tree_age:
                board[r][c] -= tree_age
                alive_note.append(tree_age+1)
            # 양분이 부족하면 주금
            else:
                death_note.append((i, tree_age))
        # 살아남은 애들 push
        for age in alive_note:
            hq.heappush(Tree_info[i], age)
        alive_note.clear()
    # 죽은 애들 여름으로 넘김
    return death_note
# 여름
def summer(N, death_note):
    # 죽은 나무들 나이의 절반만큼 양분에 추가
    for i, age in death_note:
        r, c = divmod(i, N)
        board[r][c] += age//2
# 가을
def fall(N):
    # 인접한 칸
    adjacent = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]
    for k, v in Tree_info.items():
        for age in v:
            # 5배수 아니면 넘기기
            if age % 5 != 0:
                continue
            r, c = divmod(k, N)
            for my, mx in adjacent:
                ny, nx = r+my, c+mx
                if 0 <= ny < N and 0 <= nx < N:
                    # (ny*N, nx) 좌표에 나이 1 나무 추가
                    hq.heappush(Tree_info[ny*N + nx], 1)
# 겨울
def winter(N):
    for i in range(N**2):
        r, c = divmod(i, N)
        # 양분 추가
        board[r][c] += A[r][c]
# 나무 세기
def count_trees():
    answer = 0
    for v in Tree_info.values():
        answer += len(v)
    return answer

for i in range(K):
    summer(N, spring(N))
    fall(N)
    winter(N)

    
print(count_trees())
print(Tree_info)