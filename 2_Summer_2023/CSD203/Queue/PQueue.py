class Student:
    def __init__(self, id, name, mark):
        self.__id = id
        self.__name = name
        self.__mark = mark

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getMark(self):
        return self.__mark

    def setId(self, new_id):
        self.__id = new_id

    def setName(self, new_name):
        self.__name = new_name

    def setMark(self, new_mark):
        self.__mark = new_mark

    def show(self):
        return f'id: {self.__id}, name: {self.__name}, mark: {self.__mark}'


class Node:
    def __init__(self, data=None):
        self.__data = data
        self.__next = None

    def get_data(self):
        return self.__data

    def set_data(self, new_data):
        self.__data = new_data

    def get_next(self):
        return self.__next

    def set_next(self, new_next):
        self.__next = new_next

class PQueue:
    def __init__(self):
        self.__head = None
        self.__size = 0

    #
    # def find(self, key): #Trả  về p(Node) sao cho key vừa lớn hơn thằng data và bé hơn thang next
    #     if self.__size == 0:
    #         return self.__head
    #     elif self.__size == 1:

    def add(self, key, value):
        newNode = Node(value)
        if self.__size == 0:
            self.__head = newNode
            self.__size += 1
        elif self.__size == 1:
            if self.__head.get_data().getId() > key:
                newNode.set_next(self.__head)
                self.__head = newNode
                self.__size += 1
            else:
                self.__head.set_next(newNode)
                self.__size += 1
        elif key < self.__head.get_data().getId():
            newNode.set_next(self.__head)
            self.__head = newNode
            self.__size += 1
        else:
            p = self.__head
            while p.get_next() is not None:
                if p.get_data().getId() < key < p.get_next().get_data().getId():
                    break
                p = p.get_next()
            if p.get_next() is None:
                p.set_next(newNode)
                self.__size += 1
            else:
                newNode.set_next(p.get_next())
                p.set_next(newNode)
                self.__size += 1

    def removeMin(self):
        if self.__head is None:
            print("Linked List is empty!!!")
            return
        temp = self.__head
        self.__head = self.__head.getNext()
        temp = None
        self.__size -= 1

    def display(self):
        if self.__size == 0:
            print('Empty')
        else:
            p = self.__head
            while p is not None:
                print(p.get_data().show())
                p = p.get_next()

st = Student(1, "x", 3)
p = PQueue()
p.display()
print('//')
p.add(1, st)
p.display()
print('//')
p.add(3, Student(3, "a", 3))
p.add(5, Student(5, "b", 3))
p.add(4, Student(4, "c", 3))
p.add(9, Student(9, "ad", 3))
p.display()
print('//')