# 해당 문제는 퀸을 놓는 자리가 중요한데 행은 인자에, 열은 for문에 녹여낸 문제임.
# 특히 재귀함수의 depth로 알아서 방문 관리가 되기 때문에 visited 배열이 필요 없음.
# 전체적인 그림은 0번째 행부터 잡아놓고 내려가면서 열과 대각선을 확인하여 퀸을 놓는 것인데, 중요한 점이 3개 있음.
# 1. 0~7열까지 퀸의 공격 범위인지 확인하는 배열 필요 -> col 배열
# 2. "\" 모양 대각선이 퀸의 공격 범위인지 확인하는 배열 필요 -> rb_line
# 해당 대각선의 특징은 행과 열을 뺀 값이 항상 동일하다는 것
# 3. "/" 모양 대각선이 퀸의 공격 범위인지 확인하는 배열 필요 -> lb_line
# 해당 대각선의 특징은 행과 열을 더한 값이 항상 동일하다는 것

# 이렇게 3가지 요소를 key point로 재귀함수를 타고 y==N인 경우, 
# 즉 가장 끝 행에 도달한 경우 퀸을 N개 다 놓았기 때문에 경우의 수를 1개 증가시킴.
import sys
input = lambda: sys.stdin.readline().rstrip()
N = int(input())
col = [False]*N
rb_line = [False]*(2*N)
lb_line = [False]*(2*N)
cnt=0
# col=y row=x
def recur(y):
    global cnt
    if y==N:
        cnt+=1
        return
    for i in range(N):
        if col[i] or rb_line[y-i+N] or lb_line[y+i]:
            continue
        col[i] =True
        rb_line[y-i+N]=True
        lb_line[y+i]=True

        recur(y+1)
        
        col[i] =False
        rb_line[y-i+N]=False
        lb_line[y+i]=False

recur(0)

print(cnt)
