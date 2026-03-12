n = int(input())

arr = list(map(int,input().split()))
stack = []
target = 1

for i in range(n):
    if arr[i] == target:
        target += 1
        while stack:
            if stack[-1] == target:
                stack.pop()
                target += 1
            else:
                break
    else:
        stack.append(arr[i])

if stack:
    print("Sad")
else:
    print("Nice")