n = int(input())

arr = []
for _ in range(6):
    arr.append(list(map(int,input().split())))


maxW,maxH = 0,0

for i in range(6):
    v,l = arr[i]
    if v in (1,2):
        maxW = max(maxW,l)
    else:
        maxH = max(maxH,l)

minS = []

for i in range(6):

    if arr[(i-1)%6][0] == arr[(i+1)%6][0]:
        minS.append(arr[i][1])


print((maxW*maxH - minS[0]*minS[1])*n)