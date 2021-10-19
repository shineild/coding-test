def solution(n, lost, reserve):
    answer = 0
    answer = n - len(lost) #빌리지 않고 입을 수 있는 학생 수
    for i in lost: #여벌의 체육복이 있는 도난 당한 학생 먼저 빼기
        for j in reserve:
            if i==j:
                reserve.remove(j)
                lost.remove(i)
                answer+=1
                break;
    for i in lost:
        for j in reserve:
            if j==i-1 or j==i+1:
                reserve.remove(j)
                answer+=1
                #lost.remove(i)
                break;  
    
    return  answer
