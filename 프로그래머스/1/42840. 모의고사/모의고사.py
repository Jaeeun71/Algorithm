def solution(answers):
    answer_1 = [1,2,3,4,5]
    answer_2 = [2,1,2,3,2,4,2,5]
    answer_3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer = [0,0,0]
    result = []
    
    for i in range(len(answers)) :
        
        if answers[i] == answer_1[i%len(answer_1)] :
            answer[0] += 1
        if answers[i] == answer_2[i%len(answer_2)] :
            answer[1] += 1
        if answers[i] == answer_3[i%len(answer_3)] :
            answer[2] += 1
            
    for i in range(len(answer)) :
        if answer[i] == max(answer) :
            result.append(i+1)

    return result