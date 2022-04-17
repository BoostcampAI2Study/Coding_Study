from collections import defaultdict
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report_dict, report_cnt = defaultdict(list), defaultdict(int)
    
    # report_dict: user_id - report_id, report_cnt: report_id 신고 개수
    for users in report:
        user_id, report_id = users.split(" ")
        if report_id not in report_dict[user_id]:
            report_dict[user_id].append(report_id)
            report_cnt[report_id] += 1
    
    # 정지된 id list
    report_id_list = []
    for report_id in report_cnt.keys():
        if report_cnt[report_id] >= k:
            report_id_list.append(report_id)
            
    # mail 개수
    for idx, user_id in enumerate(id_list):
        for report_id in report_dict[user_id]:
            if report_id in report_id_list:
                answer[idx] += 1
        
    return answer
