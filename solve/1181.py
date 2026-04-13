
#처음 접근 방식
#너무 과함. 길이별 버킷에 set에 이중 정렬을 하고 있음.
# N = int(input())
# word=[[]for _ in range(51)]
# tmp=set()
# for i in range(N):
#     w=input()
#     if word[len(w)].count(w) < 1:
#         word[len(w)].append(w)
#         tmp.add(len(w))
# tmp=list(tmp)
# tmp.sort()
# for n in tmp:
#     word[n].sort()
#     for i in range(len(word[n])):
#         print(word[n][i])

#배운 사실 
# 1. sort()는 사전순으로 정렬해줌 
# 2. sort()는 sort(key=함수, reverse=True/False) 
# 이렇게 key에 정렬기준을, reverse에 내림차순 여부를 정할 수 있다.
N = int(input())
word=list(set(input() for _ in range(N)))
word.sort()
word.sort(key=len)
for w in word:
    print(w)