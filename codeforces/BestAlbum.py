import heapq
from collections import defaultdict

def solution(genres, plays):
    answer = []
    
#     S = set(genres)
#     Dic = {key: [] for key in S}
    Dic = defaultdict(list)
    
    for i, (g, p) in enumerate(zip(genres,plays)):
        heapq.heappush(Dic[g], (-p, i))
    
    sorD = sorted(Dic.items(), key=lambda x: sum(p for p, _ in x[1]))
    
    for gen, song in sorD:
        for _ in range(2):
            if song:
                idx = heapq.heappop(song)[1]
                answer.append(idx)
        
    return answer

''' 42579
# dict로 묶어 합산으로 정렬 후 그 중 큰 수부터 최대 2개까지 pop하는 문제 - dict, heap, sort

defaultdict(type): 없는 키를 받아도 자동 생성하는 dict -> 안쓰려면 주석처럼 set()으로 초기화 가능
'''
