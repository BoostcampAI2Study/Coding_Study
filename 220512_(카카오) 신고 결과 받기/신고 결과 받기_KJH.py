from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    cnting = defaultdict(set)   # 누가 누구한테 신고를 당했는가
    result = defaultdict(int)
    for i in report:
        id, r = i.split()
        cnting[r].add(id)
    
    for i in id_list:
        if len(cnting[i]) >= k:
            for j in cnting[i]:
                result[j]+=1
    
    for i in id_list:
        answer.append(result[i])
    print(answer)
    return answer
