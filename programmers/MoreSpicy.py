import heapq

def solution(S, k):
    cnt = 0
    heapq.heapify(S)
    while True:
        if S[0] >= k:
            return cnt
        elif len(S) == 1:
            return -1
        
        mix = heapq.heappop(S) + heapq.heappop(S) * 2
        heapq.heappush(S, mix)
        cnt += 1
    
''' 42626 
# 가장 작은 값 두개의 스코빌지수(mix)를 계산해서 모든 원소가 k이상이 되는지 구하는 문제 - heap
'''
