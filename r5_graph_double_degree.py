import collections
graph={}    #the value should be the vertice degree
neighbor=collections.defaultdict(list) #the value should be a list of adjacent vertex

A=[[6,7],[1,2],[2,3],[6,3],[5,6],[2,5],[2,4],[4,1]]
D=[]    #D is the output list

for i in range(0,len(A)):
    for j in range(0,2):
        key = A[i][j]
        if key in graph:    graph[key] += 1
        else:   graph[key] = 1
        if j == 0:  neighbor[key].append(A[i][1])
        if j == 1:  neighbor[key].append(A[i][0])

print(neighbor)
for k in neighbor:
    s = 0
    neighbor_list=neighbor[k]
    while neighbor_list:
        s = s + graph[neighbor_list.pop()]
    D.append(s)
print(D)
print(neighbor) #should be empty after pop everything out
print(graph)
print('bunny')





print(graph.values())
