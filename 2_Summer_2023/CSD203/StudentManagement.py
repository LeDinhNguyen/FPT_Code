class Student:
    def __init__(self) -> None:
        self.id: str = None
        self.name: str = None
        self.mark: int = None
    
    def create(self):
        self.id = input("Enter new student ID: ")
        self.name = input("Enter new student name: ")
        self.mark = int(input("Enter new student mark: "))

    def showInfo(self):
        print(f'ID: {self.id}, Name: {self.name}, Mark: {self.mark}')

    def update(self):
        print("Update student information:")
        self.name = input("Enter new name: ")
        self.mark = input("Enter new mark: ")
        self.id = input("Enter new id's student: ")

class Node:
    def __init__(self, stu: Student):
        self.value = stu
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def checkID(self, id: str):
        if self.head == None:
            print("Linked List is empty!!!")
            return False
        temp = self.head
        while temp != None:
            if temp.value.id == id:
                return True
            temp = temp.next
        return False
    
    def insertFirst(self):
        value = Student()
        value.create()
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        elif self.checkID(id):
            print("The student is existed!!!")
            return False
        else:
            newNode.next = self.head
            self.head = newNode
        self.size += 1
        return True

    def insertLast(self):
        value = Student()
        value.create()
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
        elif self.checkID(value.id):
            print("The student is existed")
            return False
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = newNode
        self.size += 1
        return True

    def insertAfter(self, id: str):
        value = Student()
        value.create()
        newNode = Node(value)
        #check
        if self.size == 0:
            self.head = newNode
            self.size = 1
            return True
        elif not self.checkID(id):
            print("The student is not existed")
            return False
        elif self.checkID(value.id):
            print("The student is existed")
            return False
        else:
            temp = self.head
            while temp.value.id != id:
                temp = temp.next
    
            newNode.next = temp.next
            temp.next = newNode

    def removeFirst(self):
        if self.head == None:
            print("Linked List is empty!!!")
            return False
        temp = self.head
        self.head = self.head.next
        temp = None
        self.size -= 1
        return 0
    
    def removeLast(self):
        if self.head == None:
            print("Linked List is empty!!!")
            return False
        temp = self.head
        last = temp.next
        while last.next != None:
            last = last.next
            temp = temp.next
        temp.next = None
        self.size -= 1

    def removeID(self, id: str):
        if self.head == None:
            print("The Linked List is empty!!!")
            return False
        elif self.head.value.id == id:
            return self.removeFirst()
        elif not self.checkID(id):
            print("The student is not existed!!!")
            return False
        prev = self.head
        curr = prev.next
        while curr.value.id != id:
            curr = curr.next
            prev = prev.next
        prev.next = curr.next
        curr.next = None
        curr = None

    def display(self):
        if self.head == None:
            print("Empty Linked list")
            return False
        temp = self.head
        while temp != None:
            temp.value.showInfo()
            temp = temp.next
        return True
        
    def update(self, id: str):
        if self.head == None:
            print("Linked List is empty!!!")
            return False
        elif not self.checkID(id):
            print("The student is not existed!!!")
            return False
        elif self.checkID(id):
            newValue = Student()
            newValue.create()
            temp = self.head
            while temp.value.id != id:
                temp = temp.next
            temp.value = newValue
        return True

    def search(self, id: str):
        if self.head is None:
            return "No value added!"
        elif not self.checkID(id):
            print("The student is not existed!!!")
            return False 
        else:
            if self.checkID(id):
                temp = self.head
                while temp.value.id != id:
                    if temp == None:
                        print("The student is not existed!!!")
                        return False
                    temp = temp.next
                return True

def main():
    def display_menu():
        print("\n\nMenu:")
        print("1. Insert at the beginning")
        print("2. Insert at the end")
        print("3. Insert after a node")
        print("4. Remove the first node")
        print("5. Remove the last node")
        print("6. Remove a node by ID")
        print("7. Display the linked list")
        print("8. Update a node by ID")
        print("9. Search for a node by ID")
        print("0. Exit")

    student_list = SinglyLinkedList()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            student_list.insertFirst()
        elif choice == "2":
            student_list.insertLast()
        elif choice == "3":
            id_to_insert_after = input("Insert after student: ")
            student_list.insertAfter(id_to_insert_after)
        elif choice == "4":
            student_list.removeFirst()
        elif choice == "5":
            student_list.removeLast()
        elif choice == "6":
            id_to_remove = input("Enter the ID to remove: ")
            student_list.removeID(id_to_remove)
        elif choice == "7":
            print("----------Student Management----------")
            student_list.display()
        elif choice == "8":
            id_to_update = input("Enter the ID to update: ")
            student_list.update(id_to_update)
        elif choice == "9":
            id_to_search = input("Enter the ID to search: ")
            student_list.search(id_to_search)
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Exiting the program.")

if __name__ == "__main__":
    main()