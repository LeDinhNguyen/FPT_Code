class Student:
    def __init__(self):
        self.stdid = None
        self.name = None
        self.address = None
        self.score = None

    def inputInfo(self):
        self.stdid = input("Enter Student's ID: ")
        self.name = input("Enter Student's Name: ")
        self.address = input("Enter Student's Address: ")
        self.score = int(input("Enter Student's score: "))
    
    def updateInfo(self):
        self.name = input("Enter name to update: ")
        self.address = input("Enter name to update: ")
        self.score = int(input("Enter name to update: "))
    
    def showInfo(self):
        print(f"ID: {self.stdid} - Name: {self.name} - Addres: {self.address} - Score: {self.score}")

class Node:
    def __init__(self, student: Student) -> None:
        self.value = student
        self.next = None

class StudentManagement:
    def __init__(self):
        self.head = None
        self.size = 0

    def checkID(self, stdid: str) -> bool:
        temp = self.head
        while temp.next is not None:
            if temp.value.stdid == stdid:
                return True
            
        return False
    
    def insert(self, student: Student):
        if self.head is None:
            self.head = Node(student)
            self.size += 1
        elif self.checkID(student.stdid):
            print("Same student id is not allowed!!!")
        else:
            newNode = Node(student)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            self.size += 1
            print("Student inserted successfully!!!")

    def update(self, stdid: str):
        temp = self.head
        while temp is not None and temp.value.stdid != stdid:
            temp = temp.next
        
        if temp is None:
            print("Student ID does not exist!!!")
        else:
            stu = temp.value
            stu.updateInfo()
            print("Student updated successfully!!!")

    def delete(self, stdid: str):
        if self.head is None:
            print("There is no student in the system!!!")
            return

        if self.head.value.stdid == stdid:
            self.head = self.head.next
            self.size -= 1
        
        curr = self.head
        temp = None
        if curr is not None and curr.value.stdid == stdid:
            prev = curr
            curr = curr.next

        if curr is None:
            print("Student ID does not exist!!!")
        else:
            prev.next == curr.next
            self.size -= 1
            print("Student deleted successfully!!!")

    def search(self, stdid: str):
        temp = self.head
        while temp is not None and temp.value.stdid != stdid:
            temp = temp.next
        
        if temp is None:
            print("Student ID does not exist!!!")
        else:
            stu = temp.value
            stu.showInfo()

        return False
    
    def showStudent(self):
        if self.size < 1:
            print("0000000")
        else:
            temp = self.head
            while temp is not None:
                temp.value.showInfo()
                temp = temp.next
    
def menu():
    print("""
    0. Exit
    1. Add
    2. Update
    3. Delete
    4. Search
    5. Show
    """)

def main():
    sys = StudentManagement()
    while True:
        menu()
        option = int(input("Choose option: "))
        if option == 0:
            break
        elif option == 1:
            newStudent = Student()
            newStudent.inputInfo()
            sys.insert(newStudent)
        elif option == 2:
            stdid = input("Enter ID to update: ")
            sys.update(stdid)
        elif option == 3:
            stdid = input("Enter ID to delete: ")
            sys.delete(stdid)
        elif option == 4:
            stdid = input("Enter ID to search: ")
            sys.search(stdid)
        elif option == 5:
            sys.showStudent()
            # print(sys.head.value.showInfo())

if __name__ == "__main__":
    main()