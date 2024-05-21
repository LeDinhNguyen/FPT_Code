class Student:
    def __init__(self, id: int, name: str, year: int, major: str, grade: float):
        self.id = id
        self.name = name
        self.year = year
        self.major = major
        self.grade = grade

    def showInfo(self):
        print(f'ID: {self.id} - Name: {self.name} - Year: {self.year} - Major: {self.major} - Grade: {self.grade}')


class Node:
    def __init__(self, data: Student):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        else:
            lHeight = self.height(node.left)
            rHeight = self.height(node.right)
            if lHeight > rHeight:
                return lHeight + 1
            else:
                return rHeight + 1

    def printCurrentLevel(self, node, level):
        if node is None:
            return
        elif level == 1:
            node.data.showInfo()
        else:
            self.printCurrentLevel(node.left, level - 1)
            self.printCurrentLevel(node.right, level - 1)

    def printLevelOrder(self):
        h = self.height(self.root)
        for i in range(1, h+1):
            self.printCurrentLevel(self.root, i)

    def inOrder(self, node):
        if node is not None:
            self.inOrder(node.left)
            node.data.showInfo()
            self.inOrder(node.right)

    def search(self, root: Node, key: str):
        if root is None or root.data.name == key:
            return root
        elif root.data.name < key:
            return self.search(root.right, key)
        else:
            return self.search(root.left, key)

    def searchId(self, root: Node, key: int):
        if root is None or root.data.id == key:
            return root
        elif root.data.id < key:
            return self.searchId(root.right, key)
        else:
            return self.searchId(root.left, key)

    def insert(self, root: Node, data: Student):
        newNode = Node(data)
        if root is None:
            return newNode
        elif root.data.id < data.id:
            root.right = self.insert(root.right, data)
        else:
            root.left = self.insert(root.left, data)
        return root

    def minValue(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def delete(self, root, key: int):
        if root is None:
            return root
        if key < root.data.id:
            root.left = self.delete(root.left, key)
        elif key > root.data.id:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                tmp = root.right
                root = None
                return tmp
            elif root.left is None:
                tmp = root.right
                root = None
                return tmp
            tmp = self.minValue(root.right)
            root.data = tmp.data
            root.right = self.delete(root.right, tmp.data)
        return root


def displayMenu():
    print("""
1. Insert Student
2. Search by Name
3. Delete by ID
4. Update by ID
5. Display class
6. Exit
""")


stuManTree = BinaryTree()
while True:
    displayMenu()
    choice = int(input("Enter your choice: "))
    print("/////////////")
    if choice == 6:
        break
    elif choice == 1:
        id = int(input("Enter id: "))
        name = input("Enter name: ")
        year = int(input("Enter year: "))
        major = input("Enter major: ")
        grade = float(input("Enter grade: "))
        stuManTree.root = stuManTree.insert(stuManTree.root, Student(id, name, year, major, grade))
    elif choice == 2:
        searchName = str(input("Enter name: "))
        if stuManTree.search(stuManTree.root, searchName) is None:
            print("Student not found")
        else:
            student = stuManTree.search(stuManTree.root, searchName)
            student.data.showInfo()
    elif choice == 3:
        delete = int(input("Insert delete key: "))
        stuManTree.delete(stuManTree.root, delete)
    elif choice == 4:
        updateId = int(input("Enter ID u want to update: "))
        if stuManTree.searchId(stuManTree.root, updateId) is None:
            print("Student not found")
        else:
            name = input("Enter name: ")
            year = int(input("Enter year: "))
            major = input("Enter major: ")
            grade = float(input("Enter grade: "))
            stuManTree.searchId(stuManTree.root, updateId).data = Student(updateId, name, year, major, grade)
    elif choice == 5:
        stuManTree.printLevelOrder()