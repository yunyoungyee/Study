# 해당 문제는 치킨집과 가정집이 명확하게 지도에 1과 2로 표기가 되기 때문에
# 각각 배열에 좌표 정보를 저장하고 거기에서만 찾아서 거리 계산을 해야 시간 단축이 가능함.
# 추가로 치킨집을 먼저 백트래킹으로 고르는데, 이때 순열이 아닌 조합으로 치킨집은 순서가 상관없으니
# 그렇게 골라서 고른 치킨집 배열을 또 저장하고, 
# 가정집 배열을 앞에서부터 돌면서 고른 치킨집 배열하고 거리 계산을 하여 가정집마다 "치킨거리"를 구하는 문제임.
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
MAP = [list(map(int,input().split())) for _ in range(N)]
chicken=[]
house=[]
chicken_list=[]
res=[]

for j in range(N):
    for i in range(N):
        if MAP[j][i]==2:
            chicken.append((j,i))
        elif MAP[j][i]==1:
            house.append((j,i))

def dist(c_list):
    dist_sum=0
    for hy,hx in house:
        dist_min=[]
        for cy,cx in c_list:
            dist_min.append(abs(hy-cy)+abs(hx-cx))
        dist_sum+=min(dist_min)
    return dist_sum


def recur(start):
    if len(chicken_list)==M:
        res.append(dist(chicken_list))
        return

    for i in range(start,len(chicken)):
            chicken_list.append(chicken[i])
            recur(i+1)
            chicken_list.pop()
        
recur(0)
print(min(res))