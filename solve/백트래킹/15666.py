# 해당 문제는 중복선택은 가능하지만 같은 depth에서 중복값을 사용하는것을 막으면서 시작값을 신경써야하는 문제였음.
# 따라서 prev 값을 두고 이전 for문 안쪽(=같은 depth)에서 중복값을 사용하는 것을 막아야 했고,
# start로 시작 위치를 옮겨야 했는데, 재귀함수를 부를 때 실제 값이 아닌 i값을 써야하는걸 혼동하지 말 것.
# 왜냐하면 for문 i값이 순차적으로 증가하는 걸 어차피 사용할건데 시작값도 정해서 옮겨주고 있으니 그대로 쓰면 됨.
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
res=[]
comb = list(map(int,input().split()))
comb.sort()

def recur(start):
    if len(res)==M:
        print(*res)
        return
    prev=0
    for i in range(start,N):
        if prev!=comb[i]:
            res.append(comb[i])
            prev = comb[i]
            recur(i)
            res.pop()

recur(0)
