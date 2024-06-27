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
    print(digit_list, end=" Sum = ")
    print(sum(digit_list))
    return digit_list

            
getNumber("Soduong12d-3congvao3a1a1a22")
getNumber("Soduong-4d-3congvao1a1a1a23")
getNumber("Abc3bcd3r5q1a-1a")