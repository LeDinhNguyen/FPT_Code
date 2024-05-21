import ctypes
from random import randint


class DynamicArray:
    def __init__(self):
        self.__size = 0
        self.__capacity = 1
        self.__element = self._makeArray(self.__capacity)

    @staticmethod
    def _makeArray(capacity):
        return (capacity * ctypes.py_object)()

    def display(self):
        print("Actual size: ", self.__size)
        print("Actual capacity: ", self.__capacity)

        for i in range(self.__size):
            print(self.__element[i], end=" ")

        print(" ")

    def __len__(self):
        return self.__size

    def _reSize(self, capacity):
        b = self._makeArray(capacity)
        for k in range(self.__size):
            b[k] = self.__element[k]
        self.__element = b
        self.__capacity = capacity

    def append(self, obj):
        if self.__size == self.__capacity:
            self._reSize(self.__capacity * 2)
        self.__element[self.__size] = obj
        self.__size += 1

    def insert(self, index, obj):
        if self.__size == self.__capacity:
            self._reSize(self.__capacity * 2)
        for i in range(self.__size, index, -1):
            self.__element[i] = self.__element[i-1]

        self.__element[index] = obj
        self.__size += 1

    def removeByIndex(self, index):
        if index >= self.__size:
            return "Index is out of size"
        else:
            for i in range(index, self.__size - 1):
                self.__element[i] = self.__element[i+1]
            self.__element[self.__size - 1] = None
            self.__size -= 1

    def removeByValue(self, value):
        i = 0
        while i < self.__size:
            if self.__element[i] != value:
                i += 1
            else:
                self.removeByIndex(i)

    def update(self, index, value):
        self.__element[index] = value
        return True

    def search(self, value):
        for i in range(self.__size):
            if self.__element[i] == value:
                print("index: ", i)
                return i
        print("Valid is not found!")
        return -1




def main():
    obj = DynamicArray()
    obj.append(randint(1, 11))
    obj.append(randint(1, 11))
    obj.append(randint(1, 11))
    obj.append(randint(1, 11))
    obj.append(randint(1, 11))
    obj.append(randint(1, 11))
    obj.display()
    # obj.removeByIndex(2)
    num = int(input("Enter number to remove: "))
    obj.removeByValue(num)
    obj.display()


if __name__ == "__main__":
    main()


