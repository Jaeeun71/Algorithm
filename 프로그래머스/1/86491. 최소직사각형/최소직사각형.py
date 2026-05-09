def solution(sizes):
    answer = 0
    
    # 가로<세로인 경우 자리 바꾸기
    for i in range(len(sizes)) :
        if sizes[i][0]<sizes[i][1] :
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]
            

    # 최댓값 찾기
    max_w = sizes[0][0]
    max_h = sizes[0][1]
    
    for i in range(len(sizes)) :
        if sizes[i][0] > max_w :
            max_w = sizes[i][0]
            
    for i in range(len(sizes)) :
        if sizes[i][1] > max_h :
            max_h = sizes[i][1]
            
    answer = max_w*max_h
    
    return answer