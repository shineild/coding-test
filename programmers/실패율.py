def solution(N, stages):
    answer = []
    dic = {}
    cnt = len(stages)
    l = cnt
    for i in range(1, N+1):
        fail = stages.count(i)
        if (cnt == 0):
            dic[i] = 0
        else:
            dic[i] = fail/cnt
            cnt -= fail
    new_dic = sorted(dic.items(), reverse=True, key=lambda item: item[1])

    for key, value in new_dic:
        answer.append(key)
    return answer
