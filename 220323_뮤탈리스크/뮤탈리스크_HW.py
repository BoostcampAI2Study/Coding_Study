import itertools, collections

N = int(input())
SCV = list(map(int, input().split())) + [0] * (3 - N)
visited = [[[0] * 61 for _ in range(61)] for _ in range(61)]
attacks = list(itertools.permutations([-9, -3, -1]))

q = collections.deque()
q.append((SCV, 0))
visited[SCV[0]][SCV[1]][SCV[2]] = True
min_move = 1e9

while q:
    hp, move = q.popleft()
    # check scv hp
    isExist = False
    for i in range(N):
        if hp[i] > 0:
            isExist = True
            break
    if not isExist:
        min_move = min(min_move, move)
        continue
    # attack scv
    for attack in attacks:
        new_hp = [0] * 3
        for i in range(N):
            if attack[i] + hp[i] > 0:
                new_hp[i] = attack[i] + hp[i]
            else:
                new_hp[i] = 0
        if not visited[new_hp[0]][new_hp[1]][new_hp[2]]:
            visited[new_hp[0]][new_hp[1]][new_hp[2]] = True
            q.append((new_hp, move + 1))
print(min_move)
