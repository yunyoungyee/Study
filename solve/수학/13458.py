N=int(input())
tester=list(map(int,input().split()))
M, S = map(int,input().split())
cnt=0
for i in tester:
    if i<=M:
        cnt+=1
    else:
        i-=M
        cnt+=1
        if i%S==0 and i<S:
            cnt+=1
        elif i%S==0 and i>=S:
            cnt+=(i//S)
        else:
            cnt+=(i//S+1)
print(cnt)