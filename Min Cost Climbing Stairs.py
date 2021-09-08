
# #Brute Force
# cost=[10,15,20]

# def minCostClimbingStairs1(cost):
#     n=len(cost)
#     cost.append(0)

#     return minCost1(n,cost)

# def minCost1(n,cost):
#     if n<0:
#         return 0
#     elif n==0:
#         return cost[n]
#     elif n==1:
#         return cost[n]

#     return cost[n]+min(minCost1(n-1,cost),minCost1(n-2,cost))
    
# print(minCostClimbingStairs1(cost))

# DP
# cost=[10,15,20]

# def minCostClimbingStairs2(cost):
#     minCost=[]
#     minCost.append(cost[0])
#     minCost.append(cost[1])
#     cost.append(0)
#     for i in range(2,len(cost)):
#         minCost.append(0)

#     for i in range(2,len(cost)):
#         minCost[i]=cost[i]+min(minCost[i-1],minCost[i-2])

#     return minCost[len(minCost)-1]
    
# print(minCostClimbingStairs2(cost))


#Memorization
# cost=[10,15,20]

# def minCostClimbingStairs3(cost):
#     n=len(cost)
#     dp=[None]*len(cost)


#     return min(minCost3(n-1,cost,dp),minCost3(n-2,cost,dp))

# def minCost3(n,cost,dp):
#     if n<0:
#         return 0
#     elif n==0:
#         dp[n]=cost[n]
#         return dp[n]
#     elif n==1:
#         dp[n]=cost[n]
#         return dp[n]
#     if dp[n]!=None:
#         return dp[n]

#     dp[n]=cost[n]+min(minCost3(n-1,cost,dp),minCost3(n-2,cost,dp))
#     return dp[n]
    
# print(minCostClimbingStairs3(cost))

#DP
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

