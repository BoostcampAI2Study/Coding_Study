import sys

N = int(sys.stdin.readline())
work_time, preceding_workset = [0]*(N+1), dict()
for work_id in range(1, N+1):
    work_info = list(map(int, sys.stdin.readline().split()))
    if work_info[1] == 0:
        work_time[work_id] = work_info[0]
    else:
        preceding_time = 0
        for preceding_work in work_info[2:]:
            preceding_time = max(preceding_time, work_time[preceding_work])
        work_time[work_id] = work_info[0] + preceding_time

print(max(work_time))