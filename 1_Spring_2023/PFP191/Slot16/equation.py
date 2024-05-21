infile = open("input.txt", "r")
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

for line in lines:
    if int(line[0]) == 0:
        if int(line[1]) == 0:
            print("vo so nghiem")
            outContent.append(("vo so nghiem" + "\n"))
        else:
            outContent.append(("vo nghiem" + "\n"))
            print("vo nghiem")
    else:
        outContent.append("nghiem: {0}\n".format(str(-int(line[1]) / int(line[0]))))
        print("nghiem: ", -int(line[1])/int(line[0]))
outfile.writelines(outContent)
