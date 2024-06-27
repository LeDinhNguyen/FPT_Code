def isPrime(n: int):
    count = 0
    if n ==0  or n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                count += 1
    return count == 0

infile = open("divisor.txt", "r")
content = infile.readlines()
print(content)
lines = []

outfile = open("output.txt", "w")
outContent = []

for line in content:
    line = line.strip()
    if len(line) > 0:
        lines.append(line.split(" "))
print(lines)

