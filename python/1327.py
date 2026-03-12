from collections import deque

n,k = map(int,input().split())
start = tuple(map(int,input().split()))
target = tuple(sorted(start))
visited = set()
q = deque([])
q.append([start,0])
while q:
    arr,depth = q.popleft()

    if arr == target:
        print(depth)
        break
    arr = list(arr)
    for i in range(n-k+1):
        new_arr = arr[:]

        new_arr[i:i+k] = reversed(new_arr[i:i+k])
        if tuple(new_arr) not in visited:
            visited.add(tuple(new_arr))
            q.append([tuple(new_arr),depth+1])

if arr!= target:
    print(-1)