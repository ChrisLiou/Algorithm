N=5
k=1
times=[[1,4,2],[1,2,9],[4,2,-4],[2,5,-3],[4,5,6],[5,3,7],[3,2,3],[3,1,5]]

def networkDelayTime(N,k,times):
    d=[0]
    for i in range(n):
        if i==k-1:
            d.append(0)
        else:
            d.append(float('inf'))
    for i in range(n-1):
        count=0
                
        for j in range(len(times)):
            source=times[j][0]
            target=times[j][1]
            weight=times[j][2]
            if d[source]!=float('inf') and (d[source]+weight)<d[target]:
                d[target]=d[source]+weight
                count+=1
        if count==0:
            break
    if max(d)==float('inf'):
        return -1
    else:
        return max(d)

print(networkDelayTime(N,k,times))