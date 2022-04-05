import itertools, sys

N, K = map(int, sys.stdin.readline().rstrip().split())
WORDS = []
char_candidates, cur_chars = set(), set(['a', 'n', 't', 'i', 'c']) # 'anta' + 'tica' ==> a, n, t, i, c
for _ in range(N):
    answer, word = 0, set(sys.stdin.readline().rstrip())
    for char in (word - cur_chars):
        answer |= (1 << (ord(char) - ord('a'))) # bitmasking
        char_candidates.add(char)
    WORDS.append(answer)

if K < 5:
    print(0)
    sys.exit()
elif K == 26 or len(char_candidates) < K-5:
    print(len(WORDS))
    sys.exit()

max_read_cnt = 0
for chars in itertools.combinations(char_candidates, K-5):
    taught_chars = 0
    for char in chars:
        taught_chars |= (1 << (ord(char) - ord('a'))) # bitmasking

    total_read_cnt = 0
    for chars_in_word in WORDS:
        if taught_chars | chars_in_word == taught_chars: # compare taught characters with word characters.
            total_read_cnt += 1
    
    max_read_cnt = max(max_read_cnt, total_read_cnt)
print(max_read_cnt)