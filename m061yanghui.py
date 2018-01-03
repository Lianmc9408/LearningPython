# 杨辉三角（二项式系数表）
#       1
#      1 1
#     1 2 1
#    1 3 3 1
#   1 4 6 4 1
# ..............
# 第n层为(a+b)**n 的每一项系数


from collections import deque


def yanghui(k):
    q = deque([1])

    for i in range(k):
        for j in range(i):
            q.append(q.popleft() + q[0])
        q.append(1)

    return q


if __name__ == '__main__':
    for i in range(5):
        print(yanghui(i))
