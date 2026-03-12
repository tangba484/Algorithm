n,k = map(int,input().split())
arr = set([])

for _ in range(n):
    arr.add(int(input()))

arr = sorted(list(arr))

dp = [float('inf')]*(k+1)
dp[0] = 0
n = len(arr)

for i in range(n):
    coin = arr[i]
    for j in range(coin,k+1):
        dp[j] = min(dp[j],dp[j - coin] + 1)

if dp[-1] == float('inf'):
    print(-1)
else:
    print(dp[-1])