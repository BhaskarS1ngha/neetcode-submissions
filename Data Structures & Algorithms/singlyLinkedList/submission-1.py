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
        if self.head is None:
            self.head = node(val)
            self.tail = self.head
        else:
            temp = node(val,next = self.head)
            self.head = temp

    def insertTail(self, val: int) -> None:
        temp = node(val,None)
        if self.tail is None:
            self.head = temp
        else:
            self.tail.next = temp
        self.tail = temp

    def remove(self, index: int) -> bool:
        if index == 0 and self.head is not None:
            temp = self.head
            self.head = self.head.next
            del temp
            return True
        
        temp = self.head
        i = 1
        while temp and i < index:
            temp = temp.next
            i += 1
            
        if temp and temp.next:
            target = temp.next
            if target == self.tail:
                self.tail = temp
            temp.next = target.next
            del target
            return True
        return False
            

    def getValues(self) -> List[int]:
        temp = self.head
        res = []
        while temp:
            res.append(temp.val)
            temp = temp.next
        return res
