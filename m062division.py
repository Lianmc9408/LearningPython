# 无冲突子集问题
# A = {0,1,2,3,4,5,6,7,8}
# R = {(1,4),(4,8),(1,8),(1,7),(8,3),(1,0),(0,5),(1,5),(3,4),(5,6),(5,2),(6,2),(6,4)}
# A 为代表N种动物的集合  R 为冲突关系集合
# 解法：
# 把所有动物按次序入队
# 创建一个笼子（集合）， 出队一个动物，
# 如果和笼子内动物无冲突，则添加到该笼子，有冲突则添加到队尾，等待进入新笼子
# 由于队列先进先出的特性，如果当前出队动物的index，不大于其前一个出队动物的index
# 说明当前队列中所有动物已经尝试过进入且进入不了当前笼子，此时创建新的笼子（集合）

from collections import deque


def devision(a, r):
    res = []
    q = deque(range(len(a)))
    pre = len(a)

    while q:
        cur = q.popleft()
        if cur <= pre:
            res.append([])

        for i in res[-1]:
            if (cur, i) in r or (i, cur) in r:
                q.append(cur)
                break
        else:
            res[-1].append(cur)
        pre = cur
    return res


if __name__ == '__main__':
    A = {0, 1, 2, 3, 4, 5, 6, 7, 8}
    R = {(1, 4), (4, 8), (1, 8), (1, 7), (8, 3), (1, 0), (0, 5), (1, 5), (3, 4), (5, 6), (5, 2), (6, 2), (6, 4)}

    print(devision(A, R))
