#Memorization
cost=[10,15,20]

def minCostClimbingStairs3(cost):
    n=len(cost)
    dp=[None]*len(cost)


    return min(minCost3(n-1,cost,dp),minCost3(n-2,cost,dp))

def minCost3(n,cost,dp):
    if n<0:
        return 0
    elif n==0:
        dp[n]=cost[n]
        return dp[n]
    elif n==1:
        dp[n]=cost[n]
        return dp[n]
    if dp[n]!=None:
        return dp[n]

    dp[n]=cost[n]+min(minCost3(n-1,cost,dp),minCost3(n-2,cost,dp))
    return dp[n]
    
print(minCostClimbingStairs3(cost))

