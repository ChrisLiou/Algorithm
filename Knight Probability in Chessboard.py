
# #Brute Force
# def knightProbabilityInChessboard1(n,k,row,column):
#     if row<0 or row>=n or column<0 or column>=n:
#             return 0
#     if k==0:
#         return 1
#     result=0
#     for i in range(len(Direction)):
#         x=Direction[i][0]
#         y=Direction[i][1]
#         result+=knightProbabilityInChessboard1(n,k-1,row+x,column+y)/8
#     return result



#Memoization


# class Solution:
#     def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
#         dp=[[[None]*n]*n]*(k+1)
#         Direction=[[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
#         return self.recursion(dp,n,k,row,column,Direction)

#     def recursion(self,dp,n,k,row,column,Direction):
#         if row<0 or row>=n or column<0 or column>=n:
#             return 0
#         if k==0:
#             return 1
#         if dp[k][row][column]!=None:
#             return dp[k][row][column]
#         result=0
#         for i in range(len(Direction)):
#             x=Direction[i][0]
#             y=Direction[i][1]
#             result+=self.recursion(dp,n,k-1,row+x,column+y,Direction)/8

#         dp[k][row][column]=result

#         return dp[k][row][column]

#DP Bottom up
# n=3
# k=2
# row=0
# column=0
# Direction=[[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
# def knightProbability(n: int, k: int, row: int, column: int) -> float:
#     #dp=[[[0]*n]*n]*(k+1)
#     dp=[[[0 for k in range(n)] for j in range(n)] for i in range(k+1)]
#     Direction=[[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
#     dp[0][row][column]=1
#     for step in range(1,k+1):
#         for r in range(n):
#             for c in range(n):
#                 result=0
#                 for d in range(len(Direction)):
#                     x=Direction[d][0]
#                     y=Direction[d][1]
#                     if r+x>=0 and r+x<n and c+y>=0 and c+y<n:
#                         result+=dp[step-1][r+x][c+y]/8
#                 dp[step][r][c]=result
#     res=0
#     for i in range(n):
#         for j in range(n):
#             res+=dp[k][i][j]
#     return res

    

# print(knightProbability(n,k,row,column))

#DP Bottom up Optimization
n=3
k=2
row=0
column=0
Direction=[[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
def knightProbability(n: int, k: int, row: int, column: int) -> float:
    #dp=[[[0]*n]*n]*(k+1)
    #dp=[[[0 for k in range(n)] for j in range(n)] for i in range(2)]
    dp_pre=[[0 for k in range(n)] for j in range(n)]
    dp=[[0 for k in range(n)] for j in range(n)]

    Direction=[[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]
    dp_pre[row][column]=1
    for step in range(1,k+1):
        for r in range(n):
            for c in range(n):
                result=0
                for d in range(len(Direction)):
                    x=Direction[d][0]
                    y=Direction[d][1]
                    if r+x>=0 and r+x<n and c+y>=0 and c+y<n:
                        result+=dp_pre[r+x][c+y]/8
                dp[r][c]=result
        dp_pre=dp
        dp=[[0 for k in range(n)] for j in range(n)]
        
    res=0
    for i in range(n):
        for j in range(n):
            res+=dp_pre[i][j]
    return res

    

print(knightProbability(n,k,row,column))