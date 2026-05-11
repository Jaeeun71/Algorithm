from collections import deque

def solution(maps):
    
    n = len(maps) # 행
    m = len(maps[0]) # 열
    dx = [-1,1,0,0] # 상하좌우
    dy = [0,0,-1,1] # 상하좌우
    
    q = deque()
    q.append((0,0))
    
    while q : # queue가 빌 때까지 반복
        x, y = q.popleft()
        
        for i in range(4) : # 현재 위치에서 상하좌우 확인
            nx = x + dx[i] 
            ny = y + dy[i]
            
            if nx < 0 or ny < 0 or nx >= n or ny >= m : continue
            if maps[nx][ny] == 0 : continue
            if maps[nx][ny] == 1 :
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
                
    return maps[n-1][m-1] if maps[n-1][m-1] > 1 else -1
            
        
