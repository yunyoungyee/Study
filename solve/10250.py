import sys
input = lambda: sys.stdin.readline().rstrip()
T = int(input())
for _ in range(T):
    H, W, N = map(int,input().split())
    if(N%H==0):
        xx=N//H
        yy=H*100
    else:
        xx=N//H+1
        yy=N%H*100
    print(xx+yy)