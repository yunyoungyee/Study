# 해당 문제는 순열에 사용할 값을 입력받는 것으로 순열용 배열이 필요하고, 정렬을 해서 사용해야함.
# 기존과는 다르게 1부터 증가하는것이 아니기에 for문 i를 index로 써야 하는 문제임.
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
comb = list(map(int,input().split()))
comb.sort()
res = []
visited=[False]*(max(comb)+1)

def recur(num):
    if len(res) == M:
        print(*res)
        return
    for i in range(len(comb)):
        if visited[comb[i]]==False:
            visited[comb[i]]=True
            res.append(comb[i])
            recur(comb[i])
            visited[comb[i]]=False
            res.pop()


recur(comb[0])
