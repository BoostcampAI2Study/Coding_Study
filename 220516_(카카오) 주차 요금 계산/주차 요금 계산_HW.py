import collections, math
def solution(fees, records):
    cars_park_record, cars_park_time = collections.defaultdict(list), collections.defaultdict(int)
    for record in records:
        time, car_num, _ = record.split()
        cars_park_record[car_num].append(time)
    
    for car_num in cars_park_record:
        times = cars_park_record[car_num]
        for i in range((len(times) + 1) // 2):
            in_hour, in_minute = map(int, times[i * 2].split(':'))
            print(in_hour, in_minute)
            if i * 2 + 1 >= len(times):
                out_hour, out_minute = 23, 59
            else:
                out_hour, out_minute = map(int, times[i * 2 + 1].split(':'))
            time = (out_hour - in_hour) * 60 + (out_minute - in_minute)
            cars_park_time[car_num] += time
    
    answer = []
    for car_num in sorted(cars_park_time):
        time = cars_park_time[car_num]
        if time <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1] + math.ceil((time - fees[0]) / fees[2]) * fees[3]
            answer.append(fee)
            
    return answer
