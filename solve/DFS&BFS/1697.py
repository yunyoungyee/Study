# 해당 문제는 graph를 만들지 않고 K까지의 거리를 빠르게 찾는 문제였음.
# 다만 최대 범위가 100000이라서 dist[]를 만들어두고 거리를 저장하는 방식을 사용함.
# dist[]를 쓰면서 자연스럽게 visited가 없어도 중복방지가 되는 방식임.

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
# N:수빈위치 K:동생위치
N, K = map(int,input().split())
dist = [-1]*100001
def bfs(V):
    queue=deque()
    queue.append(V)
    dist[V]=1
    while queue:
        out = queue.popleft()
        if 0<=out-1<=100000 and dist[out-1]== -1:
            queue.append(out-1)
            dist[out-1]=dist[out]+1
        if 0<=out+1<=100000 and dist[out+1]== -1:
            queue.append(out+1)
            dist[out+1]=dist[out]+1
        if 0<=out*2<=100000 and dist[out*2]== -1:
            queue.append(out*2)
            dist[out*2]=dist[out]+1
        if dist[K]!=-1:
            print(dist[K]-1)
            exit()

bfs(N)