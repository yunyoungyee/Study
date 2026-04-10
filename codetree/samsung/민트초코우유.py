# N*N (1,1)시작
# T:민트 C:초코 M:우유 TC TM CM TCM 가능
# F:초기 신봉음식 B:신앙심
# T일동안 아침 점심 저녁
# 아침: 신앙심+=1 그래서 모든 (i,j)에 +1
# 점심: 상하좌우로 붙어있는 1그룹 F가 같아야 그룹형성 / 대표자 선정(r,c) / 기준? 신앙심 큰사람 -> r작은사람 -> c작은사람
# 대표자:그룹원 -1 만큼 신앙심 추가 그룹원: -1
# 저녁: 단일,이중,삼중 3개 그룹 / 순서는 대표자 중 신앙심 큰사람 -> r작은사람 -> c작은사람

# 간절함:x x=B(신앙심)-1
# 방향: B%4한 나머지인데 
# dx=[0,0,-1,1]
# dy=[-1,1,0,0]
# 격자 밖or x==0 종료
# 전파음식==신봉음식:
#     continue
# x>y(전파대상 신앙심) 강한전파 
# 전파대상의 기존F.pop() : 기존껀 제거
# 전파대상의 기존F에.append(전파자 F) : 전파자꺼 추가
# -> 전파자=x - y(전파대상 신앙심)+1 , 전파대상 신앙심(y)+=1
# 이때, 전파자x == 0 종료

# x<=y(전파대상 신앙심) 약한 전파
# 전파대상의 기존F.append(전파자 F) : 전파대상+전파자 F
# -> 전파자x=0, y(전파대상 신앙심)+x

import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

N, T = map(int,input().split())
food=[]
mapping = {'T':1,'C':2, 'M':4, 'TC':3, 'TM':5, 'CM':6, 'TCM':7}
for _ in range(N):
    row = input().strip()
    food.append([mapping[r] for r in row])
B=[list(map(int,input().split())) for _ in range(N)]
visited=[[False]*N for _ in range(N)]
lead=[]
dx=[0,0,-1,1]
dy=[-1,1,0,0]

def morning():
    for j in range(N):
        for i in range(N):
            B[j][i]+=1
def bfs(y,x):
    queue=deque()
    queue.append((y,x))
    visited[y][x]=True
    group=[(y,x)] #대표자한테 신앙심을 주고 빼려면 같은 그룹을 따로 저장해야함.
    tmp=B[y][x]
    ty, tx = y, x
    while queue:
        ey, ex = queue.popleft()

        for i in range(4):
            ny=ey+dy[i]
            nx=ex+dx[i]
            if 0<=ny<N and 0<=nx<N:
                if visited[ny][nx]==False and food[ny][nx]==food[y][x]:
                    visited[ny][nx]=True
                    queue.append((ny,nx))#이동을 위한
                    group.append((ny,nx))#그룹저장을 위한
                    if B[ny][nx] > tmp:
                        tmp = B[ny][nx]
                        ty, tx = ny, nx
                    elif B[ny][nx] == tmp:
                        if ny<ty or (ny==ty and nx<tx):
                            ty, tx = ny, nx
    return group,(ty,tx)
                


def lunch():
    global B, visited, lead
    visited=[[False]*N for _ in range(N)]
    lead=[]

    for y in range(N):
        for x in range(N):
            if visited[y][x]==False:
                group, (ty,tx) = bfs(y,x) #같은 그룹 찾기(BFS)

                #대표자 몰아주고 그룹원 -1
                for gy,gx in group:
                    if (gy,gx)!=(ty,tx):
                        B[gy][gx]-=1
                        B[ty][tx]+=1
                lead.append((ty,tx,food[ty][tx],B[ty][tx]))
    return lead

def dinner():
    global B, food, lead

    # 1️⃣ 그룹 나누기
    single = []
    double = []
    triple = []

    for y, x, state, belief in lead:
        if state in (1, 2, 4):
            single.append((y, x, state, belief))
        elif state in (3, 5, 6):
            double.append((y, x, state, belief))
        else:
            triple.append((y, x, state, belief))

    # 2️⃣ 정렬
    def sort_func(arr):
        arr.sort(key=lambda item: (-item[3], item[0], item[1]))

    sort_func(single)
    sort_func(double)
    sort_func(triple)

    # 3️⃣ 전파
    blocked = [[False]*N for _ in range(N)]

    for arr in (single, double, triple):
        for y, x, state, belief in arr:

            if blocked[y][x]:
                continue

            d = belief % 4
            power = belief - 1

            B[y][x] = 1  # 전파자는 1만 남김

            ny, nx = y, x

            while True:
                ny += dy[d]
                nx += dx[d]

                # 종료 조건
                if not (0 <= ny < N and 0 <= nx < N):
                    break
                if power == 0:
                    break

                # 같은 음식이면 패스
                if food[ny][nx] == state:
                    continue

                target = B[ny][nx]

                # 강한 전파
                if power > target:
                    food[ny][nx] = state
                    power -= (target + 1)
                    B[ny][nx] += 1

                # 약한 전파
                else:
                    food[ny][nx] |= state
                    B[ny][nx] += power
                    power = 0

                # 방어 상태
                blocked[ny][nx] = True
    
            
def result():
    res = [0]*8  # 0~7
    for y in range(N):
        for x in range(N):
            res[food[y][x]] += B[y][x]

    # 출력 순서
    print(
        res[7],  # 민트초코우유
        res[3],  # 민트초코
        res[5],  # 민트우유
        res[6],  # 초코우유
        res[4],  # 우유
        res[2],  # 초코
        res[1]   # 민트
    )

for _ in range(T):
    morning()
    lunch()
    dinner()
    result()