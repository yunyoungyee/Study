import sys
input = lambda: sys.stdin.readline().rstrip()
N, K = map(int,input().split())

def fac(n):
    res=1
    for i in range(1, n+1):
        res*=i
    return res

a= fac(N)
b= fac(N-K)
c= fac(K)
print(a//(b*c))