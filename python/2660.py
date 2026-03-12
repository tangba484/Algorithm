from collections import deque
n = int(input())

graph = [[]for _ in range(n+1)]

while 1:
    a,b = map(int,input().split())
    if (a,b) == (-1,-1):
        break
    graph[a].append(b)
    graph[b].append(a)


def bfs(person):
    visited = [0]*(n+1)
    visited[0] = 99
    visited[person] = 1
    q = deque([[person,0]])
    
    while q:
        if visited == [99]+[1]*(n):
            return [person,q[-1][-1]]
        p,depth = q.popleft()
        
        for i in graph[p]:
            if not visited[i]:
                visited[i] = 1
                q.append([i,depth+1])
ans = []

top = 10000
for i in range(1,n+1):
    result = bfs(i)
    ans.append(result)
    top = min(result[-1],top)
ans.sort()
cnt = 0
answer = []
for i in ans:
    if i[1] == top:
        cnt += 1
        answer.append(i[0])

print(top, cnt)
print(*answer)