from collections import defaultdict
from math import ceil

def solution(fees, records):
    answer = []
    
    # 요금표
    default_time, default_fees, unit_time, unit_fees = fees
    
    # 입 출차 defaultdict
    in_dict = defaultdict(list)
    out_dict = defaultdict(list)
    
    # 내역대로 defaultdict에 저장
    for record in records:
        time, code, direction = record.split()
        
        # 입차
        if direction == 'IN':
            in_dict[code].append(time)
        # 출차
        else:
            out_dict[code].append(time)
    
    # 차량 번호가 작은 자동차부터 요금 계산
    for code in sorted(in_dict.keys()):
        # 출차 시간 없는 경우 23:59
        if len(out_dict[code]) < len(in_dict[code]):
            out_dict[code].append('23:59')
        
        time = 0
        for in_time, out_time in zip(in_dict[code], out_dict[code]):
            # 시간 계산하기 (분단위)
            in_time = cal_time(in_time)        
            out_time = cal_time(out_time)

            time += out_time - in_time
        
        # 기본요금
        fee = default_fees
        
        # 기본시간 초과하면 기본요금 + 단위 시간마다 단위 요금 청구
        if time > default_time:
            fee += ceil((time - default_time)/unit_time) * unit_fees
                
        answer.append(fee)
    
    
    return answer


# 시간 계산하기 (분단위)
def cal_time(time:str) -> int:
    time = list(map(int, time.split(':')))
    time = time[0] * 60 + time[1]
    
    return time
