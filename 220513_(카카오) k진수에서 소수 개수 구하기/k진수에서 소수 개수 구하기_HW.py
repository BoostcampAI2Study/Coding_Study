import math
def convert_num(n, k):
    k_num = ''
    while n > 0:
        n, r = divmod(n, k)
        k_num += str(r)
    return k_num[::-1]

def is_prime_num(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False 
    return True 
    
def solution(n, k):
    answer = 0
    # k진수로 변환, 조건에 맞는 수 저장
    num_list = [int(num) for num in convert_num(n, k).split('0') if num]
    # 소수 개수
    for num in num_list:
        if num > 1 and is_prime_num(num):
            answer += 1
    return answer
