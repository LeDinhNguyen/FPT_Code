def readTextFile(File):
    file = open(File, "r")
    for f in file:
        print(f, end="")

def countStartingWithoutT(File):
    count = 0
    file = open(File, "r")
    content = file.read()
    file_line = content.split("\n")
    for line in file_line:
        if not line.startswith("T") and line != "":
            count += 1
    print("No of lines not starting with T is", count)
    return count
readTextFile("poem.txt")
countStartingWithoutT("story.txt")

