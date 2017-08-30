from collections import deque

# Queue is first element added is the first element retrieved
queue = deque([1,2,3,4,5,6])
first = queue.popleft()
second = queue.popleft()
print first,second
print queue