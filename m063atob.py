# 对于一对正整数a,b,对a只能进行加1，减1，乘2操作，问最少对a进行几次操作能得到b?
from collections import deque


def atob(a, b):
    q = deque([(a, 0)])
    had_atob = {a}
    while True:
        s, c = q.popleft()
        # 别人写的
        if s == b:
            return c
        if s < b:
            if s + 1 not in had_atob:
                had_atob.add(s + 1)
                q.append((s + 1, c + 1))
            if s * 2 not in had_atob:
                had_atob.add(s * 2)
                q.append((s * 2, c + 1))
        if s > 0:
            if s - 1 not in had_atob:
                had_atob.add(s - 1)
                q.append((s - 1, c + 1))

        # 自己写的，烂！
        # if s == b:
        #     return c
        # if s + 1 == b:
        #     return c + 1
        # elif s + 1 not in had_atob and s < b:
        #     had_atob.add(s + 1)
        #     q.append((s + 1, c + 1))
        # if s - 1 == b:
        #     return c + 1
        # elif s - 1 not in had_atob and s > 0:
        #     had_atob.add(s - 1)
        #     q.append((s - 1, c + 1))
        #
        # if s * 2 == b:
        #     return c + 1
        # elif s * 2 not in had_atob and s < b:
        #     had_atob.add(s * 2)
        #     q.append((s * 2, c + 1))


if __name__ == '__main__':
    print(atob(3, 11))
    print(atob(5, 8))
