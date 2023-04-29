# 愚直に一回ずつ回転させたやつを比較する全探索！
# 横回転が少し難しいかも？

H, W = map(int, input().split())
A = [list(input()) for _ in range(H)]
B = [list(input()) for _ in range(H)]

# マップAを(0,0)から右方向に1列ずつずらしながら、それぞれマップBと比較する
for t in range(W):
    for s in range(H):
        matched = True
        for i in range(H):
            for j in range(W):
                if A[i][(j+t)%W] != B[(i+s)%H][j]:
                    matched = False
                    break
            if not matched:
                break
        if matched:
            print("Yes")
            exit()

print("No")
