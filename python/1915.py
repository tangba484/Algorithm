n,m = map(int,input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int,list(input()))))
ans = 0
dp = [[0 for _ in range(m)]for _ in range(n)]
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            dp[i][j] = 1
            ans = 1

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and 0<=i-1<n and 0<=j-1<m:
            dp[i][j] = min(dp[i-1][j] , dp[i-1][j-1], dp[i][j-1]) + 1
            ans = max(dp[i][j],ans)

print(ans**2)
