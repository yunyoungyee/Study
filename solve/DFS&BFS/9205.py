# 해당 문제는 간선 그래프 문제이지만 기존에 그래프 정보를 저장하는 방식과는 다르게 다음 노드를 계산하면서 bfs계산을 하는 문제였음.
# 그래도 거리 계산을 했을 때 범위에 포함되는 위치는 queue에다 넣는 방식은 동일했음.
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
# T:시행반복횟수 N:편의점개수 X,Y:각 장소 좌표
T=int(input())

def bfs(x,y):
    queue=deque()
    queue.append((x,y))
    while queue:
        ex, ey = queue.popleft()
        if abs(ex - graph[N+1][0]) + abs(ey - graph[N+1][1]) <=1000:
            return True
        
        for i in range(1,N+1):
            if visited[i]==False and abs(ex - graph[i][0]) + abs(ey - graph[i][1]) <=1000:
                queue.append(graph[i])
                visited[i]=True

for _ in range(T):
    N=int(input())
    graph=[list(map(int,input().split())) for _ in range(N+2)]
    visited = [False]*(N+3)
    x,y=graph[0]
    visited[0]=True
    res=bfs(x,y)
    if res==True:
        print("happy")
    else:
        print("sad")
    
