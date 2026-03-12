N,M = map(int,input().split())

m = list(map(int,input().split()))
c = list(map(int,input().split()))

maxCost = sum(c)

dp = [0]*(maxCost + 1)



for j in range(N):
    for i in range(maxCost, c[j]-1, -1):
        dp[i] = max(dp[i], dp[i - c[j]] + m[j])

for i in range(maxCost + 1):
    if dp[i] >= M:
        print(i)
        break