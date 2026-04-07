
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
res=[]
visited=[False]*(N+1)

def recur(start):
    if len(res)==M:
        print(*res)
        return

    for i in range(start,N+1): # for문 시작을 재귀함수 인자 값으로 하면 부모노드보다 작은 값은 자연스럽게 제외된다.
            res.append(i)
            recur(i+1)
            res.pop()

recur(1)