A=[4,57,3,2,6]
length = 5


for i in range(1,length):
    j = i
    while j>0 and A[j]<A[j-1]:
        A[j-1],A[j] = A[j],A[j-1]
        j = j-1
print(A)
