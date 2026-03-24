from collections import deque

n, m = map(int, input().split())
index = list(map(int, input().split()))

arr = deque(range(1, n+1))
count = 0

for i in index :
    while 1 :
        if arr[0] == i :
            arr.popleft()
            break

        else :
            if arr.index(i) <= len(arr)//2 :
                arr.rotate(-1)
                count += 1
            else : 
                arr.rotate(1)
                count += 1

print(count)