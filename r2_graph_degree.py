graph={}
A=[[6,7],[1,2],[2,3],[6,3],[5,6],[2,5],[2,4],[4,1]]
for i in range(0,len(A)):
    for j in range(0,2):
        key = A[i][j]
        if key in graph:
            graph[key] += 1
        else:
            graph[key] = 1
print(graph.values())
