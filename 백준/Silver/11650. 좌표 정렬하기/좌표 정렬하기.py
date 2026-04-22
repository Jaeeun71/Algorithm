import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n) :
    [a, b] = map(int, input().split())
    data.append([a, b])

data.sort()

for i in range(n):
    print(data[i][0], data[i][1])