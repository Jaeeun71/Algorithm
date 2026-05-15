def solution(numbers, target):
    results = [0]
    
    for i in numbers :
        tmp = []
        for parent in results :
            tmp.append(parent + i)
            tmp.append(parent - i)
        results = tmp
    
    
    return results.count(target)