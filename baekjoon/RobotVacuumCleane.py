import sys
input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

room = [[] for i in range(n)]
for i in range(n):
    ln = list(map(int, input().split()))
    room[i] = ln

# d방향의 후진 이동 idx
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def run(cx, xy, d):
    room[cx][cy] = 2 # 1번 조건

    if isClean(): # 2번 조건
        if not isWallBehind():
            run(cx + dx[d], cy + dy[d], d)
    else: # 3번 조건
        if 


    def dirtySpace(): # isClean bool로 리턴? 아예 3조건에 맞게 반시계 인덱스 반환?
        for i in range(4):
            if room[cx + dx[i]][cy + dy[i]] == 0:
                return i
        return -1

    def isWallBehind():
        if room[cx + dx[d], cy + dy[d]] == 1:
            return true
        return false
        
