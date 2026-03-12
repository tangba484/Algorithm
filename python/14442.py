from collections import deque
n,m,k = map(int,input().split())


graph = []
for _ in range(n):
    graph.append(list(map(int,list((input())))))

visited = [[[0]*(k+1) for _ in range(m)]for _ in range(n)]

visited[0][0][0] = 1
q = deque([])
q.append([0,0,0,1])
def bfs():
    while q:
        cx,cy,breaking,d = q.popleft()
        if (cx,cy) == (n-1,m-1):
            return  d

        for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
            nx,ny  = cx+dx,cy+dy
            if 0<=nx<n and 0<=ny<m:

                if graph[nx][ny] == 0 and not visited[nx][ny][breaking]:
                    visited[nx][ny][breaking] = 1
                    q.append([nx,ny,breaking,d+1])
                if graph[nx][ny] == 1 and breaking < k and not visited[nx][ny][breaking+1]:
                    visited[nx][ny][breaking + 1] = 1
                    q.append([nx,ny,breaking+1,d+1])
    return -1

print(bfs())
