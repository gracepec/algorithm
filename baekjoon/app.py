import sys
input = sys.stdin.readline

n, p = map(int, input().split())
M = list(map(int, input().split()))
C = list(map(int, input().split()))

D = [0] * 10005
fup = C[0]
for i in range(n):
    fi = fup
    for ci in range(fi, -1, -1):
        if D[ci] != 0:
            D[ci+C[i]] = max(D[ci+C[i]], D[ci]+M[i])
            fup = max(fup, ci+C[i])
    D[C[i]] = max(D[C[i]], M[i])

for i in range(fup+1):
    if D[i] >= p:
        print(i)
        break

'''7579
# 주어진 메모리를 확보하기 위한 최소비용 계산 - DP + 배낭문제 활용
 - D: 비용을 인덱스로 가지는 최대 메모리 (비어있는 인덱스 많음)
 - fup : D의 finish index를 업데이트 하는 변수

n=5 p=60
M 30 10 20 35 40
C 3  0  3  5  4

  0  3  3  4  5
  10 20 30 40 35
D [0][1][2][3][4]
0 10 
1 
2 
3     30 40
4           50
5              45
6        60  <- P랑 크거나같 나오면 이 아래 계산할 필요 X
7          (80)
8
9
10        (100X)

(비어있는 인덱스) 0이면 계산x
'''
