class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.arr = list()
    
    def get(self, index: int) -> int:
        try:
            return self.arr[index]
        except IndexError:
            return -1

    def insertHead(self, val: int) -> None:
        if self.head is None:
            self.arr = [val]
            self.tail = val
        else:
            self.arr = [val]+self.arr
        self.head = val

    def insertTail(self, val: int) -> None:
        if self.tail is None:
            self.arr = [val]
            self.head = val
        else:
            self.arr.append(val)
        self.tail = val

    def remove(self, index: int) -> bool:
        try:
            self.arr.pop(index)
            return True
        except IndexError:
            return False

    def getValues(self) -> List[int]:
        return self.arr
