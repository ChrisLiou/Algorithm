#DP_Optimize
cost=[10,15,20]

def minCostClimbingStairs4(cost):
    minCost=[]
    minCost.append(cost[0])
    minCost.append(cost[1])

    for i in range(2,len(cost)):
        minCost.append(cost[i]+min(minCost[0],minCost[1]))
        minCost.pop(0)

    return min(minCost[0],minCost[1])
    
print(minCostClimbingStairs4(cost))

