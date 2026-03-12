n = int(input())

arr = list(map(int,input().split()))

dp = [1]*(n)

for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i],dp[j] + 1)
print(max(dp))

target = max(dp)
ans = []
for i in range(n-1,-1,-1):
    if dp[i] == target:
       ans.append(arr[i])
       target -= 1
print(*sorted(ans) )
