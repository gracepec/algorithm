from collections import deque

n = int(input())
P = list(map(int, input().split()))

q = deque(P)
st = deque()

turn = 1
while q:
    p = q.popleft()
    if p == turn:
        turn += 1
    else:
        st.append(p)

    while st:
        if st[-1] == turn:
            st.pop()
            turn += 1
        else:
            break

ans = "Sad" if q or st else "Nice"
print(ans)

''' 12789
# 도키도키 간식드리미: T자 길에서 순서대로 간식받기 - Queue, Stack
'''
