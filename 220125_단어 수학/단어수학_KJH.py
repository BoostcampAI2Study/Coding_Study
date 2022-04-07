import sys
Alhpa = []
Numb = ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0']
N = int(sys.stdin.readline())
_alpha = set()
for _ in range(N):
    x = sys.stdin.readline().rstrip()
    Alhpa.append(x)
    for i in x:
        _alpha |= set(i)

_alpha = sorted(list(_alpha))
answer = 0
visited = []
for i in range(len(_alpha)):
    change = {}
    tmp = {}
    if i == len(_alpha) - 1:
        visited.append((set(_alpha) - set(visited)).pop())
        break
    for al in _alpha:
        tmp_num = []
        change[al] = Numb[i]
        for A in _alpha:
            if A in visited:
                change[A] = Numb[visited.index(A)]
            elif A != al:
                change[A] = '0'
        for alp in Alhpa:
            tmp_num.append(int(''.join(list(map(lambda x: change[x], alp)))))
        tmp[sum(tmp_num)] = al
    visited.append(tmp[max(tmp)])
for al, n in zip(visited, Numb[:len(_alpha)]):
    change[al] = n
for al in Alhpa:
    answer += int(''.join(list(map(lambda x: change[x], al))))
print(answer)
