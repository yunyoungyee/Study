# 최단거리를 찾기 때문에 탐색한 길에 대해서 MAP을 거리로 덮어씌우는 방식임.
# DFS는 모든 길을 다 다니기 때문에 BFS를 쓰는데, 탐색한 길을 거리로 덮어씌우면서
# 계속 이어지는 길은 거리를 1씩 늘려가며 덮어씌우고 끊기거나, 돌아갈 일이 없도록 만들어버림.
# 어떻게 돌아가는 길이 없도록 하는걸까? 상하좌우로 길이 있으면 일단 1씩 올려서 거리를 덮어씌웠기 때문에
# 방문여부를 따로 확인하지 않아도 덮어씌워진 해당 MAP배열 값에서 다음 상하좌우를 탐색하며 1일 경우에 거리를 덮어씌우는 것임.
# 예)
# 100 -> 100 -> 100 -> 100
# 111    211    231    234

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
MAP = [list (map(int,input().strip())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(y,x):
    queue = deque()
    queue.append((y,x))
    while queue:
        ey, ex = queue.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if MAP[ny][nx]==1:
                    MAP[ny][nx]=MAP[ey][ex]+1
                    queue.append((ny,nx))

for j in range(N):
    for i in range(M):
        if MAP[j][i]!=0 and visited[j][i]==False:
            visited[j][i]=True
            bfs(j,i)
print(MAP[N-1][M-1])
print(MAP[0][0])
print(MAP[0][1])
print(MAP[1][0])
print(MAP[1][1])
print(MAP[2][0])