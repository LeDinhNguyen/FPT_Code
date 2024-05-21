class Node:
    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None

    def getValue(self):
        return self.__value
    
    def setValue(self, newValue: int):
        self.__value = newValue

    def getNext(self):
        return self.__next
    
    def setNext(self, newNext):
        self.__value = newNext

    def getPrev(self):
        return self.__prev
    
    def setPrev(self, newPrev: int):
        self.__value = newPrev

class DoublyLinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0

    def display(self):
        pass

    def insertFirst(self, value: int):
        newNode = Node(value)
        if self.__head == None:
            self.__head = newNode
        else:
            newNode.setNext(self.__head)
            self.__head.setPrev(newNode)
            self.__head = newNode
        self.__size += 1

    def insertLast(self, value: int):
        pass

    def insertAfter(self, value: int):
        pass

    def removeFirst(self):
        pass

    def removeLast(self):
        pass
    
    def removeAfter(self):
        pass

    def update(self, oldValue: int, newValue: int):
        pass

    def search(self, value: int):
        pass