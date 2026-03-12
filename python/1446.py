N,D = map(int,input().split())

dp = [float('inf')]*(D+1)
dp[0] = 0
arr = []
for _ in range(N):
    arr.append(list(map(int,input().split())))

for now in range(1,D+1):

    i = 0
    flag = 0
    while i < N:
        start,end,cost = arr[i]
        if now == end:
            flag = 1
            dp[now] = min(dp[start] + cost , dp[now-1] + 1,dp[now])
        i += 1
    if flag == 0:
        dp[now] = dp[now-1] + 1
print(dp[-1])
