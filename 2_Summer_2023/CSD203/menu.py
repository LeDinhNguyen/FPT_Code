class Dog:
    def __init__(self):
        self.id = None
        self.name = None
        self.age = None
        self.male = None
    
    def inputInformation(self):
        self.id = input("Enter id: ")
        self.name = input("Enter name: ")
        self.age = int(input("Enter age: "))
        self.male = bool(int(input("1: Male\n0: Female\nEnter sex: ")))

    def sex(self):
        if self.male == True:
            return "Male"
        else:
            return "Female"

    def show(self):
        print("{} - {} - {} - {}".format(self.id, self.name, self.age, self.sex()))

def tinhTong():
    a = int(input("Enter a = "))
    b = int(input("Enter b = "))
    return a + b

def showDogList(dogList):
    for dog in dogList:
        dog.show()

dog_list = []
while True:
	print("""
1. Input dog information
2. Display dog information
3. Summation of 2 integers
0. Exit
""")
	
	num = int(input("Enter number: "))
	if num == 0:
		break
	elif num == 1:
		dog = Dog()
		dog.inputInformation()

	elif num == 2:
		showDogList(dog_list)
	elif num == 3:
		tinhTong()
	else:
		print("Invalid number, ReEnter number: ")
		continue
