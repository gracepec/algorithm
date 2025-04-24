from collections import deque

def solution(M):
    lx = len(M)
    ly = len(M[0])

    q = deque()
    q.append((0, 0))
    
    Dx = [1, -1, 0, 0]
    Dy = [0, 0, 1, -1]
        
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(Dx, Dy):
            xn = x + dx
            yn = y + dy
            
            if not (0 <= xn < lx and 0 <= yn < ly):
                continue
            
            if M[xn][yn] == 1:
                q.append((xn, yn))
                M[xn][yn] = M[x][y] + 1
                
            if xn == lx-1 and yn == ly-1:
                return M[xn][yn]
                
    return -1

''' 1844
# 게임 맵 최단거리 (0,0부터 상하좌우 한칸씩 이동하며 m,n까지 도달할 최단거리 구하기) - BFS
 -> queue 활용하여 상하좌우 가보고 인덱스가 벗어나거나 벽(0)이 아니면(1) append하고 이동칸에 이동횟수 누적 +1
    다음 반복(while)은 q에 popleft이기에 너비우선 최단거리 BFS 계산이 됨.
    목적지(n,m)에 도달하면 리턴. 끝까지 도달 못하면 종료 후 -1 리턴
'''
