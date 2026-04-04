import sys
from collections import deque
def dfs(V):
    visited[V]=True
    rs.append(V)
    for i in graph[V]:
        if not visited[i]:
            dfs(i)

def bfs(V):
    visited = [False]*(N+1)
    queue=deque()
    queue.append(V)
    visited[V]=True
    while queue:
        out = queue.popleft()
        rs.append(out)
        for i in graph[out]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


def qp(rs):
    print(*rs)
    rs.clear()

input = lambda: sys.stdin.readline().rstrip()
N, M, V = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
rs=[]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(N+1):
    graph[i].sort()
    
dfs(V)
qp(rs)
bfs(V)
qp(rs)