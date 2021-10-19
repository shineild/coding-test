def solution(record):
    answer = []
    di = {}
    for a in range(len(record)):
        record[a] = record[a].split()   
    for b in range(len(record)):
        if(record[b][0] != "Leave"):
            if(record[b][0] == "Enter" or "Change"):               
                di[record[b][1]] = record[b][2]
    for c in range(len(record)):
        if record[c][0] == "Enter":        
            answer.append(di[record[c][1]] + "님이 들어왔습니다.")
        elif record[c][0] == "Leave":
            answer.append(di[record[c][1]] + "님이 나갔습니다.")
    return answer
