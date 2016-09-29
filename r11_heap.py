A = [1,3,5,7,2]
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0


    def perUp(self,i):
        while i // 2 >0:
            if self.heapList[i] < self.heapList[i//2]:
                self.heapList[i//2],self.heapList[i] = self.heapList[i],self.heapList[i//2]
            i = i // 2


    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.perUp(self.currentSize)

heap = BinHeap()
for i in A:
    heap.insert(i)
print(A)
