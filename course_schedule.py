prereqs1=[[1,0],[2,1],[2,5],[0,3],[4,3],[3,5],[4,5]]
prereqs2=[[2,0],[1,0],[3,1],[3,2],[1,3]]
numCourses=4

#Topological Sort
def canFinish(numCourses, prerequisites):
    result=[]
    graph=[]
    indegree=[]
    for i in range(numCourses):
        graph.append([])
        indegree.append(0)
    for i in range(len(prerequisites)):
        graph[prerequisites[i][1]].append(prerequisites[i][0])
        indegree[prerequisites[i][0]]+=1
    
    while 0 in indegree:
        for i in range(len(indegree)):
            if indegree[i]==0:
                result.append(i)
                indegree[i]-=1
                connection=graph[i]
                for j in range(len(connection)):
                    indegree[connection[j]]-=1

    return len(result)==numCourses

print(canFinish(numCourses,prereqs2))

#BFS

# def canFinish(numCourses, prerequisites) -> bool:
#     graph=[]
#     for i in range(numCourses):
#         graph.append([])
#     for i in range(len(prerequisites)):
#         graph[prerequisites[i][1]].append(prerequisites[i][0])
    
#     for i in range(len(graph)):
#         myQ=[]
#         seen={}
#         myQ.append(i)
#         while len(myQ)!=0:
#             currentNode=myQ.pop(0)
#             childNode=graph[currentNode]
#             seen[currentNode]=True
#             for j in range(len(childNode)):
#                 if childNode[j]==i:
#                     return False
#                 if not childNode[j] in seen:
#                     myQ.append(childNode[j])
#     return True


# print(canFinish(numCourses,prereqs))