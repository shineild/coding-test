import heapq
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
answer = 0

for i in range(m):
    a,b,c = map(int,sys.stdin.readline().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

queue = []
heapq.heappush(queue, (0,1))

def Prim():
    global answer
    while queue:
        wei, now = heapq.heappop(queue)
        if visited[now] == False:
            visited[now] = True
            answer += wei
            for next_wei, next_node in graph[now]:
                heapq.heappush(queue, (next_wei, next_node))
    return answer

print(Prim())
