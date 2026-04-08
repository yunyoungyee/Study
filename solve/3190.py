# 해당 문제는 구현하는 순서를 굉장히 잘 세워서 중간에 꼬이지 않게 차근차근 조건을 만족해나가는 문제임.
# 순서를 정리해보면, 
# 1. 시간 증가 (이동 시도)
# 2. 벽 충돌
# 3. 몸 충돌
# 4. 머리 이동
# 5. 사과 처리
# 6. 방향 전환
# 이렇듯 충돌나는 경우를 가장 먼저 처리하고 그 이후에 머리 먼저 이동하고 사과에 대한 분기를 세우고
# 방향 전환을 마지막으로 해야했음.
# 특히, 방향 전환의 경우 3, D 처럼 숫자와 문자가 섞여 있어서 dict로 해결하는 방법을 썼는데
# t하고 d에 각각 숫자와 문자를 받아놓고 dict 변수[int(t)]에 d(문자)를 넣는 방식임.
# 이는 조건에 맞는 시간이 됐을 때 time변수로 dict에 있는지 확인하면 바로 문자열을 뽑아낼 수 있었음.
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
# N:보드크기 K:사과개수 L:회전횟수
N = int(input())
K = int(input())
apple=[[False]*(N+1)for _ in range(N+1)]
for _ in range(K):
    y,x=map(int,input().split())
    apple[y][x] = True

L = int(input())
rotate={}
for _ in range(L):
    t,d = input().split()
    rotate[int(t)] = d
visited=[[False]*(N+1) for _ in range(N+1)]
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def func(y,x):
    queue=deque()
    queue.append((y,x))
    visited[y][x]=True
    d=0
    time=0
    while True:
        ey, ex = queue[-1]
        ny = ey + dy[d]
        nx = ex + dx[d]
        time+=1
        if not (1<=ny<=N and 1<=nx<=N):
            print(time)
            return
        if visited[ny][nx]:
            print(time)
            return
        
        queue.append((ny,nx))
        visited[ny][nx]=True

        if not apple[ny][nx]:
            ty,tx =queue.popleft()
            visited[ty][tx]=False
        elif apple[ny][nx]:
            apple[ny][nx]=False
        

        if time in rotate:
            if rotate[time] == 'D':
                d=(d+1)%4
            else:
                d=(d-1)%4


func(1,1)

# 1. 시간 증가 (이동 시도)

# 2. 벽 충돌

# 3. 몸 충돌

# 4. 머리 이동

# 5. 사과 처리

# 6. 방향 전환