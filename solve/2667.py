import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
MAP=[list(map(int,input().strip())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
size=0
result = []

# def dfs(y,x):
#     global size
#     size+=1
#     for k in range(4):
#         nx = x + dx[k]
#         ny = y + dy[k]
#         if 0<=nx<N and 0<=ny<N:
#             if MAP[ny][nx]!=0 and visited[ny][nx]==False:
#                 visited[ny][nx]=True
#                 dfs(ny,nx)

def bfs(y,x):
    global size
    queue=deque()
    queue.append((y,x))
    while queue:
        ey, ex = queue.popleft()
        size+=1
        for k in range(4):
            nx = ex + dx[k]
            ny = ey + dy[k]
            if 0<=nx<N and 0<=ny<N:
                if MAP[ny][nx]!=0 and visited[ny][nx]==False:
                    visited[ny][nx]=True
                    queue.append((ny,nx))

for j in range(N):
    for i in range(N):
        if MAP[j][i]!=0 and visited[j][i]==False:
            visited[j][i]=True
            size=0
            # dfs(j,i)
            bfs(j,i)
            result.append(size)
result.sort()
print(len(result))
for res in result:
    print(res)

