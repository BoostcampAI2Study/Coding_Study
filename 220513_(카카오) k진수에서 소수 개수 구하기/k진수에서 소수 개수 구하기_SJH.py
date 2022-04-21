def solution(n, k):
    answer = 0
    
    kn = convert(n,k) if k < 10 else str(n) # 진수 변환
    kn = kn.split('0')
    
    nums = []    
    for _kn in kn:
        if _kn:
            nums.append(int(_kn))            
            
    # 소수면 count
    for num in nums:
        if num < 2:
            continue
        for i in range(2, int(num ** 0.5)+1):
            if num % i == 0:
                break
        else:
            answer += 1   
    
    return answer


def convert(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1]