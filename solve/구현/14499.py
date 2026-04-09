# 해당 문제는 주사위의 기본값을 정해놓고, 동/서/북/남 방향에 따른 주사위 이동을
# 정해두면 해결되는 문제임.
# 명령에 따라 주사위를 굴리게 되는데, 그 때 방향에 따라 주사위 리스트를 수정하고,
# 수정된 주사위를 가지고 바닥은 분기조건에, 위는 출력에 그대로 사용하면 됨.
# 처음 주사위 상태를 회전방향에 따라 계속 주사위 상태 업데이트를 해주면서 푸는 문제임.
import sys
input = lambda: sys.stdin.readline().rstrip()

N, M, Y, X, K = map(int,input().split())
MAP=[list(map(int,input().split()))for _ in range(N)]
ORDER=list(map(int,input().split()))

dice=[0]*6
dx=[1,-1,0,0]
dy=[0,0,-1,1]

def roll(order):
    top, bottom, north, south, west, east = dice #초기값
    
    
    if order == 1:  # 동
        dice[0] = west
        dice[1] = east
        dice[4] = bottom
        dice[5] = top
        dice[2] = north
        dice[3] = south

    elif order == 2:  # 서
        dice[0] = east
        dice[1] = west
        dice[4] = top
        dice[5] = bottom
        dice[2] = north
        dice[3] = south

    elif order == 3:  # 북
        dice[0] = south
        dice[1] = north
        dice[2] = top
        dice[3] = bottom
        dice[4] = west
        dice[5] = east

    elif order == 4:  # 남
        dice[0] = north
        dice[1] = south
        dice[2] = bottom
        dice[3] = top
        dice[4] = west
        dice[5] = east
for order in ORDER:
    ny=Y+dy[order-1]
    nx=X+dx[order-1]

    if not (0<=ny<N and 0<=nx<M):
        continue
    Y, X = ny, nx
    roll(order)

    if MAP[Y][X] == 0:
        MAP[Y][X] = dice[1]
    else:
        dice[1]=MAP[Y][X]
        MAP[Y][X]=0
    print(dice[0])