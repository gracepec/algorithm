import sys
input = sys.stdin.readline

n, maxw = map(int, input().split())
W = [0] * n
V = [0] * n
for i in range(n):
    P = tuple(map(int, input().split()))
    W[i] = P[0]
    V[i] = P[1]
    
D = [[0] * (n+1) for _ in range(maxw+1)]
for i in range(n):
    for wi in range(maxw):
        if wi < W[i]:
            D[i][wi] = D[i-1][wi]
        else:
            D[i][wi] = max(D[i-1][wi],  D[i-1][wi-W[i]] + V[i])
        print(D)
print(D[n][maxw])
        
    
'''12865
# 배낭문제 - DP

    """
        n, k = map(int, input().split())
        items = [tuple(map(int, input().split())) for _ in range(n)]
        
        # DP 테이블 초기화: (n+1) x (k+1)
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # DP 진행
        for i in range(1, n + 1):
            weight, value = items[i - 1]
            for w in range(k + 1):
                if w < weight:
                    dp[i][w] = dp[i - 1][w]  # 현재 물건을 넣을 수 없는 경우
                else:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
                
        # 정답은 마지막 칸
        print(dp[n][k])
    """
'''
