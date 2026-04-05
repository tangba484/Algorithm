import sys

input = sys.stdin.readline

N, M = map(int, input().split())
rows = [input().strip() for _ in range(N)]
K = int(input())

count_map = {}

for row in rows:
    count_map[row] = count_map.get(row, 0) + 1

answer = 0

for row, cnt in count_map.items():
    zero_count = row.count('0')

    if zero_count <= K and (K - zero_count) % 2 == 0:
        answer = max(answer, cnt)

print(answer)