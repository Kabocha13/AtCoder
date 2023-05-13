# https://atcoder.jp/contests/abc301/tasks/abc301_c
# a,t,c,o,d,e,r,@の8つの要素のリストとその他用の別のリストをs用とt用の二つ用意する。
# それぞれ対応する文字の個数を入れてどれにも当てはまらないものはその他用リストにそのまま入れる。
# まずその他用リストをソートしたものを比較して違う場合は問答無用で死刑
# あってた場合はaから順番に個数が等しければ次、個数違ければ@の数を-して行く。
# 最終的に@の数が-にならないかつそれぞれの@の数が等しくなればYes

s = input()
t = input()

# 2つの列に含まれる各文字の出現回数を数える
# a t c o d e r @ その他
s_count = [0] * 8
t_count = [0] * 8
selse = []
telse = []


for i in s:
  if i=="a":
    s_count[0] += 1
  elif i=="t":
    s_count[1] += 1
  elif i=="c":
    s_count[2] += 1
  elif i=="o":
    s_count[3] += 1
  elif i=="d":
    s_count[4] += 1
  elif i=="e":
    s_count[5] += 1
  elif i=="r":
    s_count[6] += 1
  elif i=="@":
    s_count[7] += 1
  else:
    selse.append(i)
    
for i in t:
  if i=="a":
    t_count[0] += 1
  elif i=="t":
    t_count[1] += 1
  elif i=="c":
    t_count[2] += 1
  elif i=="o":
    t_count[3] += 1
  elif i=="d":
    t_count[4] += 1
  elif i=="e":
    t_count[5] += 1
  elif i=="r":
    t_count[6] += 1
  elif i=="@":
    t_count[7] += 1
  else:
    telse.append(i)
    

  
if sorted(selse)==sorted(telse):
  for i in range (7):
    if t_count[i]==s_count[i]:
      continue
    elif t_count[i]<s_count[i]:
      t_count[7] -= s_count[i]-t_count[i]
    else:
      s_count[7] -= t_count[i]-s_count[i]
  if s_count[7]==t_count[7] and s_count[7]>=0 and t_count[7]>=0:
    print("Yes")
  else:
    print("No")
else:
  print("No")
