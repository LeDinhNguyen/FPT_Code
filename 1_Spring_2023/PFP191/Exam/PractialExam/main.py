def convertToEmail(fullname: str) -> str:
    result = ""
    fpt_mail = "@fpt.edu.vn"
    name = fullname.split()
    for i in range(len(name) - 1):
        result += name[i][0].lower()
    result = result + name[-1].lower() + fpt_mail

    return result


def convertToListEmail(names: list) -> list:
    result = []
    count = {}
    for i in range(len(names)):
        if convertToEmail(names[i]) not in result:
            result.append(convertToEmail(names[i]))
            count[convertToEmail(names[i])] = 1
        else:
            count[convertToEmail(names[i])] += 1
            names[i] += str(count[convertToEmail(names[i])])
            result.append(convertToEmail(names[i]))


    return result

# name_list = ["Le Dinh Nguyen", "Le Duong Nguyen", "Tran Thanh Tam", "Tran Thien Tam", "Tran Thi Tam", "Le Thanh Tung", "Le Thanh Thao", "Le Tuan Tung"]
# print(convertToListEmail(name_list))

def convertInt2Bit(n: int, k: int) -> list:
    result = []
    hex_decimal = hex(n)[2::]
    if len(hex_decimal) < k:
        hex_decimal = "0" * (k - len(hex_decimal)) + hex_decimal

    for s in hex_decimal:
        result.append(s.upper())
    return result

# print(convertInt2Bit(10, 5))

def input_students_info():
    students_info = {}
    n = int(input("Nhập số lượng sinh viên: "))
    for i in range(n):
        student_info = {}
        id = input("Nhập mã số sinh viên: ")
        name = input("Nhập tên sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        score = float(input("Nhập điểm số sinh viên: "))
    ##### WRITE YOUR CODE HERE #######
        student_info["name"] = name
        student_info["age"] = age
        student_info["score"] = score
        students_info[id] = student_info
    return students_info

# result = {'a': 2, 'student': 2, 'i': 1, 'am': 1, 'good': 1}
# print(dict(sorted(result.items(), key= lambda items: items[1])))

a = {1:"A"}
print(a.get(1,4))
def convertToListEmail(names: list) -> list:
    result = []
    for name in names:
        name = name.lower().split()
        temp = name[-1]
        for i in range(len(name) - 1):
            temp += name[i][0]
            templen = len(temp)
        while temp in result:
            if temp[templen:].isdigit():
                temp = temp[:templen] + str(int(temp[templen:]) + 1)
                print(temp)
            else:
                temp = temp + "2"
        result.append(temp)
            
    return result