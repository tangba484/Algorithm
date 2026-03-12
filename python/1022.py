r1, c1, r2, c2 = map(int,input().split())

answer = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]

N = 0
cnt = 0
cx,cy = 0,0
n = 0
dv = -1 # 0 오른쪽,1 왼쪽 , 2위,3아래
while cnt < (c2-c1+1)*(r2-r1+1):
    n += 1
    if r1<=cx<=r2 and c1<=cy<=c2:
        answer[-(r1)+ cx][-(c1) + cy] = n
        cnt += 1
        N = max(N,n)
    if cx>=0 and (cx==cy):
        cy += 1
        dv = 2
    elif cx < 0 and (-cx == cy):
        cy -= 1
        dv = 1
    elif (cx == cy) and cx < 0:
        cx += 1
        dv = 3
    elif cx >0 and cx == -cy:
        cy += 1
        dv = 0
    else:
        if dv == 2:
            cx -= 1
        elif dv ==1:
            cy -= 1
        elif dv == 3:
            cx += 1
        elif dv == 0:
            cy += 1
lenOfNum = len(str(N))
for i in range(len(answer)):
    for j in range(len(answer[0])):
        print(" "*(lenOfNum - len(str(answer[i][j])))    +   str(answer[i][j]),end=" ")
    print()
