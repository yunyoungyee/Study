#택배 승차 c:택배 왼쪽 열 위치 w:택배 가로 크기 h:택배 세로 크기 k:택배 번호
#택배 하차 (왼쪽), k가 작은 순, 택배 1개 빼면 공간 남아있을 때 떨어짐.
#택배 하차 (오른쪽), 동일
#이랬을 때 택배의 번호 순서대로 출력
import sys
input = lambda: sys.stdin.readline().rstrip()
N, M = map(int,input().split())
graph=[[0]*(N+1) for _ in range(N+1)]
area = dict() #택배번호로 그 번호가 가진 위치(택배 점유 위치)를 뽑아내기 위함
# 택배 상차
for _ in range(M):
    # 3 1 2 3
    K, H, W, C = map(int,input().split())
    tmp=[]
    for i in range(C,C+W):
        for j in range(1,N+1):
            if graph[j][i]!=0:
                tmp.append(j-1)
                break
        else:
            tmp.append(N)
    base = min(tmp)
    area[K] = []
    for i in range(C,C+W):
        for j in range(base,base-H,-1):
            if j < 1:
                break
            graph[j][i]=K
            area[K].append((j,i))

def left_choice(K):
    for (y,x) in area[K]:
        for nx in range(1,x):
            if graph[y][nx]!=0 and graph[y][nx]!=K:
                return False
    return True

def right_choice(K):
    for (y,x) in area[K]:
        for nx in range(x+1,N+1):
            if graph[y][nx]!=0 and graph[y][nx]!=K:
                return False
    return True

def remove(K):
    for (y,x) in area[K]:
        graph[y][x]=0
    del area[K]

def drop_dist(K):
    min_dist = N
    for (y,x) in area[K]:
        dist = 0
        ny = y+1
        while ny <= N and(graph[ny][x] == 0 or graph[ny][x] == K):
            dist += 1
            ny += 1
        min_dist = min(min_dist, dist)

    return min_dist

def drop(K, dist):
    for (y,x) in area[K]:
        graph[y][x]=0
    new_pos = []
    for (y,x) in area[K]:
        graph[y+dist][x]=K
        new_pos.append((y+dist,x))
    area[K]=new_pos

def gravity():
    while True:
        moved=False

        for K in area:
            dist=drop_dist(K)
            if dist>0:
                drop(K, dist)
                moved=True
        if not moved:
            break


# 택배 하차
left_turn = True
remain = set(area.keys())
while remain:
    candidate=[]
    # 1.왼쪽 뺄 택배 번호 찾기(뺄 수 있는게 없어? 그러면 넘겨)
    if left_turn:
        for k in remain:
            if left_choice(k):
                candidate.append(k)
    # 2.오른쪽 뺄 택배 번호 찾기(뺄 수 있는게 없어? 그러면 넘겨)
    else:
        for k in remain:
            if right_choice(k):
                candidate.append(k)
    # 3.택배 제거하기
    if candidate:
        remove_box = min(candidate) #제거 후보군 중에 가장 작은 택배번호 k 찾기
        remove(remove_box) #택배 제거 함수에 넣어서 0으로 돌려놓기
        remain.remove(remove_box) #남은 택배 set에서 뺀 택배 지우기
        # 4.중력 적용해서 재배치하기
        gravity()
        # 5.제거한 택배 출력하기
        print(remove_box)
    # left_turn = not left_turn
    left_turn = not left_turn