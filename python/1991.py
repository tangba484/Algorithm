n = int(input())

D = dict()

for _ in range(n):
    a,b,c = input().split()
    D[a] = []
    D[a].append(b)
    D[a].append(c)

def preOrder(D,s):
    print(s,end="")
    for i in D[s]:
        if i != '.':
            preOrder(D,i)

def postOrder(D,s):
    for i in D[s]:
        if i != '.':
            postOrder(D,i)
    print(s,end="")

def inOrder(D,s):
    if D[s][0] != '.':
        inOrder(D,D[s][0])
    print(s,end="")
    if D[s][1] != '.':
        inOrder(D,D[s][1])

preOrder(D,'A')
print("\n",end="")
inOrder(D,'A')
print("\n",end="")
postOrder(D,'A')