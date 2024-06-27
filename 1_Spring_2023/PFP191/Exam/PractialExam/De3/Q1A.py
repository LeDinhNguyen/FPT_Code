'''
Q1 - 3.5 điểm
---------------Phần 1 - 2.5 điểm --------------------
Cho chuỗi s chứa tên của nhân viên FPT như sau:
               Le Thanh Tung
chuyển chuỗi đã cho về dạng email FPT như sau:
output:      tunglt@fpt.edu.vn

Lưu ý: tên có thể có nhiều hơn 3 từ, nhưng quy ước
từ cuối cùng là tên
Ví dụ: tên "Tran Thi Thanh Tam" thì output sẽ là "tamttt"

---------------Phần 2 - 1 điểm --------------------
Cho danh sách nhân viên đọc từ file input.txt, tạo danh sách
nhân viên tương ứng sao cho nếu 2 nhân viên có cùng phần viết tắt
thì đánh số tăng dần sau phần viết tắt
Ví dụ:
trong danh sách có 2 nhân viên là
Le Thanh Tung   và Le Thu Tung
đều có phần viết tắt là tunglt
thì do Le Thanh Tung xuất hiện trước nên không cần thêm số
Le Thu Tung xuất hiện sau nên thêm số bắt đầu từ 2 nghĩa là
Le Thu Tung sẽ có email là: tunglt2@fpt.edu.vn

Đầu vào và đầu ra ví dụ được cung cấp trong file input.txt và out1a.txt

'''

def convertToEmail(fullname: str) -> str:
    result = ""


    return result



def convertToListEmail(names: list) -> list:
    result = []

    return result

def writeListEmailToFile(outFileName: str, mailList: list):
    outFile = open(outFileName, "w")
    for email in mailList:
        outFile.write(email + "\n")
    outFile.close()

def readListMail(inFileName: str):
    inFile = open(inFileName, "r")
    names = []
    for line in inFile:
        line = line.strip()
        names.append(line)
    return names


if __name__ == '__main__':
    #  Phần 1
    s = "Le Thanh Tung"
    output = convertToEmail(s)
    print(output)

    # Phần 2
    names = readListMail("input.txt")
    emails = convertToListEmail(names)
    writeListEmailToFile("out.txt", emails)

