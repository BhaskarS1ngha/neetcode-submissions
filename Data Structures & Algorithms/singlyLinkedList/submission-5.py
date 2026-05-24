class node:
    def __init__(self, val, next=None ):
        self.val = val
        self.next = next
        

class LinkedList:
    
    def __init__(self):
        self.head:node = None
        self.tail:node = None
    
    def get(self, index: int) -> int:
        counter = 0
        temp = self.head
        while temp:
            if counter == index:
                return temp.val
            counter +=1
            temp = temp.next
        return -1

    def insertHead(self, val: int) -> None:
        temp = node(val)
        if self.head is None:
            self.tail = temp
        else:
            temp.next = self.head
        self.head = temp

    def insertTail(self, val: int) -> None:
        temp = node(val,None)
        if self.tail is None:
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp

    def remove(self, index: int) -> bool:
        if index == 0:
            try:
                self.head = self.head.next
                return True
            except AttributeError:
                return False
        

        i = 1
        temp = self.head
        while i < index and temp:
            i += 1
            temp = temp.next

        if temp and temp.next:
            if temp.next == self.tail:
                self.tail = temp
            temp.next = temp.next.next
            return True
        
        return False
            

    def getValues(self) -> List[int]:
        temp = self.head
        res = []
        while temp:
            res.append(temp.val)
            temp = temp.next
        return res
