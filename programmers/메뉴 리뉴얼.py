from itertools import chain, combinations

def get_all_subset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def solution(orders, course):
    answer = []
    dic = {}
    
    orders = sorted(orders)
    for i in range(len(orders)):
        orders[i] = sorted(list(orders[i]))
    for i in range(len(orders)): 
        subset_list = get_all_subset(list(range(0, len(orders[i]))))
        for j in subset_list:
            if len(j) in course:
                string = ''
                for k in j:
                    string += orders[i][k]
                if string in dic:
                    dic[string] += 1
                else:
                    dic[string] = 1
    tmp = [0] * 10
    tmp_answer = [['']] * 10
    for key, val in dic.items():
        if val >= 2:
            l = len(key)-1
            if tmp[l] < val:
                tmp[l] = val
                tmp_answer[l] = [key]
            elif tmp[l] == val:
                tmp_answer[l].append(key)
    for c in tmp_answer:
        if c == ['']:
            continue
        answer += c
    answer.sort()
    return answer
