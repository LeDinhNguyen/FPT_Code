class AirPort():
    def __init__(self, name: str):
        self.name = name
        self.cost = [0]
        self.number = 0

class AirPortMatrix():
    def __init__(self):
        self.matrix = []
        self.size = 0

    def addAirport(self, newAirport: AirPort):
        if self.size == 0:
            self.matrix.append(newAirport)
            self.size += 1
        else:
            newAirport.number = self.size
            tempSize = self.size
            while tempSize > 0:
                tempSize -= 1
                cost = int(input(f"Cost from Airport: {newAirport.number} to Airport: {tempSize} : "))
                # cost = randint(0,200)
                newAirport.cost.insert(0,cost)
                self.matrix[tempSize].cost.append(cost)
            self.matrix.append(newAirport)
            self.size += 1
        print("inserted sucessfuly!")

    def deleteAirport(self, number: int):
        for i in range(self.size):
            self.matrix[i].cost.pop(number)
        self.matrix.pop(number)
        self.size -= 1
        for i in range(self.size):
            self.matrix[i].number = i

    def updateAirport(self, number: int):
        newAirport = AirPort(number)
        for i in range(self.size):
            if i == number:
                self.matrix[number].cost[i] = 0
            else:
                tempSize = self.size
                cost = int(input(f"Cost from Airport: {newAirport.number} to Airport: {tempSize} : "))
                # cost = randint(0,200)
                self.matrix[number].cost[i] = cost
                self.matrix[i].cost[number] = cost

    def toMatrix(self):
        spacing = 4
        print(f"{''.ljust(spacing)}", end="| ")
        for i in range(self.size):
            print(str(self.matrix[i].name+str(self.matrix[i].number)).ljust(spacing), end='| ')
        print()
        for i in range(self.size):
            print(f"{str(self.matrix[i].name).ljust(spacing)}", end="| ")
            for j in range(self.size):
                print(f"{str(self.matrix[i].cost[j]).ljust(spacing)}", end='| ')
            print()

    def listOfCost(self):
        list = []
        for i in range(self.size):
            list.append(self.matrix[i].cost)
        return list

    def dijkstra(self, start, end):
        numNodes = self.size
        distances = {node: float('inf') for node in range(numNodes)}
        distances[start] = 0
        visited = set()
        previous = {}
        # Xét cho tới khi đi qua hết các điểm
        while len(visited) < numNodes:
            # Tìm khoảng cách ngắn nhất nè :0
            min_distance = float('inf')
            currentNode = None
            for node in range(numNodes):
                if node not in visited and distances[node] < min_distance:
                    min_distance = distances[node]
                    currentNode = node
            # Tới cái end node thì dừng thoai
            if currentNode == end:
                break
            else:
                # Nếu chưa tới thì cũng tìm được cái ngắn nhất thì update vào hàng sẽ đi qua
                visited.add(currentNode)
            # xét mấy đứa hàng xóm láng giềng cua currentNode
            for neighbor in range(numNodes):
                if neighbor not in visited and self.listOfCost()[currentNode][neighbor] > 0:
                    new_distance = distances[currentNode] + self.listOfCost()[currentNode][neighbor]
                    # Update thông tin nếu thấy ngắn hơn
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
                        previous[neighbor] = currentNode

        # từ cái visited mình dựng ngược lại cái path
        path = []
        current = end
        while current in previous:
            path.append(current)
            current = previous[current]
        path.append(start)
        path.reverse()

        return path, distances[end]

# sys = AirPortMatrix()
# # input()
# for i in range(300):
#     sys.addAirport(AirPort(str(i)))
# sys.toMatrix()
# print(sys.listOfCost())
# sys.deleteAirport(2)
# sys.toMatrix()
# print(sys.listOfCost())
# sys.deleteAirport(0)
# sys.toMatrix()
# print(sys.listOfCost())
# sys.deleteAirport(sys.size-1)
# sys.toMatrix()
# print(sys.listOfCost())
# sys.addAirport(AirPort("Hùng"))
# sys.toMatrix()
# print(sys.listOfCost())
# sys.addAirport(AirPort("Hùng"))
# sys.toMatrix()
# print(sys.listOfCost())
# sys.updateAirport(1)
# sys.updateAirport(2)
# sys.updateAirport(3)
# sys.toMatrix()
# print(sys.listOfCost())


'''start_node = 1
end_node = 215
path, total_cost = sys.dijkstra(start_node, end_node)
print(f'Shortest path from {sys.matrix[start_node].name} to {sys.matrix[end_node].name}')
for i in path:
    for j in range(len(sys.matrix)):
        if sys.matrix[j].number == i:
            print(sys.matrix[j].name, end='  ')
print()
print("Total cost:", total_cost)
# sys.toMatrix()
print(sys.listOfCost())'''

def menu():
    print("""
    0. Exit
    1. Add airport
    2. Delete airport
    3. Update airport
    4. Lowes cost from A to B
    """)

if __name__ == "__main__":
    sys = AirPortMatrix()
    while True:
        menu()
        choice = int(input("Enter your choice: "))
        if choice == 0:
            break
        elif choice == 1:
            name = str(input("Enter airport name: "))
            sys.addAirport(AirPort(name))
        elif choice == 2:
            deleteNumber = int(input("Enter number of airport: "))
            sys.deleteAirport(deleteNumber)
        elif choice == 3:
            updateNumber = int(input("Enter number of airport: "))
            sys.updateAirport(updateNumber)
        elif choice == 4:
            startNode = int(input("Enter number you want to start from: "))
            endNode = int(input("Enter your destination: "))
            sys.dijkstra(startNode, endNode)