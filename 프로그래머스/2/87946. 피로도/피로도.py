def solution(k, dungeons):
    answer = 0
    visited = len(dungeons) * [False]
    
    def DFS(count, current) :
        nonlocal answer
        answer = max(count, answer)
        
        for i in range(len(dungeons)) :
            min, down = dungeons[i]
            
            if not visited[i] and current >= min :
                visited[i] = True
            
                DFS(count+1, current-down)
                visited[i] = False
            
    DFS(0, k)
            
    return answer