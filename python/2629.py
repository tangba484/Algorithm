n = int(input())

w = [0]+list(map(int,input().split()))

m = int(input())
targets = list(map(int, input().split()))

W = sum(w)

dp = [[0 for _ in range(W+1)] for _ in range(n + 1)]
for i in range(n+1):
    dp[i][0] = 1
for i in range(1,n+1):

    weight = w[i]

    for j in range(W + 1):
        if dp[i-1][j]:
            dp[i][j] = 1
            if j + weight < W+1:
                dp[i][j + weight] = 1
            dp[i][abs(j-weight)] = 1



for i in range(m):
    target = targets[i]
    if target > W:
        print("N",end = " ")
        continue
    if dp[-1][target] == 1:
        print("Y",end=" ")
    else:
        print("N",end=" ")
