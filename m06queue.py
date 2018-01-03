from collections import deque

q1 = deque()
q2 = deque([1, 2, 3])
q3 = deque([1, 2, 3], 5)


q1.append(2)
print(q1)
q1.append(3)
print(q1)
q1.appendleft(5)
print(q1)

q1.extend([6, 7])
print(q1)
q1.extendleft([9, 10])
print(q1)

q1.pop()
print(q1)
q1.popleft()
print(q1)

print(q1.maxlen)
print(q3.maxlen)
print(len(q3))

q1.clear()
print(q1)

# 判断队列为满
q3.maxlen == len(q3)

# 队列中值为4的个数
print(q3.count(3))

# 移除队列中最左边开始第一个值为3的元素
q3.remove(3)

q3.reverse()

# 把最右端的1个值放到最左边
q3.rotate(1)
# 把最左端的1个值放到最右边
q3.rotate(-1)

