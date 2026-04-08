# 해당 문제는 같은 depth에서 중복값을 사용하는것만 막으면 되는 문제였음.
# 특히, 순서가 중요한 순열이라 visited배열을 썼는데 순열에 사용할 값을 직접 입력 받은 배열이 있기 때문에
# visited 배열을 실제 값 기준으로 쓰는 것이 아닌 인덱스 기준으로 써야하는게 key point임.
# 또한 prev 값을 두고 이전 for문 안쪽(=같은 depth)에서 중복값을 사용하는 것을 막는게 2번째 key point임.
# 그래서 for문을 다 돌고나오면 depth가 달라지니까 prev=0으로 초기화하는 것임.
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
comb = list(map(int,input().split()))
comb.sort()
visited=[False]*N
res = []
# 1 7 9 9 
def recur():
    if len(res) == M:
        print(*res)
        return
    prev = 0 #아래 depth에서 중복만 막도록 했으면 위에선 초기화
    for i in range(N):
        if visited[i]== False and comb[i]!=prev:
            visited[i]=True
            res.append(comb[i])
            prev=comb[i]
            recur()
            visited[i]=False
            res.pop()

recur()