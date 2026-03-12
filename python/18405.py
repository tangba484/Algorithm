from collections import deque
n,k = map(int,input().split())

graph = [[-1 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    graph[i][1:] = list(map(int,input().split()))

S,X,Y = map(int,input().split())

q = deque([])
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] != 0 and graph[i][j] != -1:
            q.append([graph[i][j],i,j,0])
q = deque(sorted(list(q)))

while q:
    virus,x,y,time = q.popleft()
    if time >= S:
        continue
    
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx,ny = x+dx,y+dy
        if 0<=nx<=n and 0<=ny<=n and graph[nx][ny] == 0:
            graph[nx][ny] = virus
            q.append([virus,nx,ny,time + 1])

print(graph[X][Y])