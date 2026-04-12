# 최대공약수는 유클리드 호제법으로 구함
# -> 큰 수를 작은 수로 나눈 나머지로 계속 바꿔가면, 결국 최대공약수가 남는다
# 최소공배수는
# -> A*B//최대공약수 
A, B = map(int,input().split())
max_gong = 0
min_gong = 0

def gcd(a,b): #유클리드 호제법
    while b!=0:
        a,b=b,a%b
    return a

def lcm(a,b,max_gong):
    return a*b//max_gong

if A>B:
    max_gong=gcd(A,B)
else:
    max_gong=gcd(B,A)
min_gong=lcm(A,B,max_gong)

print(max_gong)
print(min_gong)
