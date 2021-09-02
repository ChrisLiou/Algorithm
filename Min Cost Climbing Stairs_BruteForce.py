
#Brute Force
cost=[10,15,20]

def minCostClimbingStairs1(cost):
    n=len(cost)
    cost.append(0)

    return minCost1(n,cost)

def minCost1(n,cost):
    if n<0:
        return 0
    elif n==0:
        return cost[n]
    elif n==1:
        return cost[n]

    return cost[n]+min(minCost1(n-1,cost),minCost1(n-2,cost))
    
print(minCostClimbingStairs1(cost))

