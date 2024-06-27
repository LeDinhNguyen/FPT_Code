class Node:
    def __init__(self, value: int):
        self.__value = value
        self.__next = None

    def getValue(self):
        return self.__value

    def setValue(self, newValue: int):
        self.__value = newValue

    def getNext(self):
        return self.__next

    def setNext(self, newNode):
        self.__next = newNode


class CircleLinkedList:
    def __init__(self):
        self.__tail = None
        self.__size = 0

    def insertFirst(self, value: int):
        newNode = Node(value)
        if self.__size == 0:
            self.__tail = newNode
            self.__tail.setNext(newNode)
        else:
            newNode.setNext(self.__tail.getNext())
            self.__tail.setNext(newNode)
        self.__size += 1

    def insertLast(self, value: int):
        newNode = Node(value)
        if self.__tail == None:
            self.__tail = newNode
            self.__tail.setNext(newNode)
        else:
            newNode.setNext(self.__tail.getNext())
            self.__tail.setNext(newNode) 
            self.__tail = newNode # update tail
        self.__size += 1 # update size

    def insertAfter(self, value: int, newValue: int):
        newNode = Node(newValue)
        if self.__tail.getNext() is None:
            self.__tail = newNode
            self.__tail.setNext(newNode)
            return
        pointer = self.__tail.getNext()
        while not pointer.getValue() == value:
            pointer = pointer.getNext()
            if pointer == self.__tail.getNext():
                print("No value found")
                return False
        newNode.setNext(pointer.getNext())
        pointer.setNext(newNode)
        self.__size += 1

    def removeFirst(self):
        if self.__tail is None:
            print("Linked List is empty!!!")
        else:
            temp = self.__tail.getNext()
            self.__tail.setNext(temp.getNext())
            temp = None
        self.__size -= 1

    def removeLast(self):
        if self.__tail is None:
            print("Linked List is empty!!!")
        else:
            pointer = self.__tail.getNext()
            while pointer.getNext() != self.__tail:
                pointer = pointer.getNext()
            pointer.setNext(self.__tail.getNext())
            self.__tail = pointer
        self.__size -= 1

    def removeAfter(self, value: int):
        if self.__tail.getNext() is None:
            print("Linked List is empty!!!")
        else:
            pointer = self.__tail.getNext()
            while pointer.getValue() != value:
                pointer = pointer.getNext()
                if pointer.getValue() == self.__tail.getNext():
                    print("No value found")
                    return False
            temp = pointer.getNext()
            pointer.setNext(temp.getNext())
            temp = None
        self.__size -= 1

    def display(self):
        if self.__size == 0:
            print("Empty Linked List!!!")
        elif self.__size == 1:
            print(self.__tail.getValue())
        else:
            temp = self.__tail.getNext()
            while temp != self.__tail:
                print(temp.getValue(), end=" ")
                temp = temp.getNext()
            print(temp.getValue())

    def search(self, value: int):
        if self.__tail is None:
            print("Empty List!")
            return
        pointer = self.__tail.getNext()
        while pointer is not self.__tail:
            if pointer.getValue() == value:
                return pointer
            pointer = pointer.getNext()
        return None

    def update(self, oldValue: int, newValue: int):
        if self.__tail.getNext() is None:
            print("Linked List is empty!!!")
            return
        pointer = self.__tail.getNext()
        while not pointer.getValue() == oldValue:
            pointer = pointer.getNext()
            if pointer.getValue() == self.__tail.getNext():
                print("No Id found")
                return
        pointer.setValue(newValue)

def menu():
    print("Circle Linked List Menu")
    print("1. Insert First")
    print("2. Insert Last")
    print("3. Insert After")
    print("4. Remove First")
    print("5. Remove Last")
    print("6. Remove After")
    print("7. Display")
    print("8. Search")
    print("9. Update")
    print("10. Exit")

def main():
    cll = CircleLinkedList()
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 1:
            value = int(input("Enter the new value to insert: "))
            cll.insertFirst(value)
        elif choice == 2:
            value = int(input("Enter the new value to insert: "))
            cll.insertLast(value)
        elif choice == 3:
            newValue = int(input("Enter the new value to insert: "))
            idValue = int(input("Enter the value after which to insert: "))
            cll.insertAfter(idValue, newValue)
        elif choice == 4:
            cll.removeFirst()
        elif choice == 5:
            cll.removeLast()
        elif choice == 6:
            idValue = int(input("Enter the value after which to remove: "))
            cll.removeAfter(idValue)
        elif choice == 7:
            cll.display()
        elif choice == 8:
            value = int(input("Enter the value to search: "))
            cll.search(value)
        elif choice == 9:
            value = int(input("Enter the value to update: "))
            newValue = int(input("Enter the new value: "))
            cll.update(value, newValue)
        elif choice == 10:
            break
        else:
            print("Invalid Choice!")


if __name__ == "__main__":
    main()