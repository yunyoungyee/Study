N = int(input())
member=[]
for _ in range(N):
    k, v = input().split()
    member.append((k,v))
member.sort(key=lambda x: x[0])
for k, v in member:
    print(k, v)
# member={}
# for _ in range(N):
#     member