import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l,n = map(int,input().split())
    ants = []
    fast=[]
    late = []
    for _ in range(n):
        ants.append(int(input()))

    for i in range(n):
        fast.append(min(l-ants[i],ants[i]))
        late.append(max(ants[i],l-ants[i]))
    print(max(fast),max(late))
