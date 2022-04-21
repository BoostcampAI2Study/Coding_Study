from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    report_dict = defaultdict(set)      # 각 유저가 신고한 유저
    reported_count = defaultdict(int)   # 신고받은 횟수
    stop = set()
    
    for pair in report:
        uid, r_uid = pair.split()   # 신고한 유저, 신고당한 유저       
        
        # 해당 유저를 이미 신고했다면 pass
        if r_uid in report_dict[uid]:
            continue
        
        # 신고한 유저 기록
        report_dict[uid].add(r_uid)
        
        # 신고된 유저 count 이미 정지된 유저는 pass
        if r_uid not in stop:
            reported_count[r_uid] += 1           
    
            # k회 이상 신고되었으면 set에 저장
            if reported_count[r_uid] == k:
                stop.add(r_uid)
                
    # 메일 받은 횟수 구하기
    for uid in id_list:
        answer.append(len(report_dict[uid]&stop))
    
    
    return answer