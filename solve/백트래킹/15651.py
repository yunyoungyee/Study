# 해당 문제는 순열이지만 순서를 신경쓸 필요가 없는 이유가 중복순열이기 때문임.
# 그래서 방문여부를 포함하지 않는 것으로 해결이 가능함.
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
res=[]

def recur(num):
    if num == M:
        print(*res)
        return
    for i in range(1,N+1):
        res.append(i)
        recur(num+1)
        res.pop()

recur(0)