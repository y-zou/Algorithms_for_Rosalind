#algorithm: 1.use dictionary. when key, value=value+1, if value>n/2, return key runningtime:O(n) Memory:(n^2)
# 2. sort(). count=1. k=the n/2th element. count how may k value when k going forward and backward. runningtime:O(nlogn) Memory: O(n)

A=[2,2,4,2,3,22,1,2,2,2,2]
A.sort()
l = int(len(A)/2)
majority = A[l]
count = 1   #count the time the value majority appears
i,j=l+1,l-1

while i<len(A) and A[i] == majority:
    count=count+1
    i=i+1
while j>=0 and A[j] == majority:
    count=count+1
    j=j-1

if count<l+1:
    majority =-1
print(majority)
