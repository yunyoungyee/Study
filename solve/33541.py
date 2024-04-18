import sys
input = lambda: sys.stdin.readline().rstrip()
X = int(input())
while(1):
    X+=1
    a = (X)//100
    b = (X)%100
    if X>9999:
        print(-1)
        break
    elif ((a+b)*(a+b) == X):
        print(X)
        break