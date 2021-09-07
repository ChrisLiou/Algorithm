n=3
k=2
row=0
column=0
Direction=[[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2],[-1,-2]]

def knightProbabilityInChessboard(n,k,row,column):
    if row<0 or row>=n or column<0 or column>=n:
            return 0
    if k==0:
        return 1
    result=0
    for i in range(len(Direction)):
        x=Direction[i][0]
        y=Direction[i][1]
        result+=knightProbabilityInChessboard(n,k-1,row+x,column+y)/8
    return result

print(knightProbabilityInChessboard(n,k,row,column))
