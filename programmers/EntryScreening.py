def solution(n, T):
    l, r = 1, max(T) * n
    res = r
    
    while l <= r:
        mid = (l + r) // 2
        p = sum(mid // t for t in T)
        
        if p >= n:
            res = mid
            r = mid - 1
        else:
            l = mid + 1
    
    return res

''' 43238
# 입국심사 줄을 최대한 빨리 줄이기 - 이진탐색 (binary search)
 -> p: mid시간에 예상되는 최대의 통과 사람수 (걸린시간 mid에서 각 심사대 시간을 나누어 합하는)
    p가 실제 기다리는 사람 n보다 크거나 같으면 통과 가능 + 더 짧게 걸릴수도 -> r줄여
    p < n : 시간 더 필요 -> l 떙겨서
'''
