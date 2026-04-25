import sys
input = sys.stdin.readline

data = list(map(int, list(input().strip())))
data.sort(reverse = True)

print("".join(map(str,data)))