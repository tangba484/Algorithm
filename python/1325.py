import sys
input = sys.stdin.readline
n,m = map(int,input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(com):
    visited = [0]*(n+1)
    visited[com] = 1
    stack = [com]
    ans = 1
    while stack:
        cur_com = stack.pop()
        for i in graph[cur_com]:
            if not visited[i]:
                visited[i] = 1
                stack.append(i)
                ans += 1
    return ans
res = []
for i in range(1,n+1):
    res.append([i,dfs(i)])
res.sort(key = lambda x: -x[1])

target = res[0][1]
answer = []
for i in res:
    if i[1] == target:
        answer.append(i[0])
print(*sorted(answer))