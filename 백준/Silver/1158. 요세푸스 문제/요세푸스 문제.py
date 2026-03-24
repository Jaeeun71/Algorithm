n, k = map(int, input().split())
arr = list(range(1, n+1))

answer=[]
num = 0

for i in range(n) :
    num = (k-1 + num) % len(arr)
    answer.append(str(arr.pop(num)))

print("<" + ", ".join(answer) + ">" )