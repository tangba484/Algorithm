n,t = map(int,input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int,input().split())))

dp = [0]*(t+1)

for i in range(n):
    k,s = arr[i]
    for j in range(t,k-1,-1):
        dp[j] = max(dp[j],dp[j - k] + s)
print(dp[-1])