n = input()

start = n
cnt = 0
while 1:
    cnt += 1
    if len(n) == 1:
        n = '0'+n
    s = str(int(n[0]) + int(n[-1]))

    next_num = int(n[-1] + s[-1])
    if next_num == int(start):
        print(cnt)
        break

    n = str(next_num)