def solution(brown, yellow):
    answer = []
    area = brown + yellow
    
    for h in range(3, brown//2 +1) :
        if area % h == 0 :
            w = area // h
            
            if yellow == (w-2)*(h-2) :
                return [w,h]