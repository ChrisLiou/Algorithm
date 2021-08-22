adjacencyList = [
  [1, 3],
  [0],
  [3, 8],
  [0, 2, 4, 5],
  [3, 6],
  [3],
  [4, 7],
  [6],
  [2]
]

def adjacencyListBFS(adjacencyList):
    myQ=[]
    res=[]
    myQ.append(0)
    while len(myQ)>0:
        currentNode=myQ.pop(0)
        res.append(currentNode)
        for i in range(len(adjacencyList[currentNode])):
            if adjacencyList[currentNode][i] not in res:
                myQ.append(adjacencyList[currentNode][i])
    return res

adjacencyMatrix = [
  [0, 1, 0, 1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 1],
  [1, 0, 1, 0, 1, 1, 0, 0, 0],
  [0, 0, 0, 1, 0, 0, 1, 0, 0],
  [0, 0, 0, 1, 0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1, 0, 0, 1, 0],
  [0, 0, 0, 0, 0, 0, 1, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 0]
]

def adjacencyMatrixBFS(adjacencyMatrix):
    myQ=[]
    res=[]
    myQ.append(0)
    while len(myQ)>0:
        currentNode=myQ.pop(0)
        res.append(currentNode)
        for i in range(len(adjacencyMatrix[currentNode])):
            if adjacencyMatrix[currentNode][i]==1 and i not in res:
                myQ.append(i)
    return res

        
#print(adjacencyListBFS(adjacencyList))
print(adjacencyMatrixBFS(adjacencyMatrix))
        
