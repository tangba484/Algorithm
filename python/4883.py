t = 0.1
while t:
    t = int(t) + 1
    n = int(input())
    if n == 0:
        break
    graph = []
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    dp = [[0 for _ in range(3)] for _ in range(n)]
    dp[0] = graph[0]
    dp[0][-1] =  graph[0][1] + graph[0][2]
    dp[1][0] = graph[0][1] + graph[1][0]
    dp[1][1] = min(dp[1][0]+graph[1][1],dp[0][1] + graph[1][1],dp[0][2] + graph[1][1])
    dp[1][2] = min(dp[1][1]+graph[1][2],dp[0][1] + graph[1][2],dp[0][2] + graph[1][2])
    for i in range(2,n):
        for j in range(3):
            if j == 0:
                dp[i][j] = min(graph[i][j] + dp[i-1][j], graph[i][j] + dp[i-1][j+1])
            elif j == 1:
                dp[i][j] = min(graph[i][j] + dp[i-1][j], graph[i][j] + dp[i-1][j+1],graph[i][j] + dp[i-1][j-1],graph[i][j] + dp[i][j-1])
            elif j == 2:
                dp[i][j] = min(graph[i][j] + dp[i-1][j],graph[i][j] + dp[i-1][j-1],graph[i][j] + dp[i][j-1])
    print(str(t)+".",dp[-1][1])
    