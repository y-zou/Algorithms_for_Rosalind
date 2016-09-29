A=[[1,2],[1,5],[5,9],[5,10],[9,10],[3,4],[3,7],[3,8],[4,8],[7,11],[8,11],[11,12],[8,12]]

import collections
neighbor=collections.defaultdict(list)
linked_v=[]
max_vertice = -1
for i in range(0,len(A)):
    vertice_pair_max = max(A[i][0],A[i][1])
    if max_vertice<vertice_pair_max:
        max_vertice=vertice_pair_max
    neighbor[A[i][0]].append(A[i][1])
    neighbor[A[i][1]].append(A[i][0])
    linked_v.append(A[i][0])
print(neighbor)
print(linked_v)

isolated_vertice = max_vertice - len(linked_v)
sum = 0 + isolated_vertice

#sum+=1 when the current node's all neighbors has been iterated
while linked_v:
    node = linked_v.pop()
    while neighbor[node]:
        next_node = neighbor[node].pop()
        if next_node in linked_v:
            node = next_node
            linked_v.remove(next_node)
    sum = sum+1
        


print('bunny')
print(sum)
