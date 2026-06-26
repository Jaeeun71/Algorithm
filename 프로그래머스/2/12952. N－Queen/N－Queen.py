def solution(n) :
    answer = 0
    board = [0]*n
    
    def is_safe(y):
        for i in range(y) :
            if board[y] == board[i] or abs(y-i) == abs(board[y]-board[i]) :
                return False
        return True
    
    def DFS(y) :
        nonlocal answer
        
        if y == n :
            answer += 1
            return
        
        for x in range(n) :
            board[y] = x
            
            if is_safe(y) :
                DFS(y+1)
                
                
    DFS(0)
    
    return answer