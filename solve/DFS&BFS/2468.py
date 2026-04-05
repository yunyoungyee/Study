# 해당 문제는 기본적인 지도형 dfs&bfs문제와 동일했는데, 하나 다른점은 방문 여부를 계속 사용해야해서 초기화를 시켜야 했고,
# 지도도 덮어씌우면 안되는 문제였음.
# 특히, 모든 영역이 비에 다 잠기는 경우에 끝내기 위해 최대 높이를 구하는 방식에서 기존 for문을 최대값인 100까지 돌았는데,
# 그렇게 하지 않고 graph 값들 중 최대값을 찾고 그 값을 반복문의 최대값으로 두는 방식으로 개선하였음.
# 또 다른 점이라면 bfs 인자에 비 높이를 같이 넘겨서 상하좌우 탐색을 할 때 비를 벽으로 가정하여 탐색하는 방법을 사용함.
import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]
result=0
dx=[1,0,-1,0]
dy=[0,1,0,-1]

def bfs(y,x,n):
    queue=deque()
    queue.append((y,x))
    rain = n
    while queue:
        ey, ex = queue.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0<=ny<N and 0<=nx<N:
                if graph[ny][nx]>rain and visited[ny][nx]==False:
                    visited[ny][nx]=True
                    queue.append((ny,nx))
max_height = max(map(max,graph))
#map(max,graph) -> 각 행에 max를 하나씩 적용해서 행 별 최대값을 모아둠.
#모아둔 값에 max()를 적용해서 가장 큰 값을 찾음.
for n in range(max_height):
#for n in range(100) 
    visited = [[False]*N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for i in range(N):
            if graph[j][i]>n and visited[j][i]==False:
                visited[j][i]=True
                bfs(j,i,n)
                cnt+=1
    if cnt==0:
        break
    if result<=cnt:
        result=cnt
        
print(result)
