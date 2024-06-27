class Customer:
    def __init__(self, id, name, level = 3):
        self.id = id
        self.name = name
        self.level = level

    def display(self):
        print(f"Level: {self.level} - ID: {self.id} - Name: {self.name}")

class Node:
    def __init__(self, value: Customer) -> None:
        self.value = value
        self.next = None

class PQueue:
    def __init__(self, capacity = 50) -> None:
        self.head = None
        self.size = 0
        self.capacity = capacity

    def enQueue(self, value: Customer):
        newNode = Node(value)

        # if self.size == 0:
        #     self.head = newNode
        # elif self.size == 1:
        #     if newNode.value.level >= self.head.value.level:
        #         newNode.next = self.head
        #         self.head = newNode
        #     else:
        #         self.head.next = newNode
        # elif newNode.value.level == 3:
        #     newNode.next = self.head
        #     self.head = newNode
        # elif newNode.value.level == 2:
        #     temp = self.head
        #     while not temp.next.value.level == 2:
        #         temp = temp.next
        #     newNode.next = temp.next
        #     temp.next = newNode
        # elif newNode.value.level == 1:
        #     temp = self.head
        #     while not temp.next.value.level == 1:
        #         temp = temp.next
        #     newNode.next = temp.next
        #     temp.next = newNode
        if self.size == 0 or newNode.value.level >= self.head.value.level:
            newNode.next = self.head
            self.head = newNode
        else:
            temp = self.head
            while temp.next and newNode.value.level < temp.next.value.level:
                temp = temp.next
            newNode.next = temp.next
            temp.next = newNode

        self.size += 1

    def deQueue(self):
        if self.size == 0:
            print("No Customer")
            return
        if self.size == 1:
            self.head = None
            return
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        last = temp.next
        temp.next = None
        last = None
        self.size -= 1

    def display(self):
        if self.size == 0:
            print("Empty")
        else:
            temp = self.head
            while temp !=  None:
                temp.value.display()
                temp = temp.next
        
def displayMenu():
    print("""
0. Exit
1. Insert Customer
2. Give Customer a room
3. Display
""")

def main():
    customerQueue = PQueue()
    while True:
        displayMenu()
        option = int(input("\nEnter your choice: "))
        if option == 1:
            id = str(input("Enter ID: "))
            name = str(input("Enter Name: "))
            level = int(input("""Choose Level:
            3. Normal customer
            2. Friendly Customer
            1. VVIP Customer
            """))
            if level in [1,2,3]:
                newCustomer = Customer(id, name, level)
                customerQueue.enQueue(newCustomer)
            else:
                print("Level no Specifided")
        elif option == 2:
            customerQueue.deQueue()
        elif option == 3:
            customerQueue.display()
        elif option == 0:
            break
        else:
            print("invalid option")

if __name__ == "__main__":
    main()