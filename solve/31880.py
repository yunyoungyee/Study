import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int, input().split())
sum = 0
a=list(map(int, input().split()))
b=list(map(int, input().split()))
for i in a:
    sum += i
for j in b:
    if(j!=0):
        sum *= j
print(sum)

# 주사위의 개수는 1 3 6 n(n+1)/2
# 1층은 1-5
# 2층은 주사위 1층 결과 + 3개-1층 개수(1개)*4면 + 1층 개수(1-2, 2-4, 1-5(1층)
# 3층은 주사위 