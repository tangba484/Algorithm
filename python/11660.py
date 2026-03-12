n,m = map(int,input().split())

graph=[]

for _ in range(n):
    graph.append(list(map(int,input().split())))
targets = []
for _ in range(m):
    targets.append(list(map(int,input().split())))

dp = [[0 for _ in range(n)]for _ in range(n)]

dp[0][0] = graph[0][0]

for i in range(1,n):
    dp[0][i] = dp[0][i-1] + graph[0][i]
    dp[i][0] = dp[i-1][0] + graph[i][0]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i][j]

dp.insert(0,[0]*(n))
for i in range(len(dp)):
    dp[i] = [0]+dp[i]

for x1,y1,x2,y2 in targets:
    print( dp[x2][y2] - dp[x1-1 ][y2] - dp[x2][y1-1] + dp[x1-1][y1-1])