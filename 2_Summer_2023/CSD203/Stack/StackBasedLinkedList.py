from LinkedList.Node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def getSize(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        return False
    
    def push(self, value: int):
        newNode = Node(value)
        if self.size == 0:
            self.top = newNode
        else:
            temp = self.top
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        self.size += 1
    
    def pop(self):
        if self.isEmpty():
            print("Emtpy stack!!!")
            return None
        else:
            temp = self.top
            last = temp.next
            while last.next is not None:
                temp = temp.next
                last = last.next
            temp.next = None
            self.size -= 1
        return last.value

    def top(self):
        if self.isEmpty():
            print("Empty stack!!")
            return False
        return self.top.value
    
    def display(self):
        temp = self.top
        while temp != None:
            print(temp.value, end=" ")
            temp = temp.next
        print("")
        
    
stack = Stack()
print(stack.isEmpty())
a = stack.pop()
print(a)
stack.display()
print(stack.getSize())
