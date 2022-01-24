K = int(input())
word_list = []
for _ in range(K):
    word_list.append(list(input()))

alphabet_set = set()
alphabet_map = [0] * 26
for i, word in enumerate(word_list):
    for j, character in enumerate(word):
        alphabet_num = ord(character) - 65  # ord("A") = 65
        alphabet_map[alphabet_num] += 10 ** (len(word) - j)     # 자릿수 더하기
        alphabet_set.add(alphabet_num)

sort_list = []
for alpha in alphabet_set:
    sort_list.append((alphabet_map[alpha], alpha))  # (자릿수, 알파벳 숫자)
sort_list.sort(reverse=True)

# 알파벳에 숫자 부여
temp = 9
for _, alphabet_num in sort_list:
    alphabet_map[alphabet_num] = temp
    temp -= 1

result = 0
for i, word in enumerate(word_list):
    for j, character in enumerate(word):
        alphabet_num = ord(character) - 65
        word_list[i][j] = str(alphabet_map[alphabet_num])
    result += int(''.join(word))
print(result)