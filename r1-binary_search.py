def bSearch(A,i,j,a):
    while(i<=j):
        mid = int((i+j)/2)
        if a == A[mid]: return mid
        if a < A[mid]: j=mid-1
        if a>A[mid]: i=mid+1
    return -1


def binarySearch(A,B):
    for i in range(0,len(B)):
        print(bSearch(A,0,len(A)-1,B[i]),end=' ')


def readFromText():
    #import sys
    #sys.setrecursionlimit(2000)
    filepath = 'C:\\workspace\\python\\numbers.txt'
    content = []
    with open(filepath,'r') as f:
        A_length = f.readline().strip()
        B_length = f.readline().strip()
        content = f.readline()
        #for line in f:
	    #    numbers_str=line.split()

    print(A_length)
    print(B_length)
    print('hi!alpaca')
    print(content)
    print(type(content))
    #binarySearch(numbers_str[0:int(A_length)], numbers_str[int(A_length):int(A_length+B_length)])
