import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    sum = 0
    n=M-N+1
    if(N==1):
        print(M)
    else:
        for _ in range(M-N):
            sum+=n*(n+1)/2
            n-=1
    print(sum)