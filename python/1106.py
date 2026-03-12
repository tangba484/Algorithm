c,n = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp = [float('inf')]*(2*c+101)
dp[0] = 0
for i in range(n):
    cost,v = arr[i]
    for j in range(v,2*c+101):
        dp[j] = min(dp[j],dp[j - v] + cost)

print(min(dp[c:]))