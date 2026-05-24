class DynamicArray:
    
    def __init__(self, capacity: int):
        self.dynamic_list = [None] *capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.dynamic_list[i]

    def set(self, i: int, n: int) -> None:
        self.dynamic_list[i] = n

    def pushback(self, n: int) -> None:
        if self.size >= self.capacity:
            self.resize()
        self.set(self.size,n) 
        self.size +=1

    def popback(self) -> int:
        self.size -= 1
        return self.dynamic_list.pop(self.size)

    def resize(self) -> None:
        self.dynamic_list += [None for _ in range(self.capacity)]
        self.capacity *=2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
