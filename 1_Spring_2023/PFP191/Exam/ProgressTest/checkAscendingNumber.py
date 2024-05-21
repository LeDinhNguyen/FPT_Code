def getNumber(string: str):
    num_str = ""
    num = 0
    digit_list = []
    signed = 1
    for ch in string:
        if ch == "-":
            signed = -1
        elif ch.isnumeric():
            if num_str == "0" and ch == "0":
                pass
            else:
                num_str += ch
        else:
            if num_str != "":
                num = int(num_str) * signed
                digit_list.append(num)
            signed = 1
            num_str = ""
    if len(num_str) != 0:     
        digit_list.append(int(num_str))
    return digit_list
            
def checkAscendingNumber(string: str) -> bool:
    number_list = getNumber(string)
    flag = 0

    for i in range(len(number_list) - 1):
        if (number_list[i] > number_list[i+1]):
            flag += 1

    if (flag == 0):
        print("True")
    else:
        print("False")
    return flag == 0

checkAscendingNumber("Soduong12d-3congvao3a1a1a22")
checkAscendingNumber("Soduong-4d-3congvao1a1a1a23")
checkAscendingNumber("Abc3bcd3r5q1a-1a")