import heapq

def solution(J):
    n = len(J)
    J.sort(reverse=True)
    
    H = []
    fin = 0
    total = 0
    while J or H:
        if not H:
            heapq.heappush(H, J.pop()[::-1])
            
        load, req = heapq.heappop(H)
        fin = load + (req if req > fin else fin)
        total += fin - req
        
        while J and fin >= J[-1][0]:
            heapq.heappush(H, J.pop()[::-1])
    
    return total // n

''' 42627
# 우선순위 디스크 컨트롤러 작업 처리 - heap
    -> 대기 큐(힙)에 작업이 끝나는 시간까지의 요청을 push하고 하나씩 pop하면서 업데이트 (힙과 jobs에 아무것도 안남을때까지)

fin: finsih time: 현재 작업이 끝나는 시점
total: 리턴을 위해 작업들의 총 반환 시간 합
load: 해당 작업의 진행 소요시간 == J[i][0]
req: request: 해당 작업의 요청시간
'''
