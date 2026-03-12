n = int(input())
string = input()
D = {}

for i in range(n):
    val = int(input())
    D[chr(65 + i)] = val


stack = []

S = list(string[:])
for i in range(len(S)):
    if S[i] not in ("*+-/"):
        S[i] = D[S[i]]

i = 0
while i < len(S):
    if str(S[i]) not in "*+-/":
        stack.append(S[i])
        i += 1
    else:
        if S[i] == "*":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append( n2 * n1)
        elif S[i] == "+":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append( n2 + n1)
        elif S[i] =="-":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append( n2 - n1)
        elif S[i] == "/":
            n1 = stack.pop()
            n2 = stack.pop()
            stack.append( n2 / n1)
        i += 1
print(f"{stack[0]:.2f}")