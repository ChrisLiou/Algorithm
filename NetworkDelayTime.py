import heapq

times=[[1,2,9],[1,4,2],[2,5,1],[4,2,4],[4,5,6],[3,2,3],[5,3,7],[3,1,5]]
k=1
n=5
d=[0]
graph=[{}]
for i in range(n):
    if i+1==k:
        d.append(0)
    else:
        d.append(float('inf'))
    graph.append({})

for i in range(len(times)):
    source=times[i][0]
    target=times[i][1]
    weight=times[i][2]
    graph[source][target]=weight

pq=[]
heapq.heapify(pq)
heapq.heappush(pq,k)
seen=[]
while not pq.empty():
    currentNode=heapq.heappop(pq,0)
    seen.append(currentNode)
    for key in graph[currentNode]:
        if key not in seen:
            heapq.heappush(pq,key)
            weight=graph[currentNode].get(key)
            d[key]=min(weight+d[currentNode],d[key])

print(d)
        

