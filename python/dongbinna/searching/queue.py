from collections import deque
dq = deque()

#파이썬은 deque ==> 시간복잡도 O(1)
# 5 2 3 7 - 1 4 - 

dq.append(5)
dq.append(2)
dq.append(3)
dq.append(7)
dq.popleft()
dq.append(1)
dq.append(4)
dq.popleft()

print(dq)
dq.reverse()
print(dq)