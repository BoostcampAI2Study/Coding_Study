import collections

def solution(id_list, report, k):
    REPORTS, report_cnt_dict = collections.defaultdict(set), collections.defaultdict(int)
    for rep in report:
        reporter_id, bad_user_id = rep.split()
        if bad_user_id not in REPORTS[reporter_id]: # handling duplicates
            REPORTS[reporter_id].add(bad_user_id)
            report_cnt_dict[bad_user_id]+=1
    
    banned_ids = set()
    for bad_user_id, report_cnt in report_cnt_dict.items():
        if report_cnt >= k:
            banned_ids.add(bad_user_id)

    return [len(set(REPORTS[reporter_id]) & banned_ids) for reporter_id in id_list]