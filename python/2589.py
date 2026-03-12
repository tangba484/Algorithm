from collections import deque
Row,Col = map(int,input().split())

graph = []
for _ in range(Row):
    graph.append(list(input()))


v = [[0 for _ in range(Col)] for _ in range(Row)]

def dfs(x,y):
    ans = 0
    stack = deque([[x,y,0]])
    visited = []
    for i in v:
        visited.append(i[:])
    visited[x][y] = 1
    while stack:
        cx,cy,time = stack.popleft()
        ans = max(ans,time)

        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx,ny = cx+dx,cy+dy
            if 0<=nx<Row and 0<=ny<Col and graph[nx][ny] =="L" and not visited[nx][ny]:
                stack.append([nx,ny,time + 1])
                visited[nx][ny] = 1

    return ans

res = []
for x in range(Row):
    for y in range(Col):
        if graph[x][y] == "L":
            res.append(dfs(x,y))

if res:
    print(max(res))
else:
    print(0)