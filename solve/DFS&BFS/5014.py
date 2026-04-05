# 해당 문제는 최대 층수까지 bfs로 탐색을 하면서 해당 층수에 도달하는 최단거리를 구하는 문제였음
# 이 문제도 graph를 따로 만들지않고 U,D로 다음 층을 구하면서 바로 bfs 계산을 적용하는 문제임.
# 개인적으로 목적지 층에 도달하지 못할 경우 bfs 탐색을 어디서 끝내지? 하는 어려움에 빠졌는데, 
# 목적지 층에 도달하지 못한 채 최대 층수까지 탐색이 끝나면 알아서 queue가 비워지면서 bfs가 끝나기 때문에
# 목적지 층을 찾으면 dist[목적지 층]을 출력하고 queue가 다 비워져서 while문을 나갔을 때는 use the stairs를 출력하여 해결하는 문제임.
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
# F:건물층수 S:강호위치 G:스타링크위치 U:올라가는 층수(덧셈) D:내려가는 층수(뺄셈)
F, S, G, U, D = map(int,input().split())
dist=[-1]*(F+1)

def bfs(V):
    queue=deque()
    queue.append(V)
    dist[V]=0
    while queue:
        out = queue.popleft()
        if 0<out+U<=F and dist[out+U]==-1:
            dist[out+U]=dist[out]+1
            queue.append(out+U)
        if 0<out-D<=F and dist[out-D]==-1:
            dist[out-D]=dist[out]+1
            queue.append(out-D)
        if dist[G]!=-1:
            print(dist[G])
            exit()
    print("use the stairs")

bfs(S)