n = int(input())

for _ in range(n):
    a = input()
    stack = []
    flag = 0
    for i in range(len(a)):
        if a[i] == "(":
            stack.append(a[i])
        else:
            if stack:
                stack.pop()
            else:
                flag = 1
                break
    if flag == 1:
        print("NO")
    elif stack:
        print("NO")
    else:
        print("YES")