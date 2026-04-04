# 기본적인 bfs, dfs문제임.

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
C = int(input())
N = int(input())
graph = [ [] for _ in range(C+1)]
visited=[False]*(C+1)
cnt = 0

# def dfs(V):
#     global cnt
#     visited[V]=True
#     for i in graph[V]:
#         if not visited[i]:
#             cnt+=1
#             visited[i]=True
#             dfs(i)

def bfs(V):
    global cnt
    queue=deque()
    queue.append(V)
    visited[V]=True
    while queue:
        out = queue.popleft()
        for i in graph[out]:
            if not visited[i]:
                cnt+=1
                visited[i]=True
                queue.append(i)

for _ in range(N):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
# dfs(1)
bfs(1)
print(cnt)