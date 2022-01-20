

N, K = map(int, input().split())
# 체스판
m = [list(map(int, input().split())) for _ in range(N)]
# 체스판 위의 말들의 상태 ('O'인 경우 말이 없는 경우 '123'이라면 1번말 위에 2번말 위에 3번 말이 있는 경우)
m2 = [['O'] * N for _ in range(N)]
# 말들의 좌표와 방향을 담는 딕셔너리
horses = dict()
# 순서대로 우, 좌, 상, 하
move = [(0, 1), (0, -1), (-1, 0), (1, 0)]
answer = 0

for i in range(K):
    r, c, v = list(map(int, input().split()))
    # 문자열의 형태로 저장
    m2[r-1][c-1] = str(i)
    # 초기 말들의 좌표와 방향 저장
    horses[str(i)] = {'coor': (r-1, c-1), 'dir': v}

# 다음 칸의 색상 확인
def check(y, x, N):
    if 0 <= y < N and 0<= x < N:
        return m[y][x]
    return -1

# 말 움직일 때 사용하는 함수
def moving(n, cy, cx, ny, nx, color):      # 말 번호, 현재 좌표, 다음 좌표, 다음 좌표의 색상
    # 현재 좌표의 문자열을 쪼개서 남을 말들과 옮길 말들을 분리
    current, next = m2[cy][cx].split(n)
    # split 하면 자기 자신은 사라지므로 보충
    next = n + next
    # 옮길 좌표가 빨간색이면 뒤집기
    if color:
        next = next[::-1]
    # 남는 말이 없으면 'O' 처리
    if not current:
        current = 'O'
    # 옮길 좌표에 말이 없으면 그대로 복사
    m2[ny][nx] = next if m2[ny][nx] == 'O' else m2[ny][nx] + next
    # 현재 좌표 말 상태 갱신
    m2[cy][cx] = current

    # 자기 위에 있는 말들 좌표 갱신
    for _n in next:
        horses[_n]['coor'] = (ny, nx)      
    

# 1000보다 크면 종료
for i in range(K*1001):
    # 현재 검사하는 말의 번호, 좌표, 방향
    n = str(i % K)
    r, c = horses[n]['coor']
    v = horses[n]['dir']

    if int(n) == 0:
        answer += 1
    if answer > 1000:
        break

    my, mx = move[v-1]
    ny, nx = r + my, c + mx

    # 움직일 칸의 색상 찾기
    color = check(ny, nx, N)
    # 흰색 혹은 빨간색인 경우 경우
    if color in [0, 1]:
        moving(n, r, c, ny, nx, color)                        
    # 파란색 혹은 판을 벗어나는 경우
    elif color in [2, -1]:
        # 방향 반대로
        ny, nx = r - my, c - mx
        v += -1 + (v%2) * 2
        # 다음 칸도 파란색이라면
        if check(ny, nx, N) in [2, -1]:
            # 방향만 바꾸고 끝
            horses[n]['dir'] = v
        else:
            moving(n, r, c, ny, nx, check(ny, nx, N))
            horses[n]['dir'] = v
    # 4개 이상 차면 조기 종료
    if check(ny, nx, N) != -1 and len(m2[ny][nx]) >= 4:
        break

if answer > 1000:
    print(-1)
else:
    print(answer)

'''
Memory : 30864 KB
Time : 96 ms
language : Python3
Code length : 2692 B
'''
