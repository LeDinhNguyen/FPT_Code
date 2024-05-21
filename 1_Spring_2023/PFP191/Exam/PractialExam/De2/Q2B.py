'''
4 điểm
Cho số nguyên dương n và k nhập từ bàn phím.
Viết chương trình lưu trữ dạng biểu diễn
thập lục phân của số nguyên n dưới dạng list
trong hệ biểu diễn k bit.

Ví dụ: n = 499, k = 5
thì ta có biểu diễn nhị phân của 37 là 1F3
trong hệ 5 bit nên kết quả đầu ra là
result = [0, 0, 1, 'F', 3]

'''
def convertInt2Bit(n: int, k: int) -> list:
    result = []
    hex_decimal = hex(n)[2::]
    if len(hex_decimal) < k:
        hex_decimal = "0" * (k - len(hex_decimal)) + hex_decimal

    for s in hex_decimal:
        if s.isnumeric():
            result.append(int(s))
        else:
            result.append(s.upper())

    return result


if __name__ == '__main__':
    #  Phần 1
    n = 499
    k = 5
    result = convertInt2Bit(n, k)
    print(result)
