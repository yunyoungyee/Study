import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
count=0
for _ in range(N):
    c = input()
    if c==c[::-1]:
        count+=1

print(count)