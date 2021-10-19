def solution(s, n):
    answer = ''
    for i in range(len(s)):
        tmp = chr(ord(s[i])+n)
        if s[i] == ' ':
            answer += ' '
        elif tmp > 'Z' and s[i] < 'a':
            tmp = chr(ord(tmp) - 26)
            answer += tmp
        elif tmp > 'z':
            tmp = chr(ord(tmp) - 26)
            answer += tmp
        else:
            answer += tmp
    return answer
