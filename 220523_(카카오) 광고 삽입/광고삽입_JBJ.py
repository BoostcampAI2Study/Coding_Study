def sec_2_str(second):
    hour, minute = divmod(second, 3600)
    minute, second = divmod(minute, 60)
    return f'{hour:02d}:{minute:02d}:{second:02d}'

def str_2_sec(string):
    hour, minute, second = map(int, string.split(':'))
    return (hour*3600)+(minute*60)+(second)

def solution(play_time, adv_time, logs):
    play_time, adv_time = str_2_sec(play_time), str_2_sec(adv_time)
    play_cnt_list = [0]*(play_time+1)
    
    for idx, log in enumerate(logs): # play counts at the time.
        start_time, end_time = log.split('-')
        play_cnt_list[str_2_sec(start_time)] += 1
        play_cnt_list[str_2_sec(end_time)] -= 1
    
    for idx in range(play_time): # number of plays per second. (cumulative sum)
        play_cnt_list[idx+1] += play_cnt_list[idx]
    for idx in range(play_time): # 0 ~ idx cumulative play time.
        play_cnt_list[idx+1] += play_cnt_list[idx]
    
    max_adv_start_time, max_adv_play_time = 0, play_cnt_list[adv_time]
    for adv_start_time in range(1, play_time-adv_time+1):
        adv_end_time = adv_start_time + adv_time
        adv_play_time = play_cnt_list[adv_end_time] - play_cnt_list[adv_start_time]
        if adv_play_time > max_adv_play_time:
            max_adv_start_time, max_adv_play_time = adv_start_time+1, adv_play_time
    
    return sec_2_str(max_adv_start_time)