#DP
cost=[10,15,20]

def minCostClimbingStairs2(cost):
    minCost=[]
    minCost.append(cost[0])
    minCost.append(cost[1])
    cost.append(0)
    for i in range(2,len(cost)):
        minCost.append(0)

    for i in range(2,len(cost)):
        minCost[i]=cost[i]+min(minCost[i-1],minCost[i-2])

    return minCost[len(minCost)-1]
    
print(minCostClimbingStairs2(cost))

