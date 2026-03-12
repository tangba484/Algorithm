n, d, k, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]

max_cnt = 0

for i in range(n):
    s = set()
    
    for j in range(k):
        s.add(arr[(i + j) % n]) 
    if c not in s:
        s.add(c)
    
    max_cnt = max(max_cnt, len(s))

print(max_cnt)