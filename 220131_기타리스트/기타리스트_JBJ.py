import sys

N, S, M = map(int, sys.stdin.readline().strip().split())
CHANGES = list(map(int, sys.stdin.readline().strip().split()))
volume_list = [-1 for _ in range(M+1)]
volume_list[S] = 0

for song_idx, change in enumerate(CHANGES, start=1):
    new_volume_list = []
    for volume in range(M+1):
        # get previously played volume.
        if volume_list[volume] == song_idx-1:
            # volume changes validation.
            if volume+change <= M:
                new_volume_list.append(volume+change)
            if 0 <= volume-change:
                new_volume_list.append(volume-change)
    # update volume list with new volumes.         
    for new_volume in new_volume_list:
        volume_list[new_volume] = song_idx

max_volume = -1
for volume in range(M,-1,-1):
    if volume_list[volume] == N:
        max_volume = volume
        break
print(max_volume)