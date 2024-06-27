class Student:
    def __init__(self) -> None:
        self.stuId= None
        self.name = None 
        self.year = None
        self.major = None
        self.grade = None

    def showInfo(self):
        print(f"ID: {self.stuId} - Name: {self.name} - Year {self.year} - Major {self.major} - Grade {self.grade}")
    
    def insertInfo(self):
        self.stuId = int(input("Enter id: "))
        self.name = input("Enter name: ")
        self.year = int(input("Enter year: "))
        self.major = input("Enter major: ")
        self.grade = float(input("Enter grade: "))

    def updateInfo(self):
        self.name = input("Enter name: ")
        self.year = int(input("Enter year: "))
        self.major = input("Enter major: ")
        self.grade = float(input("Enter grade: "))

class Node:
    def __init__(self, data: Student) -> None:
        self.data = data
        self.right = None
        self.left = None

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def height(self, node: Node):
        if node == None:
            return 0 
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
        
    def printCurrentLevel(self, node: Node, level: int):
        if node == None:
            return 
        elif level == 1:
            node.data.showInfo()
        else:
            self.printCurrentLevel(node.left, level - 1)
            self.printCurrentLevel(node.right, level - 1)

    def printLevelOrder(self):
        h = self.height(self.root)
        for i in range(1, h + 1):
            self.printCurrentLevel(self.root, i)

    def inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            node.data.showInfo()
            self.inOrder(node.right)

    def preOrder(self, node):
        if node != None:
            node.data.showInfo()
            self.preOrder(node.left)
            self.postOrder(node.right)

    def postOrder(self, node):
        if node != None:
            self.postOrder(node.right)
            self.postOrder(node.left)
            node.data.showInfo()
        
    def insert(self, root: Node, student: Student):
        newNode = Node(student)
        if root is None:
            return newNode
        elif root.data.stuId < student.stuId:
            root.right = self.insert(root.right, student)
        else:
            root.left = self.insert(root.left, student)
        return root

    def deleteById(self, root: Node, keyId: str):
        if root == None:
            return None
        if root.data.stuId < keyId:
            root.right = self.deleteById(root.left, keyId)
        elif root.data.stuId > keyId:
            root.left = self.deleteById(root.left, keyId)
        else:
            if root.left == None:
                return root.right
            elif root.right ==None:
                return root.left
            temp = self.minValue(root.right)
            root.data = temp.data
            root.right = self.deleteById(root.right, temp.data)
        return root


    def searchByName(self, name: str):
        pass

    def searchById(self, root: Node, stuId: str):
        if root == None or root.data.stuId == stuId:
            return root
        elif root.data.stuId < stuId:
            return self.searchById(root.left, stuId)
        else:
            return self.searchById(root.right, stuId)

    def minValue(self, root):
        curr = root
        while curr.left != None:
            curr = curr.left
        return curr




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
        newStudent = Student()
        newStudent.insertInfo()
        stuManTree.root = stuManTree.insert(stuManTree.root, newStudent)
    elif choice == 2:
        searchName = str(input("Enter name: "))
        if stuManTree.search(stuManTree.root, searchName) is None:
            print("Student not found")
        else:
            student = stuManTree.search(stuManTree.root, searchName)
            student.data.showInfo()
    elif choice == 3:
        delete = int(input("Insert delete key: "))
        stuManTree.deleteById(stuManTree.root, delete)
    elif choice == 4:
        updateId = int(input("Enter ID u want to update: "))
        if stuManTree.searchById(stuManTree.root, updateId) is None:
            print("Student not found")
        else:
            # name = input("Enter name: ")
            # year = int(input("Enter year: "))
            # major = input("Enter major: ")
            # grade = float(input("Enter grade: "))
            foundedNode = stuManTree.searchById(stuManTree.root, updateId)
            foundedNode.data.updateInfo()
    elif choice == 5:
        stuManTree.printLevelOrder()
        # root.leftdata.showInfo()