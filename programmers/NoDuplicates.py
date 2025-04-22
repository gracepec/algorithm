def solution(arr):
    res = []
    for a in arr:
        if not res or res[-1] != a:
            res.append(a)
    return res

''' 12906
# 같은 숫자는 싫어 - stack
'''
