import ast, collections, sys

N = int(sys.stdin.readline().strip())
weighted_chars = collections.defaultdict(int)
WORDS = [sys.stdin.readline().strip() for _ in range(N)]

# assign weight to each character based on positions. → ABCDE : A = 10000, B = 1000, ...
for word in WORDS:
    for power, char in enumerate(word[::-1]):
        weighted_chars[char] += 10**power

# assign (char) number to each character based on weights. → '9', '8', '7', ...
char2num = dict()
ascii_num = 57 # '9'
for char, _ in sorted(weighted_chars.items(), key=lambda x:x[1], reverse=True):
    char2num[char] = chr(ascii_num) 
    ascii_num-=1

# convert the words to the real numbers.
word2num = [ast.literal_eval(''.join([char2num[char] for char in word])) for word in WORDS]
print(sum(word2num))