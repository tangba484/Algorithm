
N = int(input())
M = int(input())
D = dict()

for num in range(1,N+1):
    D[num] = []
    l = list(map(int,input().split()))
    for x in range(len(l)):
        if l[x] == 1:
            D[num].append(x+1)
print(D)
target = list(map(int,input().split()))
a = set()
visited = [0]*(N+1)
def dfs(num):
    a.add(num)

    for i in D[num]:
        if not visited[i]:
            visited[i] = 1
            dfs(i)
dfs(target[0])
flag = 0
for i in list(set(target)):
    if i not in a:
        print("NO")
        flag = 1
        break

if flag == 0:
    print("YES")