import sys
import heapq
t = int(sys.stdin.readline())
for i in range(t):
    k = int(sys.stdin.readline())
    visit = [False] * 1000001
    max_que = []
    min_que = []
    for i in range(k):
        com = list(map(str, sys.stdin.readline().split()))

        if com[0] == 'I':
            heapq.heappush(min_que, (int(com[1]), i))
            heapq.heappush(max_que, (int(com[1]) * -1, i))
            visit[i] = True
        elif com[1] == '1':
            while max_que and not visit[max_que[0][1]]:
                heapq.heappop(max_que)
            if max_que:
                visit[max_que[0][1]] = False
                heapq.heappop(max_que)
        else:
            while min_que and not visit[min_que[0][1]]:
                heapq.heappop(min_que)
            if max_que:
                visit[min_que[0][1]] = False
                heapq.heappop(min_que)
        while max_que and not visit[max_que[0][1]]:
            heapq.heappop(max_que)
        while min_que and not visit[min_que[0][1]]:
            heapq.heappop(min_que)
            
    if max_que and min_que:
        print(max_que[0][0] * -1, min_que[0][0])
    else:
        print("EMPTY")
