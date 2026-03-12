n= int(input())
arr = list(map(int,input().split()))
stack = [arr[n-1]]
ans =dict()
for i in range(n-2,-1,-1):
    while stack:
        if stack[-1] < arr[i]:
            a = stack.pop()
            ans[a] = i+1
            continue
        else:
            break
    stack.append(arr[i])

while stack:
    a = stack.pop()
    ans[a] = 0

for i in arr:
    print(ans[i],end=" ")