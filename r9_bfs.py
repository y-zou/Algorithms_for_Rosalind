import collections
#put vertice into dict first
graph = collections.defaultdict(list)
distance = collections.defaultdict(int)
distance[1] = 0
A=[[6,7],[1,2],[2,3],[5,6],[2,5],[2,4],[1,4],[1,5],[1,7],[1,3],[4,8],[8,10],[10,11]]

max_vertice = -1
for i in range(0,len(A)):
    #find the max vertice
    if max_vertice<A[i][0]:
        max_vertice=A[i][0]
    if max_vertice<A[i][1]:
        max_vertice=A[i][1]

    key = A[i][0]
    graph[key].append(A[i][1])
print(graph)
print('\n')

for i in range(2,max_vertice+1):
    distance[i]=-1

print(distance)

adj_queue = [1]
while adj_queue:
    key = adj_queue.pop(0)
    new_distance = distance[key]+1

    if key in graph:
        for i in graph[key]:
            print(i, end = '    ')
            if distance[i] == -1 or distance[i]>new_distance:
                distance[i] = new_distance
            adj_queue.append(i)


print(distance)
