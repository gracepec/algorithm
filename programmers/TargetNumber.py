def dfs(N, t, idx, sum):
    if idx == len(N):
        return 1 if sum == t else 0

    return dfs(N, t, idx+1, sum + N[idx]) + \
           dfs(N, t, idx+1, sum - N[idx])

def solution(N, t):
    return dfs(N, t, 0, 0)
    
''' 43165
# N의 순서로 더하거나 빼서 t를 만들수 있는 방법의 수 - DFS
 -> idx: N 인덱스 진행, sum: 지금까지 더하거나 빼면서 온 값
    (종료조건) idx가 N의 마지막 원소까지 갔을 때
    (반환조건) 최종 sum이 t와 같다면 만들 수 있는 방법의 수 += 1 아니면 0
    
    모든 경우의 수 가보는 것. 그 중 sum==t 나오는 성공 횟수 더하면서 리턴.
'''
