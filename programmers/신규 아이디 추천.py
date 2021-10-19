def solution(new_id):
    answer = ''
    
    # 1
    new_id = new_id.lower()
    
    # 2
    ban = ['~','!','@','#','$','%',"'",'"','^','&','*','(',')','=','+','[','{',']','}',':','?',',','<','>','/']
    new_id = list(new_id)
    check = True
    while(True):
        for c in new_id:
            if c in ban:
                new_id.remove(c)
                check = False
                break
        if check == True:
            break
        else:
            check = True
    
    # 3
    check = True
    while(True):
        for i in range(len(new_id)-1):
            if new_id[i] == '.':
                if new_id[i+1] == '.':
                    del new_id[i]
                    check = False
                    break
        if check == True:
            break
        else:
            check = True
    
    # 4 & 5
    if len(new_id) != 0:
        if new_id[0] == '.':
            del new_id[0]
    else:
        new_id = ['a']
    if len(new_id) != 0:
        if new_id[-1] == '.':
            del new_id[-1]
    else:
        new_id = ['a']
    
    # 6
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[14] == '.':
            del new_id[14]
    # 7
    if len(new_id) <= 2:
        while(len(new_id) != 3):
            new_id.append(new_id[-1])
    answer = ''.join(new_id)
    return answer
