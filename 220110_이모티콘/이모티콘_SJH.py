'''
14226번: 이모티콘
https://www.acmicpc.net/problem/14226

스마일 이모티콘 S개 만들기
1. 이모티콘 복사
2. 이모티콘 붙여넣기
3. 이모티콘 하나 삭제
각 연산 1초 걸림

복사+ 붙여넣기 세트 2초
'''

emo_num = int(input())  # 이모티콘 수
count = 0   # 연산 시간 카운트
screen = 1  # 화면에 떠있는 이모티콘

while screen < emo_num:
    if emo_num - screen * 2 < screen:
        while emo_num % screen:
            print(screen)
            screen -= 1
            count += 1
        print(screen,count)
        count += emo_num // screen - 1
        screen = emo_num
        break
    
    screen *= 2
    count += 2
    print(screen, count)


print(count)