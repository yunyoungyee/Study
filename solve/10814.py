# sort(key)에다가 정렬 기준을 lambda를 써서 x값으로 정렬하자는 건데,
# 그걸 x[0]으로 한 이유는 key값으로 정렬을 하고 싶은데 튜플이라서 저렇게 접근하는 것임.
N = int(input())
member=[]
for _ in range(N):
    k, v = input().split()
    member.append((int(k),v))
member.sort(key=lambda x: x[0])
for k, v in member:
    print(k, v)