from collections import deque

n= int(input())
arr = deque(list(input()))

graph = []
for _ in range(n):
    graph.append(list(input()))

flashMap = [[0 for _ in range(n)]for _ in range(n)]
zombieMap = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'Z':
            zombieMap.append([i,j,3])

cx,cy,state = 0,0,3 

# 아래 오른 위 왼   
#   3  2   1  0
flag = 0
while arr:
    x = arr.popleft()
    # if graph[cx][cy] == 'Z' and not flashMap[cx][cy]:
    #     print("Aaaaaah!")
    #     break

    for zx,zy,zState in zombieMap:
        if (zx,zy) == (cx,cy) and not flashMap[zx][zy]:
            flag = 1
            break
    if x == "F":
        if state == 3: cx += 1
        elif state == 2: cy += 1
        elif state == 0: cy -= 1
        elif state == 1: cx -= 1
        if cx >=n: cx-=1
        elif cy>=n: cy-=1
        elif cx<0: cx+=1
        elif cy<0: cy+=1
    elif x == 'L':
        state = (state - 1)%4
    elif x == 'R':
        state = (state + 1)%4
    
    if graph[cx][cy] == "S":
        for dx,dy in [(0,0),(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
            nx,ny = cx+dx,cy+dy
            if 0<=nx<n and 0<=ny<n: flashMap[nx][ny] = 1
    

    for zx,zy,zState in zombieMap:
        if (zx,zy) == (cx,cy) and not flashMap[zx][zy]:
            flag = 1
            break
    for i in range(len(zombieMap)):
        zx, zy, zState = zombieMap[i]
        if zState == 3:
            zx += 1
        elif zState == 1:
            zx -= 1
        if zx >= n:
            zx -= 1
            zState = 1
        elif zx <0:
            zx += 1
            zState = 3
        zombieMap[i] = [zx, zy, zState]
    
    if flag == 1:
        print("Aaaaaah!")
        break
if flag == 0:
    print("Phew...")