from collections import defaultdict

N = int(input())

# 문자별로 값 저장
db = defaultdict(int)
for _ in range(N):
    word = input()
    for idx, i in enumerate(word):
        db[i] += 10**(len(word)-idx-1)

# 값이 큰 문자부터 계산
MAX = 9
answer = 0
for value in sorted(list(db.values()))[::-1]:
    answer += value*MAX
    MAX -= 1
print(answer)

