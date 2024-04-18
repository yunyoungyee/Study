import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
A,B = 0, 0
for a in range(N):
    col = input()
    if(col=="yonsei"):
        A=a
    elif(col=="korea"):
        B=a
    elif(A!=0 and B!=0):
        exit
if(A<B):
    print("Yonsei Won!")
else:
    print("Yonsei Lost...")