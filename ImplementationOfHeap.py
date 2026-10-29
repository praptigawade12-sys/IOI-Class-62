class BinaryTree:
    def __init__(self):
        self.items = []

    def parent(self,i):
        return (i-1)//2

    def size(self):
        return len(self.items)

    def left(self,i):
        return 2*i+1

    def right(self,i):
        return 2*i+2

    def get(self,i):
        return self.items[i]

    def getmax(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def extractmax(self):
        if self.size() == 0:
            return None

        largest = self.getmax()
        self.items[0]=self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest

    def max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)

        if l <= self.size()-1 and self.get(l) > self.get(i):
            largest = l
        else:
            largest = i
        if r <= self.size()-1 and self.get(r) > self.get(i):
            largest = r
        if largest != i:
            self.swap(largest,i)
            self.max_heapify(largest)

    def swap(self,i,j):
        self.items[i],self.items[j] = self.items[j],self.items[i]

    def insert(self,key):
        index = self.size()
        self.items.append(key)
        while index != 0:
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p,index)
            index = p

heap = BinaryTree()
print("""
Menu :-
Insert __
Max Get
Max Extract
Exit""")

while True:
    do = input("What would you like to do ?").split()

    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        heap.insert(data)

    elif operation == 'max':
        subop = do[1].strip().lower()
        if subop == 'get':
            print("Max value is {}".format(heap.getmax()))
        elif subop == "extract":
            print("Max value removed {}".format(heap.extractmax()))

    elif operation == 'exit':
        break

    else:
        print("Invalid Input")
        continue