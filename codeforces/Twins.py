# https://codeforces.com/contest/160/problem/A

n = int(input())
C = list(map(int, input().split()))

C.sort(reverse=True)

half = sum(C) / 2
s = 0

cnt = 0
for i in C:
    s += i
    cnt += 1
    if s > half:
        break

print(cnt)

'''
# 최소 동전 개수로 동생보다 큰 금액 가져가기
'''
