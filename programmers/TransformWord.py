from collections import deque

def solution(begin, target, words):
    n = len(words)
    V = [False] * n
    
    q = deque([(begin, 0)])
    while(q):
        print(q)
        cur, depth = q.popleft()
        
        if cur == target:
            return depth
        
        for i, next in enumerate(words):
            if not V[i] and isTransform(cur, next):
                V[i] = True
                q.append((next, depth+1))
                
    return 0    
        
def isTransform(A, B):
    cnt = 0
    for a, b in zip(A, B):
        if a != b:
            cnt += 1

    return True if cnt == 1 else False
