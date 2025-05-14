from collections import deque

def solution(bridge_len, weight, truck_wei):
    T = deque(truck_wei)
    B = deque([0] * bridge_len)
    time = 0
    now_wei = 0
    
    while T:
        time += 1
        now_wei -= B.popleft()
        if now_wei+T[0] <= weight:
            t = T.popleft()
            B.append(t)
            now_wei += t
        else:
            B.append(0)
    
    return time + bridge_len

''' 42583
# 다리를 지나는 트럭 - queue
    -> 시간의 흐름에 따라 반복문 통과 (트럭이 못올라가면 append(0))

    *반복문 안에서 sum() 쓰면 테스트케이스 하나 시간초과 -> now_wei 변수로 따로 관리
'''
