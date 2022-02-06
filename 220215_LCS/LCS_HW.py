# reference: https://velog.io/@emplam27/알고리즘-그림으로-알아보는-LCS-알고리즘-Longest-Common-Substring와-Longest-Common-Subsequence

input_strs = [input() for _ in range(2)]
compare_str = [[0] * (len(input_strs[1]) + 1) for _ in range(len(input_strs[0]) + 1)]

for char_idx1 in range(len(input_strs[0])):
    for char_idx2 in range(len(input_strs[1])):
        # identical char
        if input_strs[0][char_idx1] == input_strs[1][char_idx2]:
            compare_str[char_idx1 + 1][char_idx2 + 1] = compare_str[char_idx1][char_idx2] + 1
        # different char
        else:
            compare_str[char_idx1 + 1][char_idx2 + 1] = max(compare_str[char_idx1][char_idx2 + 1], compare_str[char_idx1 + 1][char_idx2])

print(max(max(compare_str)))