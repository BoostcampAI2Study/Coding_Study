import collections, math

def solution(fees, records):
    answer = []
    parking_lot = dict()
    cars_parking_time = collections.defaultdict(int)
    
    def time_conversion(time):
        hours, minutes = time.split(':')
        return int(hours)*60 + int(minutes)
    
    # spending time of in and out cars' in parking lot.
    for record in records:
        time, car_num, is_in = record.split()
        time = time_conversion(time)
        print(car_num, time)
        
        if is_in == 'IN':
            parking_lot[car_num] = time
        else:
            cars_parking_time[car_num] += (time - parking_lot[car_num])
            del parking_lot[car_num]
    
    # spending time of in and no out cars' in parking lot.
    if parking_lot:
        for car_num, time in parking_lot.items():
            cars_parking_time[car_num] += (time_conversion('23:59') - parking_lot[car_num])
    
    # calculate parking fees.
    for car_num, time in cars_parking_time.items():
        if time <= fees[0]:
            answer.append((car_num, fees[1]))
        else:
            answer.append((car_num, fees[1] + math.ceil((time-fees[0])/fees[2]) * fees[3]))
    
    return [fee for _, fee in sorted(answer, key=lambda x:x[0])]