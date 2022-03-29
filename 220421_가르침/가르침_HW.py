import sys
N, K = map(int, sys.stdin.readline().split())

fix_chars, candidate_chars = set('antic'), set()
words, chars = [], [0] * 26
result = 0

for idx in range(N):
    word = set(sys.stdin.readline().strip()) - fix_chars
    words.append(word)
    candidate_chars.update(word)
candidate_chars = list(candidate_chars)

for char in fix_chars:
    chars[ord(char) - ord('a')] = 1

def dfs(cnt, char_idx):
    global result
    if cnt == 0:
        read_word = 0
        for word in words:
            for char in word:
                if not chars[ord(char) - ord('a')]:
                    break
            else:
                read_word += 1
        result = max(result, read_word)
        return
    for idx in range(char_idx, len(candidate_chars)):
        num = ord(candidate_chars[idx]) - ord('a')
        if not chars[num]:
            chars[num] = 1
            dfs(cnt - 1, idx)
            chars[num] = 0

if K >= 5:
    if K < len(candidate_chars) + 5:
        dfs(K - 5, 0)
    else:
        result = N
print(result)
