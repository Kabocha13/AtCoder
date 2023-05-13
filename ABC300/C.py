# https://atcoder.jp/contests/abc300/tasks/abc300_c
# 制約を見れば#を見つけたらとにかく右下に何個連なってるか数える
# その値の最大値が答えになることがわかる
# 探索済みの#を他の文字列に変えなければ重複して計算してしまう

import sys

H, W = map(int, input().split())
g = []
for i in range(H):
    g.append(input().strip())

def ok(i, j):
    return 0 <= i < H and 0 <= j < W

def test(i, j, d):
    for x in [+d, -d]:
        for y in [+d, -d]:
            s, t = i + x, j + y
            if not ok(s, t) or g[s][t] != '#':
                return False
    return True

N = min(H, W)
ans = [0] * (N + 1)

for i in range(H):
    for j in range(W):
        if g[i][j] != '#':
            continue
        if test(i, j, 1):
            d = 1
            while test(i, j, d + 1):
                d += 1
            ans[d] += 1

for i in range(1, N + 1):
    print(ans[i], end=' ' if i < N else '\n')
