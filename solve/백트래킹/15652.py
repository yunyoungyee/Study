# 해당 문제는 조합으로 순서는 상관없는데 다음 선택 시작 위치가 중요한 문제임.
# 특히 시작위치가 i의 시작점이 되는데, 재귀함수를 부를 때 i+1을 해주면 중복없는 조합이 되고
# i를 그대로 넘기면 중복을 포함하는 조합이 되는 것임.
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
res=[]

def recur(start):
    if len(res)==M:
        print(*res)
        return
    for i in range(start, N+1):
        res.append(i)
        recur(i)
        res.pop()


recur(1)