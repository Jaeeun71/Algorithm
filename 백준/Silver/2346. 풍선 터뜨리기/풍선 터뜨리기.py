import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
deq = deque(enumerate(map(int, input().split())))
answer = []

while deq :
    index, paper = deq.popleft()
    answer.append(index+1)

    if paper > 0 :
        deq.rotate(-(paper-1))
    else : deq.rotate(-paper)

print(' '.join(map(str, answer)))