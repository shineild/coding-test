def solution(s):
    answer = ''
    cnt = 0
    for i in range(len(s)):
        s = list(s)
        
        if s[i] == ' ':
            answer += s[i]
            cnt = 0
        elif s[i] >'Z' and s[i] <'a':
            answer += s[i]
            cnt += 1
        elif s[i] <'A' or s[i] > 'z':
            answer += s[i]
            cnt += 1
        
        elif cnt % 2 == 0:
            if s[i] > 'Z':
                answer += chr(ord(s[i]) - 32)
            else:
                answer += s[i]
            cnt += 1
        else:
            if s[i] < 'a':
                answer += chr(ord(s[i])+32)
            else:
                answer += s[i]
            cnt += 1
    
    return answer
