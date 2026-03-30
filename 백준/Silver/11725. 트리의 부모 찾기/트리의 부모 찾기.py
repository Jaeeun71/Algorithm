import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
array = [[] for _ in range (n+1)] # 연결 관계 저장
parentArray = [0] * (n+1) # 부모 노드 저장

for _ in range(n-1) :
    i, k = map(int, input().split())
    array[i].append(k)
    array[k].append(i)

queue = deque([1]) 
parentArray[1] = 1 

while queue:
    nowNode = queue.popleft()
    for connectedNode in array[nowNode]:
        if parentArray[connectedNode] == 0: 
            parentArray[connectedNode] = nowNode 
            queue.append(connectedNode)


for i in range(2, n+1):
    print(parentArray[i])

