# https://atcoder.jp/contests/abc301/tasks/abc301_b
# 一文字ずつ調べてあってるならansにそのまま入れて違うならその差を一つづつansに入れる

n = int(input())
a = list(map(int,input().split()))
ans = [a[0]]

for i in range(1,len(a)):
    if abs(ans[-1] - a[i]) == 1:
        ans.append(a[i])
    else:
        if ans[-1] < a[i]:
            for j in range(ans[-1]+1, a[i]):
                ans.append(j)
            ans.append(a[i])
        else:
            for j in range(ans[-1]-1, a[i], -1):
                ans.append(j)
            ans.append(a[i])
print(*ans)
