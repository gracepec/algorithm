from collections import deque
import sys
input = sys.stdin.readline

ladder = []
snake = []

G = []

n, m = map(int, input().split())
for _ in range(n):
    x, y = map(int, input().split())
    ladder.append((x,y))
for _ in range(m):
    u, v = map(int, input().split())
    snake.append((u,v))

ladder.sort()

q = deque([1])
while q:
    cn = q.popleft()
    while cn < ladder[0][0] <= cn+6:
        x, y = ladder.pop(0)
        q.append(y)
    i = 6
    while not cn+i in q or i != 0:
        i -= 1
    q.append(cn+i)
    ...

'''
3 _
2 80
5 40
42 93
45 95
_

-> 5 40 45 95
'''
