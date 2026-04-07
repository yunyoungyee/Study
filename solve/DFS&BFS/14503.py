# 해당 문제는 dfs로 풀수도 있고 while문을 쓰기도 하고 구현+시뮬레이션 알고리즘 문제임.
# dfs로 푼 코드의 경우 d 방향에 맞춰 dx, dy를 설정해야한다는 점이 key point임.
# 특히, d의 경우는 0 1 2 3 이 방향이기에 무한으로 90도씩 돌 수 있도록 해야하는데,
# 이는 (d-1)%4 이렇게 구현이 가능함. 응용으로 후진 같은 경우는 (d+2)%4 이렇게 구현이 가능함.
#N:x M:y 
#상하좌우 청소 안된 구역 있으면 반시계 90도
#d= 0:북 1:동 2:남 3:서 
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
Ry, Rx, d = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
#d 방향에 맞춰서 x,y를 잡아두어야 d 방향에 따라 전진이 가능함.
dx=[0,1,0,-1]
dy=[-1,0,1,0]
cnt = 0

# 1. 내 풀이 - 정답을 맞췄으나, 4방향을 미리보는 방식이 비효율적인 방식임.
# def dfs(y,x):
#     global d, cnt
#     clean=True
#     if graph[y][x]==0:
#         graph[y][x]=2
#         cnt+=1
#     for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#             if 0<=ny<N and 0<=nx<M and graph[ny][nx]==0:
#                 clean=False
#                 d=(d-1)%4
#                 break
            
#     if d==0:
#         if 0 <= y-1 < N and graph[y-1][x]==0 and not clean:
#             dfs(y-1,x)
#         elif 0 <= y+1 < N and graph[y+1][x]==1 and clean:
#             print(cnt)
#             exit()
#         else:
#             dfs(y,x)
#     elif d==1:
#         if 0 <= x+1 < M and graph[y][x+1]==0 and not clean:
#             dfs(y,x+1)
#         elif 0 <= x-1 < M and graph[y][x-1]==1 and clean:
#             print(cnt)
#             exit()
#         else:
#             dfs(y,x)
#     elif d==2:
#         if 0 <= y+1 < N and graph[y+1][x]==0 and not clean:
#             dfs(y+1,x)
#         elif 0 <= y-1 < N and graph[y-1][x]==1 and clean:
#             print(cnt)
#             exit()
#         else:
#             dfs(y,x)
#     elif d==3:
#         if 0 <= x-1 < M and graph[y][x-1]==0 and not clean:
#             dfs(y,x-1)
#         elif 0 <= x+1 < M and graph[y][x+1]==1 and clean:
#             print(cnt)
#             exit()
#         else:
#             dfs(y,x)

def dfs(y,x,d):
    global cnt

    if graph[y][x] == 0:
        graph[y][x] = 2 #청소한 영역은 2로 표기
        cnt+=1
    for _ in range(4): #dfs를 호출한다는건 청소를 해야하는거니까 바로 90도 회전을 하게 함.
        d = (d-1)%4 
        ny = y + dy[d]
        nx = x + dx[d]

        if graph[ny][nx]==0:
            dfs(ny,nx,d)
            return # 이동에 성공했으면 함수 종료
    back = (d+2)%4
    ny = y + dy[back]
    nx = x + dx[back]

    if graph[ny][nx] == 1:
        print(cnt)
        exit()
    dfs (ny,nx,d)

dfs(Ry,Rx,d)