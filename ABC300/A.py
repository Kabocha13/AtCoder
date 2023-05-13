# https://atcoder.jp/contests/abc300/tasks/abc300_a
# .indexで配列の中の位置を検索するやつを使う！

n,a,b = map(int,input().split())
c = list(map(int,input().split()))
print(c.index(a+b)+1)
