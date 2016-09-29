A=[1,25,66,77,100]
B=[0,2,333]
m=5
n=3


C=[]
while A and B:
    if A[0]<B[0]:   C.append(A.pop(0))
    else:   C.append(B.pop(0))

while A: C.append(A.pop(0))
while B: C.append(B.pop(0))
print(C)
