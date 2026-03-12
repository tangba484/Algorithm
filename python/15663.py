n,m = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

ans = set()
def back(lst,use_idx,L):
    if L == m:
        ans.add(tuple(lst))
        return
    
    for i in range(n):
        if i not in use_idx:
            back(lst + [arr[i]],use_idx + [i],L+1)

back([],[],0)

ans = sorted(list(ans))
for i in ans:
    print(*i)