class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class Queue:
    def __init__(self) -> None:
        self.top = None
        self.size = 0

    def isEmpty(self):
        if self.size == 0:
            return True
        return False

    def enQueue(self, value):
        newNode = Node(value)
        if self.size == 0:
            self.top = newNode
        else:
            temp = self.top
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        self.size += 1

    def deQueue(self):
        if self.isEmpty():
            print("Empty Queue!!!")
        else: 
            temp = self.top
            self.top = self.top.next
        return temp

    def first(self):
        return self.top.value

    def last(self):
        temp = self.top
        while temp.next != None:
            temp = temp.next
        return temp.value

    def display(self):
        temp = self.top
        while temp != None:
            print(temp.value)
            temp = temp.next

    def length(self):
        return self.size
    
if __name__ == "__main__":
    queue = Queue()
    queue.enQueue(1)
    queue.enQueue(2)
    queue.enQueue(4)
    queue.enQueue(3)
    print("first: ",queue.first())
    print("last: ",queue.last())
    print("len: ",queue.length())
    queue.deQueue()
    queue.display()