# 해당 문제는 방문 여부를 확인하는 배열과 빙하 정보(입력값), 새로운 빙하 정보 저장 배열은 N*M으로 만들어도 되지만
# 빙하가 녹는걸 계산하고 빙하 덩어리를 확인하는 계산을 빙하가 있는 곳에서만 하는게 key point였음.
# 그래서 ice[]와 new_ice[]를 통해 빙하가 있는 위치정보만 저장하고 거기에서 bfs계산을 돌려야했으며 변하는 빙하 정보를 new_ice[]에 임시저장하여
# 빙하 녹는 계산이 끝난 후 ice[]에 덮어씌워버리는 형식으로 풀어나가야 했음.
import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()
# N:행(y) M:열(x)
N, M = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
dx = [1,0,-1,0]
dy = [0,1,0,-1]
max_year=max(map(max,graph))

def bfs(y,x):
    visited[y][x]=True
    queue=deque()
    queue.append((y,x))
    while queue:
        ey, ex = queue.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<M:
                if graph[ny][nx]!=0 and visited[ny][nx]==False:
                    visited[ny][nx]=True
                    queue.append((ny,nx))

ice =[]
for j in range(N):
    for i in range(M):
        if graph[j][i]!=0:
            ice.append((j,i))

year=0

while True:
    visited=[[False]*M for _ in range(N)]
    ice_cnt=0

    for y,x in ice:
        if visited[y][x]==False:
            ice_cnt+=1
            if ice_cnt>=2:
                print(year)
                exit()
            bfs(y,x)
    if ice_cnt==0:
        print(0)
        exit()
    
    ngraph = [[0]*M for _ in range(N)]
    new_ice=[]

    for y,x in ice:
        cnt=0
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if 0<= ny < N and 0<= nx < M:
                if graph[ny][nx]==0:
                    cnt+=1
        ngraph[y][x] = max(0, graph[y][x]-cnt)

        if ngraph[y][x] > 0:
            new_ice.append((y,x))
    graph = ngraph
    ice = new_ice
    year+=1

# def bfs(y,x):
#     visited[y][x]=True
#     queue=deque()
#     queue.append((y,x))
#     while queue:
#         ey, ex = queue.popleft()
#         for k in range(4):
#             ny = ey + dy[k]
#             nx = ex + dx[k]
#             if 0<=ny<N and 0<=nx<M:
#                 if graph[ny][nx]==0:
#                     #ngraph[ey][ex]=graph[ey][ex]-1
#                     if ngraph[ey][ex]-1>=0:
#                         ngraph[ey][ex]-=1
#                 if graph[ny][nx]!=0 and visited[ny][nx]==False:
#                     visited[ny][nx]=True
#                     queue.append((ny,nx))

# for year in range(1,max_year):
#     visited=[[False]*M for _ in range(N)]
#     cnt=0
#     ngraph = [row[:] for row in graph]
#     for j in range(N):
#         for i in range(M):
#             if graph[j][i]!=0 and visited[j][i]==False:
#                 cnt+=1
#                 bfs(j,i)
#     graph = [row[:] for row in ngraph]
#     if cnt!=1:
#         print(year)
#         exit()
# print(0)
# 위 과정은 첫번째 풀이로 bfs안에서 빙하가 녹는 로직이 같이 있었고 bfs 계산이 수행됨에 따라 본래 graph가 달라져 빙하 녹는 로직에도 영향을 주어 잘못된 접근 방식.

# def bfs(y,x):
#     visited[y][x]=True
#     queue=deque()
#     queue.append((y,x))
#     while queue:
#         ey, ex = queue.popleft()
#         for k in range(4):
#             ny = ey + dy[k]
#             nx = ex + dx[k]
#             if 0<=ny<N and 0<=nx<M:
#                 if graph[ny][nx]!=0 and visited[ny][nx]==False:
#                     visited[ny][nx]=True
#                     queue.append((ny,nx))
# year=0
# while True:
#     visited=[[False]*M for _ in range(N)]
#     ngraph = [[0]*M for _ in range(N)]
#     cnt=0
#     for j in range(N):
#         for i in range(M):
#             ice_cnt=0
#             if graph[j][i]!=0 and visited[j][i]==False:
#                 cnt+=1
#                 if cnt>=2:
#                     print(year)
#                     exit()
#                 bfs(j,i)
#     if cnt == 0:
#         print(0)
#         exit()
#     for j in range(N):
#         for i in range(M):
#             ice_cnt=0
#             if graph[j][i]!=0:
#                 for k in range(4):
#                     ny = j + dy[k]
#                     nx = i + dx[k]
#                     if 0<=ny<N and 0<=nx<M and graph[ny][nx]==0:
#                         ice_cnt+=1
#             ngraph[j][i]=max(0,graph[j][i]-ice_cnt)
#     graph = [row[:] for row in ngraph]
#     year+=1
# 위 과정은 값을 제대로 출력해내지만, 시간초과가 발생하는데 그 이유를 보면 3중 for으로 빙하가 없는 모든 구역을 탐색하다보니 
# 문제 상황처럼 300*300-> 90000칸에 year도 300번 돌다가 2700만인데 bfs계산도 하는 것이 문제였음.