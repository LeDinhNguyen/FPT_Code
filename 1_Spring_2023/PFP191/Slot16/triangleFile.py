inFile = open("triangle.txt")
content = inFile.readlines()
print(content)
lines = []

for line in content:
    line = line.strip()
    if len(line) > 0:
        lines.append(line)
print(lines)

outContent = []
outFile = open("output.txt", "w")


def checkTriangle(a: int, b: int, c: int) -> str:
    if a + b > c and a + c > b and b + c > c:
        if a == b and b == c:
            return "tam giac deu\n"
        elif a == b or b == c or c == a:
            return "tam giac can\n"
        elif a ** 2 + b ** 2 == c ** 2 or a ** 2 + c ** 2 == b ** 2 or c ** 2 + b ** 2 == a ** 2:
            return "tam giac vuong\n"
        return "tam giac thuong\n"
    else:
        return "Ko la tam giac\n"


for line in lines:
    a, b, c = line.split(" ")
    triangle = checkTriangle(int(a), int(b), int(c))
    outContent.append(triangle.format())

outFile.writelines(outContent)
