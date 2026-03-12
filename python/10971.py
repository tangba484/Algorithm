n = int(input())
cost = [list(map(int,input().split())) for _ in range(n)]

visited = [0]*n
ans = float('inf')

def back(idx, depth, total):
    global ans
    
    if depth == n:
        if cost[idx][0] != 0:
            ans = min(ans, total + cost[idx][0])
        return
    
    for next_idx in range(n):
        if not visited[next_idx] and cost[idx][next_idx] != 0:
            visited[next_idx] = 1
            back(next_idx, depth+1, total + cost[idx][next_idx])
            visited[next_idx] = 0

visited[0] = 1
back(0,1,0)

print(ans)