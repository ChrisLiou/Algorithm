testMatrix = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20]
]

# directions = [
#   [-1, 0], //up
#   [0, 1], //right
#   [1, 0], //down
#   [0, -1] //left
# ]

def traversalDFS(matrix):
    seen = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))] 
    
    values = []

    def dfs(matrix, row, col, seen, values):
        if row<len(matrix) and row>=0 and col<len(matrix[0]) and col>=0 and seen[row][col]==False:
            values.append(matrix[row][col])
            seen[row][col]=True
            dfs(matrix,row-1,col,seen,values)
            dfs(matrix,row,col+1,seen,values)
            dfs(matrix,row+1,col,seen,values)
            dfs(matrix,row,col-1,seen,values)

    dfs(matrix, 0, 0, seen, values)

    print(values)

def traversalBFS(matrix):
    seen = [[False for x in range(len(matrix[0]))] for y in range(len(matrix))] 
    seen[0][0]=True
    myQueue=[[0,0]]
    values = [matrix[0][0]]

    def bfs(matrix, row, col, seen, values):
        while len(myQueue)>0:
            [row,col]=myQueue.pop(0)
    
            if row-1>=0 and seen[row-1][col]==False:
                myQueue.append([row-1,col])
                values.append(matrix[row-1][col])
                seen[row-1][col]=True
            if col+1<len(matrix[0]) and seen[row][col+1]==False:
                myQueue.append([row,col+1])
                values.append(matrix[row][col+1])
                seen[row][col+1]=True
            if row+1<len(matrix) and seen[row+1][col]==False:
                myQueue.append([row+1,col])
                values.append(matrix[row+1][col])
                seen[row+1][col]=True
            if col-1>=0 and seen[row][col-1]==False:
                myQueue.append([row,col-1])
                values.append(matrix[row][col-1])
                seen[row][col-1]=True
            

    bfs(matrix, 0, 0, seen, values)

    print(values)



#traversalDFS(testMatrix)
traversalBFS(testMatrix)



