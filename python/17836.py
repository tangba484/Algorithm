from collections import deque
import heapq
N,M,T = map(int,input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int,input().split())))
visited = [[0 for _ in range(M)]for _ in range(N)]

q = deque([])
q.append([0,0,0,0])
visited[0][0] = 1
ans  = []
while q:
    cx,cy,time,gram = q.popleft()
    if time > T:
        continue
    if cx == N-1 and cy == M-1:
        ans.append(time)
        break
    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
        nx ,ny = cx+dx , cy+dy
        if gram == 0 and 0<=nx<N and 0<=ny<M and not visited[nx][ny] and graph[nx][ny]!=1:
            visited[nx][ny] = 1
            if graph[nx][ny] == 2:
                ans.append(N-1-nx + M-1-ny + time + 1)
            q.append([nx,ny,time+1,gram])
if ans:
    if min(ans) > T:
        print("Fail")
    else:
        print(min(ans))
else:
    print("Fail")

