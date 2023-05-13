# https://atcoder.jp/contests/abc301/tasks/abc301_a
n = int(input())
s = input()
if s.count("T")<s.count("A"):
  print("A")
elif s.count("A")==s.count("T"):
  if s[-1]=="A":
    print("T")
  else:
    print("A")
else:
  print("T")
