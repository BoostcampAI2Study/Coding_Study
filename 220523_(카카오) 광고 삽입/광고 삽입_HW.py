def get_time(str_time):
    hour, minute, second = str_time.split(":")
    return int(hour) * 3600 + int(minute) * 60 + int(second)

def solution(play_time, adv_time, logs):
    play_time, adv_time = get_time(play_time), get_time(adv_time)
    cur_person = [0] * (play_time + 2)
    # time 변환 & 누적합
    for log in logs:
        start, end = log.split("-")
        cur_person[get_time(start)] += 1
        cur_person[get_time(end)] -= 1
    
    for i in range(len(cur_person) - 2):
        cur_person[i + 1] += cur_person[i]
    
    # 광고 시작 시간 찾기
    total_person = sum(cur_person[:adv_time])
    max_person, result = total_person, 0
    for t in range(play_time - adv_time):
        total_person -= (cur_person[t] - cur_person[t + adv_time])
        if total_person > max_person:
            max_person = total_person
            result = t + 1
    
    # convert time to str
    hour = str(result // 3600).zfill(2)
    minute = str(result//60 - int(hour) * 60).zfill(2)
    second = str(result - int(hour) * 3600 - int(minute) * 60).zfill(2)
    
    return hour + ":" + minute + ":" + second
