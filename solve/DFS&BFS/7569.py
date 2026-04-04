# 해당 문제는 3차원에서의 bfs 문제로 z축이 포함된 상하좌우 위 아래를 확인한다는 점이 추가됐음.
# 계란이 모두 익는 최단 시간을 구하기 때문에 처음에 시작점을 모두 찾고 queue에 넣어
# bfs를 한번 수행하는게 key point임. 예시로 바이러스나, 동시에 확산되는 문제가 있으며 반대로 빌딩 구역처럼 시작점이 정해지지 않은
# 문제라면 bfs를 반복 실행할 수도 있음.
# 또한 최단 시간을 찾다보니 방문 여부를 확인할 필요가 없었고, 익는 시간을 바로 MAP에 덮어쓰며 최대값을 따로 저장해두어 bfs가 끝난 후
# 최대값이 곧 전체가 익는 시간임. 단, 각종 예외 상황에 따른 분기처리는 필요함.
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
# M:X축 N:Y축 H:Z축
M, N, H = map(int,input().split())
MAP=[[list(map(int,input().split())) for _ in range(N)] for _ in range(H)]
queue = []
# result=0
max_day=0
zero_cnt=0
dx=[1,0,-1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]

def bfs(queue):
    global max_day
    global zero_cnt
    queue=deque(queue)
    while queue:
        ez,ey,ex = queue.popleft()
        for p in range(6):
            nx=ex+dx[p]
            ny=ey+dy[p]
            nz=ez+dz[p]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H:
                if MAP[nz][ny][nx]==0:
                    MAP[nz][ny][nx]=MAP[ez][ey][ex]+1
                    max_day=MAP[nz][ny][nx]
                    zero_cnt-=1
                    queue.append((nz,ny,nx))


for k in range(H):
    for j in range(N):
        for i in range(M):
            if MAP[k][j][i]==1:
                queue.append((k,j,i))
            elif MAP[k][j][i]==0:
                zero_cnt+=1
bfs(queue)
if zero_cnt > 0:
    print(-1)
elif max_day == 0:
    print(0)
else:
    print(max_day-1)
# for k in range(H):
#     for j in range(N):
#         for i in range(M):
#             if MAP[k][j][i]==0:
#                 print(-1)
#                 exit()
#             elif MAP[k][j][i]>=result:
#                 result=MAP[k][j][i]

# if result==1:
#     print(0)
# else:
#     print(result-1)