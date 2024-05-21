import random
class Airport:
    def __init__(self, name: str):
        self.name = name
        self.cost = [0]
        self.number = 0

    def showInfo(self):
        print(f"\t- Name: {self.name} \n\t- Cost: {self.cost} \n\t- Number: {self.number}")

class AirportSystem:
    def __init__(self):
        self.airports = []
        self.size = 0

    def __checkAirport(self, name) -> bool:
        for airport in self.airports:
            if airport.name == name:
                return True
        return False

    def __getAirport(self, name: str) -> Airport:
        selectedAirport = None
        for airport in self.airports:
            if airport.name == name:
                selectedAirport = airport
        if not selectedAirport:
            print("Unexisted airport!!")
        return selectedAirport

    def insert(self, name: str) -> None:
        newAirport = Airport(name)

        if self.airports:
            newAirport.number = self.size
            for i in range(self.size):
                cost = int(input(f"Enter cost from {newAirport.name} to {self.airports[i].name}: "))
                # cost = random.randint(0, 200)
                print(f"Enter cost from {newAirport.name} to {self.airports[i].name}: ", cost)
                self.airports[i].cost.append(cost)
                newAirport.cost.insert(i, cost)
            self.airports.append(newAirport)
        else:
            self.airports.append(newAirport)
        self.size += 1

    def delete(self, name: str) -> None:
        number = 0
        for airport in self.airports:
            if airport.name == name:
                number = airport.number
        self.airports.pop(number)
        self.size -= 1

        for i in range(self.size):
            self.airports[i].cost.pop(number)
            self.airports[i].number = i

    def update(self, name: str) -> None:
        airport = self.__getAirport(name)
        for i in range(self.size):
            if i != airport.number:
                cost = random.randint(0, 100)
                self.airports[i].cost[airport.number] = cost
                airport.cost[i] = cost 

    def showMatrix(self) -> None:
        space = 3
        matrix = self.__toMatrix()
        print(" " * (space), end=" ")
        for i in range(self.size):
            print(f" {str(self.airports[i].name).ljust(space)}", end= " ")
        print()

        for i in range(self.size):
            print(str(self.airports[i].name).ljust(space), end= "|")
            for j in range(self.size):
                print(f" {str(matrix[i][j]).ljust(space)}", end="|")
            print()

    def showAirports(self) -> None:
        if self.size > 0:
            print("All airports: ", end=" ")
            for airport in self.airports:
                print(airport.name, end=" ")
            print()
        else:
            print("There is no airports in system!!!")

    def __toMatrix(self) -> list:
        matrix = []
        for item in self.airports:
            matrix.append(item.cost)

        return matrix

    def __dijkstra(self, start, end) -> set:
        numNodes = self.size
        distances = {node: float("inf") for node in range(numNodes)}
        distances[start] = 0 # itself weight = 0 
        visited = set() # directed path
        previous = {}
        
        while len(visited) <  numNodes:
            # tim khoang cach nho nhat
            min_distance = float("inf")
            u = None
            for i in range(numNodes):
                if i not in visited and distances[i] < min_distance:
                    min_distance = distances[i]
                    u = i

            # meet the end node
            if u == end:
                break

            visited.add(u)
            # Relaxation: d[v] = min(d[v], d[u] + (v, u))
            # update weight for all adjency node
            for v in range(numNodes):
                w = self.__toMatrix()[u][v]
                if v not in visited and w > 0:
                    if distances[v] > distances[u] + w:
                        distances[v] = distances[u] + w
                        previous[v] = u 

        print("Here")
        path = []
        curr = end
        while curr in previous:
            path.append(curr)
            curr = previous[curr]
        path.append(start)
        path.reverse()

        return path, distances[end]
    
    def showPath(self, start, end) -> None:
        if self.__checkAirport(start) and self.__checkAirport(end):
            path, d = self.__dijkstra(start, end)
            print(f"Path: {path[0]}", end=" ")
            for i in range(1, len(path)):
                print("--> ", end=f"{i} ")
            print("")
            print(f"Total cost: {d}")
        else:
            print("There is existed airport at start or end destination!!!")

    def airport(self, name: str):
        for airport in self.airports:
            if airport.name == name:
                airport.showInfo()
                return True
        print("No airport!!!")
        return False

def menu():
    print("""
    0. Exit
    1. Add an airport
    2. Remove an airport
    3. Edit information of airport
    4. Show all airports
    5. Find shortest path
    6. Show information of airport
    7. Show Matrix
    """)

def main():
    system = AirportSystem()
    while True:
        menu()
        option = int(input("Enter option: "))
        if option == 0:
            break
        elif option == 1:
            name = int(input("Enter name of an airport: "))
            system.insert(name)
        elif option == 2:
            name = input("Enter airport to remove: ")
            system.delete(name)
        elif option == 3:
            name = input("Enter airport to edit information: ")
            system.update(name)
        elif option == 4:
            system.showAirports()
        elif option == 5:
            start = int(input("Enter number you want to start: "))
            end = int(input("Enter number you want to reach: "))
            system.showPath(start, end)
        elif option == 6:
            number = int(input("Name of airport: "))
            system.airport(number)
        elif option == 7:
            system.showMatrix()
        else:
            print("Unvalid option!!!")
            continue

if __name__ == "__main__":
    main()