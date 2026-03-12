n,m = map(int,input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int,input().split())))

def check(graph):
    stack = []
    visited = [[0 for _ in range(m)] for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                stack = [[i,j]]
                ans += 1
                visited[i][j] = ans
                while stack:
                    cx,cy = stack.pop()
                    for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                        nx,ny = cx+dx , cy+dy
                        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] != 0:
                            visited[nx][ny] = ans
                            stack.append([nx,ny])
    return ans


def bfs(graph):
    board = [[0 for _ in range(m)]for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0:
                cnt = 0
                for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx,ny = i+dx,j+dy
                    if 0<=nx<n and 0<=ny<m and graph[nx][ny] == 0:
                        cnt += 1
                board[i][j] = cnt
    for i in range(n):
        for j in range(m):
            graph[i][j] = graph[i][j] - board[i][j]
            if graph[i][j] < 0: graph[i][j] = 0
    return graph


time = 0.1

while time :
    time = int(time) + 1
    graph = bfs(graph)
    res = check(graph)
    if res >= 2:
        print(time)
        break
    S = 0
    for i in graph:
        S = S + sum(i)
    if S == 0:
        print(0)
        break
# 3 3
# 1 0 2
# 0 0 0
# 1 0 3