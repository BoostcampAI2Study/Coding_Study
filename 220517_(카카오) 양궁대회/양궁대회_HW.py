import copy
max_score, diff_score = 0, 0
answer = [-1]
def dfs(n, target, score, apeach_score, candidate, info):
    global max_score, answer, diff_score
    if n == 0 or target == 10:
        if target == 10:
            candidate[0] = n
            score += 10 if info[0] < n else 0
            apeach_score += 10 if info[0] >= n and info[0] != 0 else 0
        else:
            for i in range(target, 11):
                apeach_score += i if info[10 - i] != 0 else 0
        if score > apeach_score and diff_score <= score - apeach_score:
            answer = copy.deepcopy(candidate)
            max_score, diff_score = score, score - apeach_score
        return
      
    for i in range(n + 1):
        candidate[10-target] = i
        cur_score = target if info[10-target] < i else 0
        opposite_score = target if info[10-target] >= i and info[10-target] != 0 else 0
        dfs(n - i, target + 1, score + cur_score, apeach_score + opposite_score, candidate, info)
        candidate[10-target] = 0
            
def solution(n, info):
    for i in range(n + 1):
        candidate = [0] * 11
        candidate[10] = i 
        dfs(n - i, 1, 0, 0, candidate, info)
    return answer
