n = int(input())

for _ in range(n) :
    pw = input()
    list_left = []
    list_right = []

    for char in pw :
        if char == '>' :
            if list_right :
                list_left.append(list_right.pop())
        elif char == '<' :
            if list_left :
                list_right.append(list_left.pop())
        elif char == '-' :
            if list_left :
                list_left.pop()
        else : list_left.append(char)
    
    print(''.join(list_left) + ''.join(reversed(list_right)))
