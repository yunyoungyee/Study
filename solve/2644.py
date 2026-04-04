# 해당 문제는 dfs bfs 둘 다 가능하지만 촌 수를 찾는 것이기에 dfs로 깊게 내려가기보다 
# bfs로 해당하는 사람을 빠르게 찾는게 적합한 풀이과정임.
# 특히 dist배열을 따로 만들어서 bfs가 탐색하는 깊이(depth)마다 거리를 1개씩 증가하여 저장해두는 방식으로
# 최단 거리를 저장할 수 있고 이를 사람 간 촌 수 계산값으로 사용하는 것.
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
# 사람 수 N
# 사람 촌 수 계산 p1, p2
# 관계 개수 M
N = int(input())
p1, p2 = map(int,input().split())
M = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)
dist = [0]*(N+1)
def bfs(V):
    queue=deque()
    queue.append(V)
    visited[V]=True
    dist[V]=0
    while queue:
        out = queue.popleft()
        for i in graph[out]:
            if visited[i]==False:
                visited[i]=True
                dist[i]=dist[out]+1
                queue.append(i)

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
bfs(min(p1,p2))
if dist[max(p1,p2)] ==0:
    print(-1)
else:
    print(dist[max(p1,p2)])
