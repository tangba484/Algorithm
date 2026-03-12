import sys
input = sys.stdin.readline
a = []
while True:
    try:
        x = input()
        a.append(int(x))
    except :
        break

print(a)
for i in a:
    