import sys
input = sys.stdin.readline

n = int(input())
data = []

for _ in range(n) :
    [a, b] = map(int, input().split())
    data.append([b, a])

data.sort()

for i in range(n) :
    print(data[i][1], data[i][0])